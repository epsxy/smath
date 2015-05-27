#! /usr/bin/python
# -*- coding: utf8 -*-

import commun
import LaTeXparser
import LaTeXparser.PytexTools

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="rituel.tex"

myRequest.ok_filenames_list=["e_smath"]
myRequest.ok_filenames_list.append("40_rituel5")
myRequest.ok_filenames_list.append("41_rituel4")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")

myRequest.add_plugin(commun.set_filename("0-rituel.pdf"),"medicament")
