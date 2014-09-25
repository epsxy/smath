#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="smath.tex"

myRequest.ok_filenames_list=["e_smath"]
myRequest.ok_filenames_list.append("2_mental5")
myRequest.ok_filenames_list.append("13_fract")
myRequest.ok_filenames_list.append("15_evaluation")
myRequest.ok_filenames_list.append("14_methodologie")
myRequest.ok_filenames_list.append("7_exercices_feuilles_cinquieme")
myRequest.ok_filenames_list.append("8_triangles")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
