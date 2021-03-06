# -*- coding: utf8 -*-
from phystricks import *
def RAACooAwsaVw():
    pspict,fig = SinglePicture("RAACooAwsaVw")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    O=Point(0,0)
    A=Point(-3,-1)
    B=Point(-1.8,2)

    Ap=A.symmetric_by(O)
    Bp=B.symmetric_by(O)

    triangle1=Polygon(A,O,B)
    triangle1.put_mark(0.2,text_list=["\( A\)","\( O\)","\( B\)"],pspict=pspict)
    triangle2=Polygon(O,Ap,Bp)
    triangle2.put_mark(0.2,text_list=["","\( A'\)","\( B'\)"],pspict=pspict)

    triangle1.filled()
    triangle1.fill_parameters.color="lightgray"
    triangle2.filled()
    triangle2.fill_parameters.color="lightgray"

    AAp=Segment(A,Ap)
    AAp.divide_in_two(n=1,d=0.1,l=0.3,pspict=pspict)
    BBp=Segment(B,Bp)
    BBp.divide_in_two(n=2,d=0.1,l=0.3,pspict=pspict)

    #pspict.DrawGraphs(triangle1)  # Si on inverse l'ordre de dessin, c'est marrant.
    pspict.DrawGraphs(triangle2,triangle1,AAp,BBp)  # Si on inverse l'ordre de dessin, c'est marrant.
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

