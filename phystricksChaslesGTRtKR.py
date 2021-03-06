# -*- coding: utf8 -*-
from phystricks import *
def ChaslesGTRtKR():
    pspict,fig = SinglePicture("ChaslesGTRtKR")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(1,3)
    C=Point(2,2)

    AB=AffineVector(A,B)
    BC=AffineVector(B,C)
    AC=AffineVector(A,C)

    AB.parameters.color="blue"
    BC.parameters.color="blue"
    AC.parameters.color="red"

    A.parameters.symbol=""
    B.parameters.symbol=""
    C.parameters.symbol=""

    A.put_mark(0.2,-90,"\( A\)",pspict=pspict)
    B.put_mark(0.2,90,"\( B\)",pspict=pspict)
    C.put_mark(0.2,0,"\( C\)",pspict=pspict)

    pspict.DrawGraphs(AB,BC,AC,A,B,C)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
