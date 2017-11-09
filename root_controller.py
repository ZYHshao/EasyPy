# -*- coding: UTF-8 -*-
from Tkinter import *
import tkFont
import os
from tkFileDialog import *


root = Tk()
fileName = ""
##########function###############

def openFile():
    global fileName
    fileName = askopenfilename(defaultextension='.py')
    if fileName == "":
        fileName = None
    else:
        containerText.delete(1.0,END)
        f=open(fileName,'r')
        containerText.insert(1.0,f.read())
        f.close()
        allText = containerText.get(0.0, END)
        containerTextLineCount = 1
        for i in range(len(allText)):
            if allText[i] == '\n':
                containerTextLineCount = containerTextLineCount + 1
        lineText.config(state=NORMAL)
        lineText.delete(0.0, 'end');
        for i in range(containerTextLineCount):
            if i != 0:
                lineText.insert(END, '\n')
            lineText.insert(END, i + 1)
        lineText.config(state=DISABLED)
        lineText.yview('moveto', currentOffset)

def newFile():
    global fileName
    fileName = None
    containerText.delete(1.0,END)
    lineText.config(state=NORMAL)
    lineText.delete(2.0,END)
    lineText.config(state=DISABLED)

def save():
    global fileName
    if fileName != None :
        fh = open(fileName, 'w')
        msg = containerText.get(1.0, END)
        fh.write(msg)
        fh.close()
    else:
        saveas()

def saveas():
    global fileName
    f = asksaveasfilename(initialfile='未命名.py',defaultextension='.py')
    if f != None :
        fileName = f
        fh = open(f,'w')
        msg = containerText.get(1.0,END)
        fh.write(msg)
        fh.close()

##########function##############




###########----UI----##################

root.title("EasyPy——简洁易用的Python编辑器")
root.geometry("1000x600+200+100")
menu = Menu(root)
root.config(menu=menu)

#menu
filemenu = Menu(menu)
menu.add_cascade(label='文件',menu=filemenu)
filemenu.add_command(label='新建',command=newFile)
filemenu.add_separator()
filemenu.add_command(label='打开',command=openFile)

subFileMenuOfOpen = Menu()
subFileMenuOfOpen.add_command(label='清空历史记录')
filemenu.add_cascade(menu=subFileMenuOfOpen,label='最新打开')

filemenu.add_separator()
filemenu.add_command(label='保存',command=save)
filemenu.add_command(label='另存为',command=saveas)

editmenu = Menu(menu)
menu.add_cascade(label='编辑',menu=editmenu)
editmenu.add_command(label='撤销')


#toolbar
toolbar = Frame(master=root,height=30,bg='#e7e7e7')
toolbar.propagate(False)
line = Frame(master=toolbar,height=1,bg='#c3c3c3')
line.pack(side=BOTTOM,fill=X)
toolbar.pack(side=TOP,fill=X)



#status bar
statusbar = Frame(master=root,height=20,bg='#e7e7e7')
statusbar.pack(side=BOTTOM,fill=X)
statusbar.propagate(False)
line = Frame(master=statusbar,height=1,bg='#c3c3c3')
line.pack(side=TOP,fill=X)

#pack
packView = Text(master=root,height=10,highlightbackground='white',highlightcolor='white',bg='#ececec',font=tkFont.Font(size=14))
packView.pack(side=BOTTOM,fill=X)
packView.propagate(False)
packView.insert(1.0,'Console...')
packView.config(state=DISABLED)
line = Frame(master=packView,height=1,bg='#c3c3c3')
line.pack(side=TOP,fill=X)

#text container
lineText = Text(width=3,bg='#ececec',highlightbackground='#ececec',font=tkFont.Font(size=19))
lineText.pack(side=LEFT,fill=Y)
lineText.insert(1.0,"1")
lineText.config(state=DISABLED)

containerText = Text(bg='white',highlightbackground='white',highlightcolor='white',tabs='0.7c',font=tkFont.Font(size=19))
containerText.pack(fill=BOTH,expand=YES)

containerTextLineCount = 0


def scrollDidScroll(a1,a2):
    containerText.yview(a1,a2)
    lineText.yview(a1, a2)
currentOffset = 0
def containerTextScrill(a1,a2):
    global currentOffset
    currentOffset = a1
    lineText.yview('moveto',a1)
def lineTextScrill(a1,a2):
    containerText.yview('moveto', a1)


containerText.config(yscrollcommand=containerTextScrill)
def inputCommand(event):
    allText = containerText.get(0.0,END)
    containerTextLineCount = 1
    for i in range(len(allText)):
        if allText[i] == '\n':
            containerTextLineCount = containerTextLineCount+1
    lineText.config(state=NORMAL)
    lineText.delete(0.0,'end')
    for i in range(containerTextLineCount):
        if i!=0:
            lineText.insert(END, '\n')
        lineText.insert(END,i+1)
    lineText.config(state=DISABLED)
    lineText.yview('moveto',currentOffset)
def deleteCommand(event):
    allText = containerText.get(0.0,END)
    containerTextLineCount = 1
    for i in range(len(allText)):
        if allText[i] == '\n':
            if i==len(allText)-1:
                containerTextLineCount = containerTextLineCount
            else:
                containerTextLineCount = containerTextLineCount+1
    lineText.config(state=NORMAL)
    lineText.delete(0.0,'end')
    for i in range(containerTextLineCount):
        if i!=0:
            lineText.insert(END, '\n')
        lineText.insert(END,i+1)
    lineText.config(state=DISABLED)
    lineText.yview('moveto', currentOffset)

containerText.bind('<Key-Return>',inputCommand)
containerText.bind("<Key-BackSpace>",deleteCommand)
lineText.config(yscrollcommand=lineTextScrill)

###########----UI----##################



root.mainloop()