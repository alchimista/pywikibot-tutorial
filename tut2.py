#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#	   
#	   (C) 2012 Alchimista <alchimistawp@gmail.com>
#		 
#		Distributed under the terms of the GNU GPL license.



import pywikibot


def main():
    site = pywikibot.Site("pt", "wikipedia")  # definimos que o site é a pt.wp

    cat = pywikibot.Category(site, u"Ambiente")  # Aqui definimos a categoria Ambiente.
    catList = cat.members()

    # Vamos verificar o título:
    print(cat.title())

    # O título sem o namespace:
    print(cat.title(withNamespace=False))

    # Informações sobre a categoria:
    print(cat.categoryinfo)

    # Ou elementos isolados:

    # Nº de subcategorias
    print("Nº de subcategorias: ", cat.categoryinfo['subcats'])

    # Nº de páginas
    print("Nº de páginas: ", cat.categoryinfo['pages'])

    # Nº de ficheiros
    print("Nº de ficheiros: ", cat.categoryinfo['files'])

    # Vamos então percorrer todos páginas, ficheiros e subcategorias
    for page in catList:
        print("Título da página: ", page.title())  # mostra o título do artigo

    # Se for preciso filtrar somente os artigos do domínio principal,
    # voltamos ao nosso objecto cat e filtramos os membros

    artigos_da_cat = cat.members(namespaces=0)  # retorna somente os elementos
    # do domínio principal

    print("\n---- Artigos do domínio principal: ----\n")
    for i in artigos_da_cat:
        print(i.title())


if __name__ == "__main__":
    try:
        main()
    finally:
        pywikibot.stopme()
