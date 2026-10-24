import pathlib,json
from PIL import Image,ImageDraw
R=pathlib.Path(__file__).resolve().parent;Q=R/'demo/qa'
items=json.loads((Q/'extraccion.json').read_text())['full_resolution']
for start in range(0,len(items),4):
    canvas=Image.new('RGB',(1920,1128),'#18202b');draw=ImageDraw.Draw(canvas)
    for j,item in enumerate(items[start:start+4]):
        x=j%2*960;y=j//2*564
        with Image.open(item['path']) as img:canvas.paste(img.resize((960,540)),(x,y))
        draw.text((x+8,y+543),f"{item['id']} @ {item['time']:.3f}s",fill='white')
    canvas.save(Q/f'estados_{start//4:02d}.jpg',quality=95)
