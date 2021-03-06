# -*- coding: utf8 -*-
from phystricks import *
def CFFyezr():
    pspict,fig = SinglePicture("CFFyezr")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.7)

    S1=Point(1,1)
    S2=Point(6,2)

    v1=AffineVector( S1,S1+(1,2) )
    v2=AffineVector(S2,S2+(-1,1))

    S1.put_mark(0.2,text="\( S_1\)",pspict=pspict,position="N")
    S2.put_mark(0.2,text="\( S_2\)",pspict=pspict,position="corner")

    pspict.DrawGraphs(S1,S2,v1,v2)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

