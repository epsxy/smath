# -*- coding: utf8 -*-
from phystricks import *
def ZQfGNsD():
    pspict,fig = SinglePicture("ZQfGNsD")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction(2*x).graph(-1.5,3)
    g=phyFunction(-x+4).graph(-1.5,5)

    f.put_mark(0.2,text="\( f\)",pspict=pspict,position="W")
    g.put_mark(0.2,text="\( g\)",pspict=pspict,position="W")

    g.parameters.color="brown"

    pspict.DrawGraphs(f,g)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
