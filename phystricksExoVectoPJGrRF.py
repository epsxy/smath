# -*- coding: utf8 -*-
from phystricks import *
def ExoVectoPJGrRF():
    pspict,fig = SinglePicture("ExoVectoPJGrRF")
    pspict.dilatation(0.7)

    A=Point(0,0)
    B=Point(-1,6)
    C=Point(3,3)

    A.put_mark(0.2,45,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,45,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,45,"\( C\)",automatic_place=pspict)

    pspict.DrawGraphs(A,B,C)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
