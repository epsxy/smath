# -*- coding: utf8 -*-
from phystricks import *
def NNZooNCAqUK():
    from communPhys import petitAKL
    dilat=0.4
    pspict,fig = SinglePicture("NNZooNCAqUK")
    pspict.dilatation(dilat)

    for i in range(0,2):
        for j in range(0,3):
            pspict.DrawGraphs(petitAKL(i,j))
    for j in range(0,3):
        pet=petitAKL(0,j)
        pet.hatched()
        pet.hatch_parameters.color='gray'
        pspict.DrawGraphs(pet)
    for j in range(0,2):
        pet=petitAKL(1,j)
        pet.filled()
        pet.fill_parameters.color='lightgray'
        pspict.DrawGraphs(pet)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
