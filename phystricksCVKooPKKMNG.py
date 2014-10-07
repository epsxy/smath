# -*- coding: utf8 -*-
from phystricks import *
def CVKooPKKMNG():
    pspict,fig = SinglePicture("CVKooPKKMNG")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    B=Point(0,0)
    C=Point(8,0)

    m1=Circle(B,6).get_point(40)
    m2=Circle(C,6).get_point(180-40)
    s1=Segment(B,m1)
    s2=Segment(C,m2)
    s1.parameters.style="dashed"
    s2.parameters.style="dashed"

    A=Intersection(s1,s2)[0]

    A.put_mark(0.2,90,"\( A\)",automatic_place=(pspict,"S"))
    B.put_mark(0.2,180+45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,-45,"\( C\)",automatic_place=(pspict,"corner"))

    trig=Polygon(A,B,C)

    a1=Angle(C,B,A,r=1)
    a3=Angle(A,C,B,r=1)

    a1.put_mark(0.3,a1.advised_mark_angle,"\SI{40}{\degree}",automatic_place=(pspict,"center"))
    a3.put_mark(0.3,a3.advised_mark_angle,"\SI{40}{\degree}",automatic_place=(pspict,"center"))

    pspict.DrawGraphs(A,B,C,s1,s2,trig,a1,a3)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()