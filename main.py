import PIL
import PIL.Image
import tkinter
from PIL import Image, ImageTk,ImageOps
from tkinter import *
from tkinter import filedialog
import os
from os import listdir
from os.path import isfile, join
import sys
from pathlib import Path
dirname = os.path.dirname(__file__)


if sys.version_info[0] < 3:
   import Tkinter as tk
else:
   import tkinter as tk
x = 0
def p1CharChange(pics,bigpic):
    im1 = "hi"
    im1 = PIL.Image.open(os.path.join("characters",bigpic))
    im1 = im1.save(os.path.join(dirname, "P1Char.png"))
def p2CharChange(pics,bigpic):
    im2 = "hi"
    im2 = PIL.Image.open(os.path.join(os.path.join(dirname, "Characters",bigpic)))
    im2 = im2.save(os.path.join(dirname, "P2Char.png"))

def p1SetTag(tag):
    tag = str(tag)
    text_file = open(os.path.join(dirname, "p1Tag.txt"), "wt")
    n = text_file.write(tag)
    text_file.close()

def p2SetTag(tag):
    tag = str(tag)
    text_file = open(os.path.join(dirname, "p2Tag.txt"), "wt")
    n = text_file.write(tag)
    text_file.close()

#def fullScreenSwitch():
#    global fullscreen
#    x += 1
#    if x % 2 == 0:
#        fullscreen = False
#    else:
#        fullscreen = True
#    return fullscreen

bigPicFiles = [f for f in listdir(os.path.join(dirname, "Characters")) if isfile(join(os.path.join(dirname, "Characters", f)))]
bigPics = []
for x in range (0, len(bigPicFiles)):
    bigTemp = open(os.path.join(os.path.join(dirname, "Characters", bigPicFiles[x])), "rb")
    bigPic = PIL.Image.open(bigTemp)
    bigPics.append(bigPic)


smolPicFiles = [f for f in listdir(os.path.join(dirname, "Small Chars")) if isfile(join(os.path.join(dirname, "Characters", f)))]
smolPics = []
for x in range (0, len(smolPicFiles)):
    smolTemp = open(os.path.join(os.path.join(dirname, "Small Chars"), smolPicFiles[x]), "rb")
    smolPic = PIL.Image.open(smolTemp)
    smolPics.append(smolPic)


#Start GUI
window = Tk()
def fullScreenSwitch(x):
    x = int(x)
    global fullscreen
    if x % 2 == 0:
        fullscreen = False
    else:
        fullscreen = True
    window.attributes("-fullscreen", fullscreen)
    
window.x = tkinter.IntVar()

window.configure(bg='black')
   
def onClick(event=None):
    window.x.set(window.x.get() + 1)
    intx = window.x.get()
    fullScreenSwitch(intx)
#if x % 2 == 0:
#    fullScreen = False
#else:
#    fullScreen = True

