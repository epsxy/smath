# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def WUEUooYWwanB():
    pspict,fig = SinglePicture("WUEUooYWwanB")

    pspict.dilatation(0.52)

    l=5
    h=4
    perspective=ObliqueProjection(30,0.5)
    A=perspective.point(0,0,0)
    B=perspective.point(l,0,0)
    C=perspective.point(l,0,l)
    D=perspective.point(0,0,l)
    a=2*l/3-0.2
    b=l/3
    S=perspective.point(a,h,b)
    I=perspective.point(a,0,b)

    hauteur=Segment(S,I)
    minidig=Segment(B,I)
    hauteur.parameters.style="dotted"
    minidig.parameters.style="dashed"
    I.put_mark(0.2,angle=45,text="\( I\)",pspict=pspict)

    for pt in [A,B,C,D]:
        pt=pt.rotation(30)

    AB=Segment(A,B)
    BC=Segment(B,C)
    CS=Segment(C,S)
    AS=Segment(A,S)
    BS=Segment(B,S)

    AB.put_mark(0.2,angle=-90,text="\( 4\)",pspict=pspict)

    AD=Segment(A,D)
    AD.parameters.style='dashed'
    DC=Segment(D,C)
    DC.parameters.style='dashed'
    SD=Segment(S,D)
    SD.parameters.style='dashed'

    A.put_mark(0.2,180,"\( A\)",pspict=pspict)
    B.put_mark(0.2,-45,"\( B\)",pspict=pspict)
    C.put_mark(0.2,0,"\( C\)",pspict=pspict)
    D.put_mark(0.1,90+45,"\( D\)",pspict=pspict)
    S.put_mark(0.2,90,"\( S\)",pspict=pspict)

    no_symbol(A,B,C,D,S)
    
    pspict.DrawGraphs(A,B,C,D,S,BS,AB,BC,CS,AS,AD,DC,SD,hauteur,minidig,I)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
