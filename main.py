import requests
from flask import Flask, redirect, url_for, request, jsonify, render_template,make_response,send_file
import os
from colorthief import ColorThief
import shutil

## get current path
cwd=os.getcwd()

##### get user site name
sitename=(input("Enter site name:\n"))


if not os.path.exists(f'{cwd}\\{sitename}'):
  os.mkdir(sitename)
  os.mkdir(f'{sitename}\\site')
  #open(f'{sitename}\\setup.py','w').close()
  open(f'{sitename}\\site\\index.html','w').close()
  #open(f'{sitename}\\iframe.html','w').close()
  open(f'{sitename}\\site\\script.js','w').close()
  open(f'{sitename}\\site\\style.css','w').close()
  #open(f'{sitename}\\ups.txt','w').close()

## create script.js
with open("templates/scripttemplate.js",'r') as scripttemp:
  scriptjs=scripttemp.read()
with open(sitename+"\\site\\script.js",'w') as scripttemp:
    scripttemp.write(scriptjs)

## create style.css
with open("templates/styletemplate.css",'r') as styletemp:
  stylecss=styletemp.read()
with open(sitename+"\\site\\style.css",'w') as styletemp:
    styletemp.write(stylecss)

## create index.html
with open ("templates/indextemplate.html",'r') as itemp:
  itemphtml=itemp.read()
with open(sitename+"\\site\\index.html",'w') as itemp:
    itemp.write(itemphtml)

## create host.py
with open ("templates/hosttemplate.py",'r') as hosttemp:
  hosttempdata =hosttemp.read()
with open(sitename+"/host.py",'w') as hosttemp:
    hosttemp.write(hosttempdata)

## get image source and save to logo.png
logosource=input("select:\n1. Local png file,\n2. online imagelink:\n")

if logosource == '1':
  logo = input("enter path:\n")[1:-1]
  shutil.copy(logo, sitename+"\\site\\logo.png")


if logosource=='2':
  logo=input("Enter logo link:\n")
  img_data = requests.get(logo).content
  with open(sitename+"\\site\\logo.png", 'wb') as handler:
      handler.write(img_data)

## get pallete
color_thief = ColorThief(sitename+"\\site\\logo.png")
dominant_color = color_thief.get_color(quality=1)
palette = color_thief.get_palette(color_count=6)[0]
print(palette)

## save bg color in hex
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb
bgcolor=(rgb_to_hex(palette))
print(bgcolor)

## insert colors into index.html
with open(sitename+"\\site\\index.html","r") as mf:
  md=mf.read()
  md=md.replace('ffffff',bgcolor)
  md=md.replace("<title>Client Portal</title>",f'<title>{sitename}</title>')
with open(sitename+"\\site\\index.html","w") as mf:
  mf.write(md)