window.geometry('1920x1080')
window.title("Laffs/Gaffs's NASB Stream Tool")
#other images
window.tagImg = PhotoImage(file = os.path.join(dirname, "Tag.png"))
window.Rand = PhotoImage(file = os.path.join(dirname, "random.png"))
window.Yes = PhotoImage(file = os.path.join(dirname, "yes.png"))
window.Divider = PhotoImage(file = os.path.join(dirname, "divider.png"))
window.Fullscreen = PhotoImage(file= os.path.join(dirname, "fullscreen.png"))
window.setLabel = PhotoImage(file= os.path.join(dirname, "Set.png"))
window.win0 = PhotoImage(file= os.path.join(dirname, "scores\win 0.png"))
window.win1 = PhotoImage(file= os.path.join(dirname, "scores\win 1.png"))
window.win2 = PhotoImage(file= os.path.join(dirname, "scores\win 2.png"))
window.win3 = PhotoImage(file= os.path.join(dirname, "scores\win 3.png"))
window.win4 = PhotoImage(file= os.path.join(dirname, "scores\win 4.png"))
window.win5 = PhotoImage(file= os.path.join(dirname, "scores\win 5.png"))
window.null1 = PhotoImage(file= os.path.join(dirname, r"scores\null 1.png"))
window.null2 = PhotoImage(file= os.path.join(dirname, r"scores\null 2.png"))
window.null3 = PhotoImage(file= os.path.join(dirname, r"scores\null 3.png"))
window.null4 = PhotoImage(file= os.path.join(dirname, r"scores\null 4.png"))
window.null5 = PhotoImage(file= os.path.join(dirname, r"scores\null 5.png"))
window.Plus = PhotoImage(file= os.path.join(dirname, "plus.png"))
#characters
window.Zim = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[0])))
window.Spongebob = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[1])))
window.Korra = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[2])))
window.CatDog = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[3])))
window.Toph = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[4])))
window.Sandy = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[5])))
window.RenStimpy = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[6])))
window.Lucy = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[7])))
window.PTM = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[8])))
window.Aang = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[9])))
window.Reptar = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[10])))
window.Leonardo = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[11])))
window.Nigel = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[12])))
window.Michaelangelo = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[13])))
window.Danny = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[14])))
window.Lincoln = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[15])))
window.April = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[16])))
window.Helga = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[17])))
window.Oblina = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[18])))
window.Patrick = PhotoImage(file = os.path.join(os.path.join(dirname, "Small Chars", smolPicFiles[19])))
#widgets
#fullscreen button

fullScreenBtn = Button(window, image= window.Fullscreen, borderwidth = 0, command= onClick, width= 50)
fullScreenBtn.place(x=5,y=5)
#divider
divider = tkinter.Label(image= window.Divider,borderwidth=0)
divider.place(x=955,y=0)
#Set Score Labels
labY = 860
numY = 880
window.scoreone = tkinter.IntVar(value=0)
window.scoretwo = tkinter.IntVar(value=0)
def onClick3(event=None):
   window.scoretwo.set(window.scoretwo.get()+1)
   intscoretwo = window.scoretwo.get()
   print(intscoretwo)
   if intscoretwo % 6 == 1:
      p2win1.place(x=1415,y=880)
      im4 = "hi"
      im4 = PIL.Image.open(os.path.join(dirname, "scores\win 1.png"))
      im4 = im4.save(os.path.join(dirname, "P2Score.png"))
   if intscoretwo % 6 == 2:
      p2win2.place(x=1475,y=880)
      im4 = "hi"
      im4 = PIL.Image.open(os.path.join(dirname, "scores\win 2.png"))
      im4 = im4.save(os.path.join(dirname, "P2Score.png"))
   if intscoretwo % 6 == 3:
      p2win3.place(x=1535,y=880)
      im4 = "hi"
      im4 = PIL.Image.open(os.path.join(dirname, "scores\win 3.png"))
      im4 = im4.save(os.path.join(dirname, "P2Score.png"))
   if intscoretwo % 6 == 4:
      p2win4.place(x=1595,y=880)
      im4 = "hi"
      im4 = PIL.Image.open(os.path.join(dirname, "scores\win 4.png"))
      im4 = im4.save(os.path.join(dirname, "P2Score.png"))
   if intscoretwo % 6 == 5:
      p2win5.place(x=1655,y=880)
      im4 = "hi"
      im4 = PIL.Image.open(os.path.join(dirname, "scores\win 5.png"))
      im4 = im4.save(os.path.join(dirname, "P2Score.png"))
   if intscoretwo % 6 == 0:
      #p1win5.place(x=700,y=880)
      im4 = "hi"
      im4 = PIL.Image.open(os.path.join(dirname, "scores\win 0.png"))
      im4 = im4.save(os.path.join(dirname, "P2Score.png"))

