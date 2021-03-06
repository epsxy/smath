# -*- coding: utf8 -*-
from phystricks import *
def RYNYooMFTMNR():
    pspicts,figs = IndependentPictures("RYNYooMFTMNR",5)
    for psp in pspicts :
        psp.dilatation(1)   

    v=(0,-1.5)
    A=Point(0,0)
    B=Point(6,0)
    C=A+v
    D=B+v

    s1=Segment(A,B)
    s2=Segment(C,D)

    angle=30*degree
    I=s2.get_point_proportion(0.2)
    directeur=(  cos(angle.radian),sin(angle.radian)  )
    support=Segment(I,I+directeur)
    J=Intersection(s1,support)[0]

    s3=Segment(I,J).dilatation(1.7)
    for psp in pspicts:
        psp.DrawGraphs(s1,s2,s3)

    r=0.5
    a1=AngleAOB(D,I,s3.F,r)
    a2=AngleAOB(B,J,s3.F,r)
    b1=a1
    b2=AngleAOB(A,J,s3.I,r)
    c1=AngleAOB(s3.F,J,A,r)
    c2=AngleAOB(s3.F,I,C,r)
    d1=AngleAOB(I,J,B,r)
    d2=AngleAOB(s3.I,I,D,r)
    e1=AngleAOB(J,I,C,r)
    pspicts[0].DrawGraphs(a1,a2)

    pspicts[1].DrawGraphs(b1,b2)
    pspicts[2].DrawGraphs(d1,d2)
    pspicts[3].DrawGraphs(d1,e1)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
