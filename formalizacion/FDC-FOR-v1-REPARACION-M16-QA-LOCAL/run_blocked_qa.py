from pathlib import Path
import os, subprocess, json, datetime, hashlib
root=Path(__file__).resolve().parent.parent
repo=root/'checkout'; cwd=repo/'lean'; logs=root/'logs'
env=os.environ.copy()
runtime=root/'runtime/lean-4.34.1-linux'
env.update(PATH=str(runtime/'bin')+':'+env['PATH'], LEAN=str(runtime/'bin/lean'), LEAN_SYSROOT=str(runtime), LAKE_HOME=str(runtime/'src/lean/lake'))
records=[]
def run(label,args,workdir=cwd):
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    path=logs/(label+'.log')
    with path.open('wb') as out:
        result=subprocess.run(args,cwd=workdir,env=env,stdout=out,stderr=subprocess.STDOUT)
    row=dict(label=label,args=args,cwd=str(workdir),start=started,end=datetime.datetime.now(datetime.timezone.utc).isoformat(),exit_code=result.returncode,log=str(path.relative_to(root)),sha256=hashlib.sha256(path.read_bytes()).hexdigest())
    records.append(row)
    (root/'evidence/local-exit-codes.json').write_text(json.dumps(records,indent=2)+'\n')
    print(label,'observed_exit_code',result.returncode,flush=True)
run('lean-version',[str(runtime/'bin/lean'),'--version'])
run('lake-version',['lake','--version'])
run('cache-get',['lake','exe','cache','get'])
run('lake-build-wfail',['lake','build','--wfail'])
for filename in ['OldSignature.lean','CapturedBody.lean']:
    run(filename+'.environment-failure',['lake','env','lean','-DautoImplicit=false',str(repo/'formalizacion/FDC-FOR-v1-REPARACION-M16/negative'/filename)])
run('verify-m16',['python',str(repo/'formalizacion/FDC-FOR-v1-REPARACION-M16/verify_m16.py')],repo)