def onClick2(event=None):
   window.scoreone.set(window.scoreone.get()+1)
   intscoreone = window.scoreone.get()
   print(intscoreone)
   if intscoreone % 6 == 1:
      p1win1.place(x=460,y=880)
      im3 = "hi"
      im3 = PIL.Image.open(os.path.join(dirname, "scores\win 1.png"))
      im3 = im3.save(os.path.join(dirname, "P1Score.png"))
   if intscoreone % 6 == 2:
      p1win2.place(x=520,y=880)
      im3 = "hi"
      im3 = PIL.Image.open(os.path.join(dirname, "scores\win 2.png"))
      im3 = im3.save(os.path.join(dirname, "P1Score.png"))
   if intscoreone % 6 == 3:
      p1win3.place(x=580,y=880)
      im3 = "hi"
      im3 = PIL.Image.open(os.path.join(dirname, "scores\win 3.png"))
      im3 = im3.save(os.path.join(dirname, "P1Score.png"))
   if intscoreone % 6 == 4:
      p1win4.place(x=640,y=880)
      im3 = "hi"
      im3 = PIL.Image.open(os.path.join(dirname, "scores\win 4.png"))
      im3 = im3.save(os.path.join(dirname, "P1Score.png"))
   if intscoreone % 6 == 5:
      p1win5.place(x=700,y=880)
      im3 = "hi"
      im3 = PIL.Image.open(os.path.join(dirname, "scores\win 5.png"))
      im3 = im3.save(os.path.join(dirname, "P1Score.png"))
   if intscoreone % 6 == 0:
      #p1win5.place(x=700,y=880)
      im3 = "hi"
      im3 = PIL.Image.open(os.path.join(dirname, "scores\win 0.png"))
      im3 = im3.save(os.path.join(dirname, "P1Score.png"))
#if intscoreone == 6:
    #  p1win1.destroy()
     # p1win2.destroy()
      #p1win3.destroy()
      #p1win4.destroy()
      #p1win5.destroy()
      #window.scoreone.set(window.scoreone.get()-6)
      
im3 = "hi"
im3 = PIL.Image.open(os.path.join(dirname, "scores\win 0.png"))
im3 = im3.save(os.path.join(dirname, "P1Score.png"))

im4 = "hi"
im4 = PIL.Image.open(os.path.join(dirname, "scores\win 0.png"))
im4 = im4.save(os.path.join(dirname, "P2Score.png"))   
setLabel1 = tkinter.Label(image= window.setLabel,borderwidth = 0)
setLabel1.place(x=100,y=860)
setLabel2 = tkinter.Label(image= window.setLabel,borderwidth = 0)
setLabel2.place(x=1055,y=860)
plusBtn1 = Button(window, image= window.Plus,bg='black', command= onClick2, width=50)
plusBtn1.place(x=800,y=880)
p1win0 = tkinter.Label(image= window.win0,bg='black')
p1win0.place(x=400,y=880)
plusBtn2 = Button(window, image= window.Plus, command= onClick3, width=50,bg='black')
plusBtn2.place(x=1755,y=880)
p2win0=tkinter.Label(image= window.win0,bg='black')
p2win0.place(x=1355,y=880)
p2null1=tkinter.Label(image= window.null1,bg='black')
p2null2=tkinter.Label(image= window.null2,bg='black')
p2null3=tkinter.Label(image= window.null3,bg='black')
p2null4=tkinter.Label(image= window.null4,bg='black')
p2null5=tkinter.Label(image= window.null5,bg='black')
p2null1.place(x=1415,y=880)
p2null2.place(x=1475,y=880)
p2null3.place(x=1535,y=880)
p2null4.place(x=1595,y=880)
p2null5.place(x=1655,y=880)
p2win1=tkinter.Label(image= window.win1,bg='black')
p2win2=tkinter.Label(image= window.win2,bg='black')
p2win3=tkinter.Label(image= window.win3,bg='black')
p2win4=tkinter.Label(image= window.win4,bg='black')
p2win5=tkinter.Label(image= window.win5,bg='black')
p1null1 = tkinter.Label(image= window.null1,bg='black')
p1null1.place(x=460,y=880)
p1null2 = tkinter.Label(image= window.null2,bg='black')
p1null2.place(x=520,y=880)
p1null3 = tkinter.Label(image= window.null3,bg='black')
p1null3.place(x=580,y=880)
p1null4 = tkinter.Label(image= window.null4,bg='black')
p1null4.place(x=640,y=880)
p1null5 = tkinter.Label(image= window.null5,bg='black')
p1null5.place(x=700,y=880)
p1win1 = tkinter.Label(image= window.win1,bg='black')
p1win2 = tkinter.Label(image= window.win2,bg='black')
p1win3 = tkinter.Label(image= window.win3,bg='black')
p1win4 = tkinter.Label(image= window.win4,bg='black')
p1win5 = tkinter.Label(image= window.win5,bg='black')


