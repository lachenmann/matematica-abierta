"""Figuras reproducibles para el artículo sobre el problema de Basilea."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.special import polygamma

DEST = Path(__file__).resolve().parent
DEST.mkdir(exist_ok=True)
plt.rcParams.update({
    'font.family': 'serif', 'font.size': 10,
    'mathtext.fontset': 'cm', 'axes.spines.top': False,
    'axes.spines.right': False, 'axes.labelsize': 10,
    'legend.fontsize': 9, 'svg.fonttype': 'path',
    'pdf.fonttype': 42, 'savefig.facecolor': 'white',
})

def save(fig, name):
    for ext in ('pdf', 'svg', 'png'):
        metadata = {'Date': None} if ext == 'svg' else ({'CreationDate': None, 'ModDate': None} if ext == 'pdf' else None)
        fig.savefig(DEST / f'{name}.{ext}', dpi=220, bbox_inches='tight', metadata=metadata)
    plt.close(fig)

fig, ax = plt.subplots(1, 2, figsize=(7.0, 2.65), layout='constrained')
n = np.arange(1, 41)
partial = np.cumsum(1.0/n**2)
ax[0].plot(n, partial, color='#195477', linewidth=1.6)
ax[0].scatter(n[::3], partial[::3], s=10, color='#195477')
ax[0].axhline(np.pi**2/6, color='#222222', linestyle='--', linewidth=1,
              label=r'$\pi^2/6$')
ax[0].set(xlabel=r'$N$', ylabel=r'$S_N$', xlim=(1, 40), ylim=(.96, 1.70))
ax[0].legend(loc='lower right', frameon=False)
ax[0].set_title('Sumas parciales', fontsize=11, loc='left')
n = np.arange(1, 1001)
ax[1].loglog(n, 1/n, color='#aa6633', linestyle='--', label=r'$1/N$')
ax[1].loglog(n, polygamma(1, n+1), color='#195477', linewidth=1.7,
             label=r'$S-S_N$')
ax[1].loglog(n, 1/(n+1), color='#555555', linestyle=':', label=r'$1/(N+1)$')
ax[1].set(xlabel=r'$N$', ylabel='Error', xlim=(1, 1000))
ax[1].set_title('Error y cotas', fontsize=11, loc='left')
ax[1].legend(frameon=False)
save(fig, 'convergencia')

fig, ax = plt.subplots(figsize=(7.0, 2.8), layout='constrained')
x = np.linspace(-2.5, 2.5, 1001)
for number, color, style in [(1, '#9b6138', '--'), (3, '#497a65', '-.'),
                              (20, '#5b5790', ':')]:
    factors = 1-x[:,None]**2/(np.arange(1,number+1)[None,:]*np.pi)**2
    ax.plot(x, np.prod(factors,axis=1), color=color, linestyle=style,
            linewidth=1.7, label=fr'$P_{{{number}}}(x)$')
ax.plot(x, np.sinc(x/np.pi), color='#111111', linewidth=1.6,
        label=r'$\sin x/x$')
ax.set(xlabel=r'$x$', ylabel='Valor', xlim=(-2.5, 2.5), ylim=(.20,1.05))
ax.legend(frameon=False, loc='lower center', ncols=4)
save(fig, 'producto_seno')

# Las variantes móviles conservan los datos y dan espacio a sus rótulos.
fig, ax = plt.subplots(2, 1, figsize=(3.7, 5.5), layout='constrained')
n = np.arange(1, 41)
ax[0].plot(n, np.cumsum(1.0/n**2), color='#195477', linewidth=1.6)
ax[0].axhline(np.pi**2/6, color='#222222', linestyle='--', linewidth=1, label=r'$\pi^2/6$')
ax[0].set(xlabel=r'$N$', ylabel=r'$S_N$', xlim=(1,40), ylim=(.96,1.70))
ax[0].legend(loc='lower right',frameon=False)
ax[0].set_title('Sumas parciales',fontsize=11,loc='left')
n = np.arange(1,1001)
ax[1].loglog(n,1/n,color='#aa6633',linestyle='--',label=r'$1/N$')
ax[1].loglog(n,polygamma(1,n+1),color='#195477',linewidth=1.7,label=r'$S-S_N$')
ax[1].loglog(n,1/(n+1),color='#555555',linestyle=':',label=r'$1/(N+1)$')
ax[1].set(xlabel=r'$N$',ylabel='Error',xlim=(1,1000))
ax[1].set_title('Error y cotas',fontsize=11,loc='left')
ax[1].legend(frameon=False)
save(fig,'convergencia-mobile')

fig, ax = plt.subplots(figsize=(3.7,3.3),layout='constrained')
x = np.linspace(-2.5,2.5,1001)
for number,color,style in [(1,'#9b6138','--'),(3,'#497a65','-.'),(20,'#5b5790',':')]:
    factors=1-x[:,None]**2/(np.arange(1,number+1)[None,:]*np.pi)**2
    ax.plot(x,np.prod(factors,axis=1),color=color,linestyle=style,linewidth=1.7,label=fr'$P_{{{number}}}(x)$')
ax.plot(x,np.sinc(x/np.pi),color='#111111',linewidth=1.6,label=r'$\sin x/x$')
ax.set(xlabel=r'$x$',ylabel='Valor',xlim=(-2.5,2.5),ylim=(.20,1.05))
ax.legend(frameon=False,loc='lower center',ncols=2)
save(fig,'producto_seno-mobile')

# El SVG publicado es autocontenido y no necesita una declaración DTD externa.
import re
for svg in DEST.glob('*.svg'):
    clean = re.sub(r'<!DOCTYPE[^>]*>', '', svg.read_text(), flags=re.S)
    svg.write_text('\n'.join(line.rstrip() for line in clean.splitlines()) + '\n')
