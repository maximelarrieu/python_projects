#!usr/bin/python3

def convert(md):
    h1 = '#'
    h2 = '##'
    h3 = '###'
    if h1 == '#':
        md.replace('#', '<h1>')
    if h2 == '##':
        md.replace('##', '<h2>')
    if h3 == '###':
        md.replace('###', '<h3>')


md_file = open("README.md", "r")
md = md_file.read()
html = convert(md)
print(html)