# -*- coding: utf8 -*-
from phystricks import *
def YRQOoPE():
    pspict,fig = SinglePicture("YRQOoPE")
    pspict.dilatation_X(0.6)
    pspict.dilatation_Y(1)

    vals=[0,3,0,1,4,4,2,1,5,3,1,1]
    pts=[   Point(i,vals[i]) for i in range(0,len(vals))   ]

    for P in pts:
        s=Segment(  Point(P.x,0),P   )
        s.parameters.add_option("linewidth","1.5mm")
        pspict.DrawGraphs(s)

    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()