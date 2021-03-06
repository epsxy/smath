# -*- coding: utf8 -*-
from phystricks import *
def VGQoojvDGr():
    pspict,fig = SinglePicture("VGQoojvDGr")
    pspict.dilatation_X(0.6)
    pspict.dilatation_Y(1)

    O=Point(0,0)
    I=Point(1,0)
    A=Point(3,0)
    B=Point(4,0)
    C=Point(7,0)
    K=Point(-1,0)
    L=Point(-5,0)

    A.put_mark(0.2,text="\( A\)",pspict=pspict,position="N")
    B.put_mark(0.2,text="\( B\)",pspict=pspict,position="N")
    C.put_mark(0.2,text="\( C\)",pspict=pspict,position="N")
    K.put_mark(0.2,text="\( K\)",pspict=pspict,position="N")
    L.put_mark(0.2,text="\( L\)",pspict=pspict,position="N")
    O.put_mark(0.2,text="\( O\)",pspict=pspict,position="N")
    I.put_mark(0.2,text="\( I\)",pspict=pspict,position="N")

    pspict.DrawGraphs(A,B,C,K,L,O,I)

    pspict.axes.no_numbering()
    pspict.axes.draw_single_axeY=False
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
