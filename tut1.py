#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
#       (C) 2016 Alchimista <alchimistawp@gmail.com>
#
#        Distributed under the terms of the GNU GPL license.

import pywikibot

# Definir qual o projecto a trabalhar
site = pywikibot.Site("pt", "wikipedia")

# definir a página
wpage = pywikibot.Page(site, "wikipédia:Página de testes/4")

# Obter o wikitexto da página
wpagetext = wpage.text

# Um print do wikitexto, para comprovar
print("\n::::::::::::\n", wpagetext, "\n::::::::::\n")

# Definimos o novo texto
newtext = u"Olá Mundo! Isto é um teste de edição :D"

# mostra o diferencial da edição sem salvar as alterações
pywikibot.showDiff(wpagetext, newtext)


