# -*- coding: utf8 -*-
from phystricks import *
def RVZNtGK():
    pspict,fig = SinglePicture("RVZNtGK")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(2,1)
    B=Point(4,2)
    C=Point(8,4)

    ligne=Segment(A,C).dilatation(1.5)

    A.put_mark(0.2,135,"\( A(x_A;y_A)\)",pspict=pspict,position="corner")
    B.put_mark(0.2,135,"\( B(x_B;y_B)\)",pspict=pspict,position="corner")
    C.put_mark(0.2,135,"\( C(x_C;y_C)\)",pspict=pspict,position="corner")

    R=Point(B.x,A.y)
    S=Point(C.x,A.y)

    s1=Segment(B,R)
    s2=Segment(C,S)
    s3=Segment(A,S)

    s1.parameters.style="dotted"
    s2.parameters.style="dotted"
    s3.parameters.style="dotted"

    m1=MeasureLength(s1,-0.2)
    m1.put_mark(0.2,text="\( y_B-y_A\)",pspict=pspict,position="W")
    m2=MeasureLength(s2,-0.2)
    m2.put_mark(0.2,text="\( y_C-y_A\)",pspict=pspict,position="W")
    m3=MeasureLength(s3,0.2)
    m3.put_mark(0.1,text="\( x_C-x_A\)",pspict=pspict,position="N")
    m4=MeasureLength(Segment(A,R),0.5)
    m4.put_mark(0.1,text="\( x_B-x_A\)",pspict=pspict,position="N")

    pspict.DrawGraphs(ligne,A,B,C,s1,s2,s3,m1,m2,m3,m4)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
