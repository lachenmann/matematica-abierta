import test from 'node:test';
import assert from 'node:assert/strict';
import { ACCOUNT_SESSION_KEY, BrowserSupabaseClient, hasStoredAccountSession } from '../supabase-browser-client.mjs';
const UID='00000000-0000-4000-8000-000000000001';
function setup(fetchImpl, expires=0, timeoutMs=1000) {
  const map=new Map();
  const storage={getItem:k=>map.get(k)??null,setItem:(k,v)=>map.set(k,String(v)),removeItem:k=>map.delete(k)};
  storage.setItem(ACCOUNT_SESSION_KEY,JSON.stringify({access_token:'old',refresh_token:'refresh-old',
    expires_at:expires,user:{id:UID,is_anonymous:true}}));
  const client=new BrowserSupabaseClient({projectUrl:'https://qa.supabase.co',publishableKey:'sb_publishable_fixture',storage,fetchImpl,timeoutMs});
  return {client,storage};
}
const response=(status,body)=>({ok:status<400,status,text:async()=>JSON.stringify(body)});

test('Un refresh offline conserva los tokens y no convierte la identidad en local ni crea otra', async()=>{
  let offline=true, refreshed=0, signups=0;
  const {client,storage}=setup(async(url,options)=>{
    if(url.endsWith('/signup')) signups++;
    if(offline) throw Error('offline');
    if(url.includes('grant_type=refresh_token')) {
      refreshed++;
      assert.equal(JSON.parse(options.body).refresh_token,'refresh-old');
      return response(200,{access_token:'new',refresh_token:'refresh-new',expires_in:3600,user:{id:UID,is_anonymous:true}});
    }
    return response(200,{id:UID,is_anonymous:true});
  });
  const before=storage.getItem(ACCOUNT_SESSION_KEY);
  const failed=await client.auth.getUser();
  assert.match(failed.error.message,/offline/); assert.equal(failed.data,null);
  assert.equal(storage.getItem(ACCOUNT_SESSION_KEY),before); assert.equal(hasStoredAccountSession(storage),true);
  offline=false;
  assert.equal((await client.auth.getUser()).data.user.id,UID);
  assert.equal(refreshed,1); assert.equal(signups,0);
});

test('Un error de Auth permanente se comunica, sin destruir silenciosamente una cuenta anónima',async()=>{
  const {client,storage}=setup(async()=>response(400,{message:'Refresh token not found',error_code:'refresh_token_not_found'}));
  const before=storage.getItem(ACCOUNT_SESSION_KEY);
  assert.ok((await client.auth.getUser()).error);
  assert.equal(storage.getItem(ACCOUNT_SESSION_KEY),before);
});

test('Consultas simultáneas comparten una sola renovación de token',async()=>{
  let renewals=0;
  const {client}=setup(async(url)=>{
    if(url.includes('grant_type=refresh_token')) {
      renewals++;
      await new Promise(resolve=>setTimeout(resolve,10));
      return response(200,{access_token:'new',refresh_token:'r2',expires_in:3600,user:{id:UID,is_anonymous:true}});
    }
    return response(200,{id:UID,is_anonymous:true});
  });
  const results=await Promise.all([client.auth.getUser(),client.auth.getUser(),client.auth.getUser()]);
  assert.equal(renewals,1); assert.ok(results.every(r=>r.data.user.id===UID));
});

test('El transporte cancela una petición suspendida y conserva la sesión',async()=>{
  const {client,storage}=setup(async(_url,options)=>new Promise((_resolve,reject)=>{
    options.signal.addEventListener('abort',()=>reject(Error('aborted')),{once:true});
  }),Math.floor(Date.now()/1000)+3600,15);
  const before=storage.getItem(ACCOUNT_SESSION_KEY);
  const result=await client.rpc('ma_finish_practice_session',{});
  assert.equal(result.error.code,'TIMEOUT'); assert.equal(storage.getItem(ACCOUNT_SESSION_KEY),before);
});

test('Una cola de otra cuenta no se transmite aunque el token activo haya cambiado',async()=>{
  let calls=0;
  const {client}=setup(async()=>{calls++;return response(200,{});},Math.floor(Date.now()/1000)+3600);
  const result=await client.rpc('ma_finish_practice_session',{p_record:{title:'private'}},{expectedUserId:'another-user'});
  assert.match(result.error.message,/otra identidad/); assert.equal(calls,0);
});

test('Un cuerpo de respuesta interrumpido deja el resultado incierto y no borra el refresh token',async()=>{
  const {client,storage}=setup(async()=>({ok:true,status:200,text:async()=>{throw Error('body interrupted');}}),Math.floor(Date.now()/1000)+3600);
  const result=await client.rpc('ma_finish_practice_session',{});
  assert.equal(result.error.code,'NETWORK_ERROR'); assert.equal(hasStoredAccountSession(storage),true);
});
