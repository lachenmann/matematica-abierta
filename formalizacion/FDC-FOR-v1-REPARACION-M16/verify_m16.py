"""M16 negative compilation and history controls; no proof rule is added."""
from pathlib import Path
import subprocess,json,hashlib
root=Path(__file__).resolve().parent
repo=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
base='390684ab0fce64cb710260fdde321c19cefe3547'
subprocess.run(['git','merge-base','--is-ancestor',base,'HEAD'],cwd=repo,check=True)
rows=json.loads((root/'base-manifest.json').read_text())
for row in rows:
 data=subprocess.check_output(['git','cat-file','blob',row['sha']],cwd=repo)
 assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==row['sha']
historical=subprocess.check_output(['git','show',base+':lean/MatematicaAbierta/Continuo/AuditoriaGuardaRenombradoRCA.lean'],cwd=repo)
assert (repo/'forensics/M15/AuditoriaGuardaRenombradoRCA.lean').read_bytes()==historical
trusted=list((repo/'lean/MatematicaAbierta').rglob('*.lean'))+[repo/'lean/MatematicaAbierta.lean']
assert all('import MatematicaAbierta.Continuo.AuditoriaGuardaRenombradoRCA' not in p.read_text() for p in trusted)
inv=json.loads((root/'static-invocations.json').read_text())
assert len(inv)==41 and len({r['module'] for r in inv})==18
assert sum(r['x']==r['y'] for r in inv)==2
for filename,reason in [('OldSignature.lean','type mismatch'),('CapturedBody.lean','decide')]:
 p=root/'negative'/filename
 result=subprocess.run(['lake','env','lean','-DautoImplicit=false',str(p)],cwd=repo/'lean',text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 (root/(filename+'.rejected.log')).write_text(result.stdout)
 assert result.returncode!=0,(filename,'unexpectedly accepted')
 assert reason.lower() in result.stdout.lower(),(filename,result.stdout)
 assert 'sorryAx' not in result.stdout,(filename,'uncontrolled recovery')
 print('REJECTED',filename,flush=True)
print('M16_HISTORY_AND_NEGATIVE_PASS',flush=True)
