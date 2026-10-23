# Cortina oficial de `IntroCanal`

## Fuente

- **Título:** Simple Piano Logo
- **Autor:** _MC5_
- **Freesound sound ID:** 524847
- **URL:** https://freesound.org/people/_MC5_/sounds/524847/
- **Licencia:** Creative Commons Attribution 4.0 (CC BY 4.0)
- **Fuente original:** WAV, 44.1 kHz, 16 bit, stereo, 8.000 s

## Atribución para descripción/créditos

> “Simple Piano Logo” — _MC5_, Freesound.org — CC BY 4.0.

La versión usada por Matemática Abierta es una adaptación técnica: se convierte a
48 kHz/stereo, se fija a 7.00 s y se aplica un fade-out de 0.65 s. No se hace loop.

## Pipeline

El archivo canónico local es:

`assets/audio/intro/CPM-intro-music.wav`

Se genera de forma reproducible con:

`prepare-intro-music.ps1`

El script busca dentro de `audiovisual/manim` un archivo cuyo nombre contenga
`524847`, o coincida con “Simple Piano Logo”, y crea el WAV canónico.

En Manim la cortina se reproduce a `-18 dB` y sólo durante los primeros 7.00 s
de `IntroCanal`. Después de la intro, el resto del video queda sólo con voz.


La voz de cada clase conserva su WAV/RPP intacto y comienza a los `7.00 s` del video; todos los marcadores Reaper se interpretan con ese desplazamiento global.
