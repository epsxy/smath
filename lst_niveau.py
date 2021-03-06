#! /usr/bin/python
# -*- coding: utf8 -*-

import sys
import commun
import latexparser
import latexparser.PytexTools

myRequest = latexparser.PytexTools.Request("seconde")
myRequest.original_filename="smath.tex"

#myRequest.ok_filenames_list=["e_smath"]

if "cinquième" in sys.argv:
    ok_mark_list=commun.cinquieme_mark_list
    myRequest.add_plugin(commun.set_filename("0-cinquième.pdf"),"medicament")
if "quatrième" in sys.argv:
    ok_mark_list=commun.quatrieme_mark_list
    myRequest.add_plugin(commun.set_filename("0-quatrième.pdf"),"medicament")
if "seconde" in sys.argv:
    ok_mark_list=commun.seconde_mark_list
    myRequest.add_plugin(commun.set_filename("0-seconde.pdf"),"medicament")
if "première" in sys.argv:
    ok_mark_list=commun.premiere_mark_list
    myRequest.add_plugin(commun.set_filename("0-premiere.pdf"),"medicament")
if "autres" in sys.argv:
    ok_mark_list=commun.autre_mark_list
    myRequest.add_plugin(commun.set_filename("0-autres.pdf"),"medicament")

myRequest.add_plugin(latexparser.PytexTools.accept_all_input,"medicament")
myRequest.add_plugin(latexparser.PytexTools.keep_script_marks(ok_mark_list),"before_pytex")
