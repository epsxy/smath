# -*- coding: utf8 -*-
from phystricks import *
def ZBHLooYfpkZA():
    pspict,fig = SinglePicture("ZBHLooYfpkZA")
    pspict.dilatation(2)

    D=Point(0,0)
    B=Circle(D,6).get_point(25)
    C=Point(B.x,D.y)
    A=Point(D.x,B.y)

    rect=Polygon(A,B,C,D)
    rect.put_mark(0.4,pspict=pspict)
    rect.make_edges_independent()

    #for s in rect.edges:
    #    pspict.DrawGraphs(s.dilatation(1.3))
    
    a20=AngleAOB(C,D,B,r=0.9)
    a20.put_mark(0.6,angle=2,added_angle=0,text="\SI{25}{\degree}",automatic_place=(pspict,"corner"))

    ai1=AngleAOB(D,B,C)
    ai2=AngleAOB(B,D,A)
    for ang in [ai1,ai2]:
        ang.put_mark(0.4,angle=None,added_angle=0,text="?",automatic_place=(pspict,""))

    diag=Segment(D,B)

    no_symbol(rect.vertices)
    pspict.comment="L'angle en B est mal tracé. Problème dans l'arc de cercle à régler."
    pspict.DrawGraphs(rect,ai1,ai2,a20,diag)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()