#tag labels
tagLabel1 = tkinter.Label(image= window.tagImg,borderwidth = 0)
tagLabel1.place(x=240, y=10)
Tag1 = StringVar(window)
Tag2 = StringVar(window)
enterTag1 = Entry(window, bd =5, textvariable=Tag1)
enterTag1.place(x=460, y=50)
tagLabel2 = tkinter.Label(image= window.tagImg,borderwidth = 0)
tagLabel2.place(x=1180,y=10)
enterTag2 = Entry(window, bd =5, textvariable=Tag2)
enterTag2.place(x=1400,y=50)
#confirm tag buttons
tagYes1 = Button(window, image = window.Yes,bg='black', command= lambda: p1SetTag(Tag1.get()), width= 50)
tagYes1.place(x=600,y = 35)
tagYes2 = Button(window, image = window.Yes,bg='black', command= lambda: p2SetTag(Tag2.get()), width= 50)
tagYes2.place(x=1540,y=35)
p1x1 = 120
p1x2 = 280
p1x3 = 440
p1x4 = 600
p1x5 = 760
p1x6 = 707
p1x7 = 547
p1x8 = 387
p1x9 = 227
p1x10 = 67
p2x1 = 1672
p2x2 = 1512
p2x3 = 1352
p2x4 = 1192
p2x5 = 1032
p2x6 = 1085
p2x7 = 1245
p2x8 = 1405
p2x9 = 1565
p2x10 = 1725
py1 = 160
py2 = 320
py3 = 480
py4 = 640

#Zim buttons
zim_btn1 = Button(window, image = window.Zim, bg='gray',command= lambda: p1CharChange(smolPicFiles,bigPicFiles[0]), width = 128)
zim_btn1.place(x=p1x6, y=py2)
zim_btn2 = Button(window, image = window.Zim,bg='gray', command= lambda: p2CharChange(smolPicFiles,bigPicFiles[0]), width = 128)
zim_btn2.place(x=p2x6, y=py2)

#Spongebob buttons
sponge_btn1 = Button(window, image = window.Spongebob,bg='gray', command= lambda: p1CharChange(smolPicFiles,bigPicFiles[1]), width = 128)
sponge_btn1.place(x = p1x1, y = py1)
sponge_btn2 = Button(window, image = window.Spongebob,bg='gray', command= lambda: p2CharChange(smolPicFiles,bigPicFiles[1]), width = 128)
sponge_btn2.place(x = p2x1, y = py1)

#Korra buttons
korra_btn1 = Button(window, image = window.Korra,bg='gray', command= lambda: p1CharChange(smolPicFiles,bigPicFiles[2]), width = 128)
korra_btn1.place(x=p1x9,y=py2)
korra_btn2 = Button(window, image = window.Korra,bg='gray', command= lambda: p2CharChange(smolPicFiles,bigPicFiles[2]), width = 128)
korra_btn2.place(x=p2x9,y=py2)

