from pathlib import Path
ROOT=Path(__file__).resolve().parent
EXPORTS=ROOT
GENERADOS=ROOT/"generados"
def srt_time(t):
 m=round(t*1000);h,m=divmod(m,3600000);mi,m=divmod(m,60000);s,m=divmod(m,1000);return f"{h:02d}:{mi:02d}:{s:02d},{m:03d}"
