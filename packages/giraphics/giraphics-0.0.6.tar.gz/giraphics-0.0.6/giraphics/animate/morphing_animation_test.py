import numpy as np

from giraphics.animate.animation import Animation
from giraphics.svg.morph2 import SVGPathObject, morph
from svg.path import Path, Line, CubicBezier, QuadraticBezier, Arc, Move, parse_path

# path1 = Path(Move(to = 0+0j), Line(start=0 + 0j, end=1 + 1j))
# path2 = Path(Move(to = 0+0j), Line(start=0 + 0j, end=1 -2j))


path1 = 'M 2 1 Q -1 1 -1 -1 L 0 0'
path2 = 'M 2 1 Q -1 1 -1 -1 L 0 0'

spo1 = SVGPathObject(path1, stroke='red', strokewidth=2)
spo2 = SVGPathObject(path2, stroke='black', strokewidth=2)


morphing1 = spo1.morph_to(spo2)

A = Animation('test4.mp4', 800, 800, 20, 20)

frames = 60

for i in range(frames):
    A.plate.bg(colour='white')
    morphing1(i/frames).draw(A)
    # print(morphing1(i/frames).pathObj)
    A.plate.press()

A.develop(cleanup=False)
