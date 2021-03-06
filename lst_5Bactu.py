#! /usr/bin/python
# -*- coding: utf8 -*-

import latexparser
import latexparser.PytexTools
import commun

myRequest = latexparser.PytexTools.Request("seconde")
myRequest.original_filename="automatedChapter.tex"


def set_filename(medicament):
    medicament.new_output_filename="0-actu5B.pdf"

classe="5B"
fract=commun.OneChapter("Écriture fractionnaire",classe)
droites_rem=commun.OneChapter("Droites remarquables dans un triangle",classe)
ops_frac=commun.OneChapter("Opérations sur les fractions",classe)
sym_centrale=commun.OneChapter("Symétrie centrale",classe)
exp_litt=commun.OneChapter("Expressions littérales",classe)
nombres_relatifs=commun.OneChapter("Nombres relatifs",classe)
ang_parall=commun.OneChapter("Angles et parallélisme",classe)
proportio=commun.OneChapter("Proportionnalité",classe)


actu5=proportio
actu5.set_filename=set_filename
actu5.write_the_file()

myRequest.add_plugin(actu5.set_filename,"medicament")
myRequest.ok_filenames_list=actu5.ok_filenames_list()
