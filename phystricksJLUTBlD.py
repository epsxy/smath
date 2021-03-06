# -*- coding: utf8 -*-
from phystricks import *

x=var("x")
f=phyFunction(3*x-1).graph(-0.5,2)
g=phyFunction(-x+3).graph(-2,4)

def JLUTBlD():
    pspict,fig = SinglePicture("JLUTBlD")
    pspict.dilatation_X(0.8)
    pspict.dilatation_Y(0.8)


    P=g.get_point(-2)
    Q=g.get_point(4)
    P.parameters.symbol=""
    Q.parameters.symbol=""

    f.parameters.color="red"

    pspict.DrawGraphs(f,P,Q)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def JWNtVIR():
    pspict,fig = SinglePicture("JWNtVIR")
    pspict.dilatation_X(0.8)
    pspict.dilatation_Y(0.8)


    P=g.get_point(-2)
    Q=g.get_point(4)
    P.parameters.symbol=""
    Q.parameters.symbol=""

    f.parameters.color="red"
    g.parameters.color="brown"

    f.put_mark(0.2,0,"\( f\)",pspict=pspict,position="W")
    g.put_mark(0.2,0,"\( g\)",pspict=pspict,position="W")

    pspict.DrawGraphs(f,g,P,Q)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

