# -*- coding: utf8 -*-
from phystricks import *
def LNQRooVNAJpf():
    pspict,fig = SinglePicture("LNQRooVNAJpf")
    pspict.dilatation(3)


    A=Point(0,0)
    B=Point(3,0)
    C=Point(0,2)

    trig=Polygon(A,B,C)
    trig.put_mark(0.5,pspict=pspict)

    ang=Angle(C,B,A,r=0.7)
    ang.put_mark(0.6,angle=None,text="\( b\)",automatic_place=(pspict,""))
    ang2=Angle(A,C,B,r=0.7)
    ang2.put_mark(0.6,angle=None,text="\( c\)",automatic_place=(pspict,""))

    trig.edges[0].put_mark(0.5,angle=None,added_angle=180,text="\( 20\)",automatic_place=(pspict,""))
    trig.edges[1].put_mark(0.5,angle=None,added_angle=180,text="\( 25\)",automatic_place=(pspict,""))
    trig.edges[2].put_mark(0.5,angle=None,added_angle=180,text="\( 15\)",automatic_place=(pspict,""))

    no_symbol(trig.vertices)

    pspict.DrawGraphs(trig,ang,ang2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()