#CatDog buttons
catdog_btn1 = Button(window, image = window.CatDog,bg='gray', command= lambda: p1CharChange(smolPicFiles,bigPicFiles[3]),width = 128)
catdog_btn1.place(x=p1x8,y=py4)
catdog_btn2 = Button(window, image = window.CatDog,bg='gray', command= lambda: p2CharChange(smolPicFiles,bigPicFiles[3]),width = 128)
catdog_btn2.place(x=p2x8,y=py4)

#Toph buttons
toph_btn1 = Button(window, image = window.Toph,bg='gray', command= lambda: p1CharChange(smolPicFiles,bigPicFiles[4]),width = 128)
toph_btn1.place(x=p1x8,y=py2)
toph_btn2 = Button(window, image = window.Toph, bg='gray',command = lambda: p2CharChange(smolPicFiles,bigPicFiles[4]),width = 128)
toph_btn2.place(x=p2x8,y=py2)

#Sandy buttons
sandy_btn1 = Button(window, image = window.Sandy, bg='gray',command= lambda: p1CharChange(smolPicFiles,bigPicFiles[5]),width=128)
sandy_btn1.place(x = p1x3, y = py1)
sandy_btn2 = Button(window, image = window.Sandy, bg='gray',command= lambda: p2CharChange(smolPicFiles,bigPicFiles[5]),width=128)
sandy_btn2.place(x = p2x3, y = py1)

#RenStimpy buttons
ren_btn1 = Button(window, image = window.RenStimpy, bg='gray',command= lambda: p1CharChange(smolPicFiles,bigPicFiles[6]),width=128)
ren_btn1.place(x=p1x5,y=py3)
ren_btn2 = Button(window, image = window.RenStimpy, bg='gray',command= lambda: p2CharChange(smolPicFiles,bigPicFiles[6]),width=128)
ren_btn2.place(x=p2x5,y=py3)

#Lucy buttons
lucy_btn1 = Button(window,image=window.Lucy,bg='gray',command= lambda: p1CharChange(smolPicFiles,bigPicFiles[7]),width=128)
lucy_btn1.place(x=p1x5, y=py1)
lucy_btn2 = Button(window,image=window.Lucy,bg='gray',command= lambda: p2CharChange(smolPicFiles,bigPicFiles[7]),width=128)
lucy_btn2.place(x=p2x5, y=py1)

#PTM buttons
ptm_btn1 = Button(window, image=window.PTM,bg='gray',command= lambda: p1CharChange(smolPicFiles,bigPicFiles[8]),width=128)
ptm_btn1.place(x=p1x4,y=py3)
ptm_btn2 = Button(window, image=window.PTM,bg='gray',command= lambda: p2CharChange(smolPicFiles,bigPicFiles[8]),width=128)
ptm_btn2.place(x=p2x4,y=py3)

#Aang buttons
aang_btn1 = Button(window, image=window.Aang,bg='gray',command= lambda: p1CharChange(smolPicFiles,bigPicFiles[9]),width=128)
aang_btn1.place(x=p1x10,y=py2)
aang_btn2 = Button(window, image=window.Aang,bg='gray',command= lambda: p2CharChange(smolPicFiles,bigPicFiles[9]),width=128)
aang_btn2.place(x=p2x10,y=py2)

#Reptar buttons
rep_btn1 = Button(window, image=window.Reptar,bg='gray',command= lambda: p1CharChange(smolPicFiles,bigPicFiles[10]),width=128)
rep_btn1.place(x = p1x10, y = py4)
rep_btn2 = Button(window, image=window.Reptar,bg='gray',command= lambda: p2CharChange(smolPicFiles,bigPicFiles[10]),width=128)
rep_btn2.place(x = p2x10, y = py4)

#Leonardo buttons
leo_btn1 = Button(window, image=window.Leonardo,bg='gray',command= lambda: p1CharChange(smolPicFiles,bigPicFiles[11]),width=128)
leo_btn1.place(x=p1x1,y=py3)
leo_btn2 = Button(window, image=window.Leonardo,bg='gray',command= lambda: p2CharChange(smolPicFiles,bigPicFiles[11]),width=128)
leo_btn2.place(x=p2x1,y=py3)

#Nigel buttons
bry_btn1 = Button(window, image=window.Nigel,bg='gray',command= lambda: p1CharChange(smolPicFiles,bigPicFiles[12]),width=128)
bry_btn1.place(x=p1x6,y=py4)
bry_btn2 = Button(window, image=window.Nigel,bg='gray',command= lambda: p2CharChange(smolPicFiles,bigPicFiles[12]),width=128)
bry_btn2.place(x=p2x6,y=py4)

#Michaelangelo buttons
mike_btn1 = Button(window, image=window.Michaelangelo,bg='gray',command= lambda: p1CharChange(smolPicFiles,bigPicFiles[13]),width=128)
mike_btn1.place(x=p1x2,y=py3)
mike_btn2 = Button(window, image=window.Michaelangelo,bg='gray',command= lambda: p2CharChange(smolPicFiles,bigPicFiles[13]),width=128)
mike_btn2.place(x=p2x2,y=py3)

#Danny buttons
dan_btn1 = Button(window, image=window.Danny,bg='gray',command= lambda: p1CharChange(smolPicFiles,bigPicFiles[14]),width=128)
dan_btn1.place(x=p1x7, y=py2)
dan_btn2 = Button(window, image=window.Danny,bg='gray',command= lambda: p2CharChange(smolPicFiles,bigPicFiles[14]),width=128)
dan_btn2.place(x=p2x7, y=py2)

#Lincoln buttons
link_btn1 = Button(window, image=window.Lincoln,bg='gray',command= lambda: p1CharChange(smolPicFiles,bigPicFiles[15]),width=128)
link_btn1.place(x = p1x4, y = py1)
link_btn2 = Button(window, image=window.Lincoln,bg='gray',command= lambda: p2CharChange(smolPicFiles,bigPicFiles[15]),width=128)
link_btn2.place(x = p2x4, y = py1)

#April buttons
april_btn1 = Button(window, image=window.April,bg='gray',command= lambda: p1CharChange(smolPicFiles,bigPicFiles[16]),width=128)
april_btn1.place(x=p1x3,y=py3)
april_btn2 = Button(window, image=window.April,bg='gray',command= lambda: p2CharChange(smolPicFiles,bigPicFiles[16]),width=128)
april_btn2.place(x=p2x3,y=py3)

#Helga buttons
helga_btn1 = Button(window, image=window.Helga,bg='gray',command= lambda: p1CharChange(smolPicFiles,bigPicFiles[17]),width=128)
helga_btn1.place(x=p1x7,y=py4)
helga_btn2 = Button(window, image=window.Helga,bg='gray',command= lambda: p2CharChange(smolPicFiles,bigPicFiles[17]),width=128)
helga_btn2.place(x=p2x7,y=py4)

#Oblina buttons
oblina_btn1 = Button(window, image=window.Oblina,bg='gray',command= lambda: p1CharChange(smolPicFiles,bigPicFiles[18]),width=128)
oblina_btn1.place(x=p1x9,y=py4)
oblina_btn2 = Button(window, image=window.Oblina,bg='gray',command= lambda: p2CharChange(smolPicFiles,bigPicFiles[18]),width=128)
oblina_btn2.place(x=p2x9,y=py4)

#Patrick buttons
pat_btn1 = Button(window, image=window.Patrick,bg='gray',command= lambda: p1CharChange(smolPicFiles,bigPicFiles[19]),width=128)
pat_btn1.place(x=p1x2,y=py1)
pat_btn2 = Button(window, image=window.Patrick,bg='gray',command= lambda: p2CharChange(smolPicFiles,bigPicFiles[19]),width=128)
pat_btn2.place(x=p2x2,y=py1)

window.mainloop()

