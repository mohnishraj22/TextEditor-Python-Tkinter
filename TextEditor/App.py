#--------------------------Creating Text Editor Using Tkinter---------------------------------------------

from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import font
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import colorchooser
from tkinter import messagebox
import os


global text

#To opening new blank file
def newfile():
    text_area.delete(1.0,END)
    root.title("New File - Text Editor")
    status_bar.config(text="New File     ")

#To open existing file from system 
def openfile():
    text_area.delete(1.0,END)
    text_file=filedialog.askopenfilename(title="Open File",filetypes=(("Text Files","*.txt"),("HTML Files","*.html"),("Python Files","*.py"),("All Files","*.*")))
    if text_file:
        l=text_file.split('/')   
        name=l[len(l)-1]
        root.title(name+" - Text Editor")
        status_bar.config(text=name+"     ")
        text_file=open(text_file,'r')
        text=text_file.read()
        text_area.insert(END,text)
        text_file.close()

#To save as current file 
def save_as():
    text_file=filedialog.asksaveasfilename(defaultextension=".*",title="Save As",filetypes=(("Text Files","*.txt"),("HTML Files","*.html"),("Python Files","*.py"),("All Files","*.*")))
    if text_file:
        l=text_file.split('/')   
        name=l[len(l)-1]
        root.title(name+" - Text Editor")
        status_bar.config(text=name+"     ")
        text_file=open(text_file,'w')
        text=text_file.write(text_area.get(1.0,END))
        text_file.close()

#TO save current file   
def save():
    text_file=filedialog.asksaveasfilename(initialfile="Newfile.txt",defaultextension=".*",title="Save",filetypes=(("Text Files","*.txt"),("HTML Files","*.html"),("Python Files","*.py"),("All Files","*.*")))
    if text_file:
        l=text_file.split('/')   
        name=l[len(l)-1]
        root.title(name+" - Text Editor")
        status_bar.config(text="Saved : "+name+"     ")
        text_file=open(text_file,'w')
        text=text_file.write(text_area.get(1.0,END))
        text_file.close()

#to Close window
def close():
    response=messagebox.askquestion('Save On Close','Do you want to save file ')
    if response=='yes':
        save()
    else:
        root.destroy()
#To count the words and lines in a file    
def count(event):
    text=text_area.get(1.0,END)
    l=text.split()
    var=list(text_area.get(1.0,"end-1c"))
    line=var.count('\n')
    label=Label(status_bar,text="  Words : "+str(len(l))+"     Lines : "+str(1+line)+"     ")
    label.place(x=1000,y=0)

#To uppercase all text in a file
def uppercase():
    text=text_area.get(1.0,END)
    l=text.upper()
    text_area.delete(1.0,END)
    text_area.insert(END,l)

#To lowercase all text in a file
def lowercase():
    text=text_area.get(1.0,END)
    l=text.lower()
    text_area.delete(1.0,END)
    text_area.insert(END,l)

#To capitalize all text in a file 
def capitalcase():
    text=text_area.get(1.0,END)
    text_area.delete(1.0,END)
    l=list(text)
    pre=' '
    for i in text:
        if pre==' ' or pre=='\n':
            text_area.insert(END,i.capitalize())
            pre=i
        else:
            pre=i
            text_area.insert(END,i)

#To togglecase all text in a file
def togglecase():
    text=text_area.get(1.0,END)
    text_area.delete(1.0,END)
    l=list(text)
    pre=' '
    for i in text:
        if pre==' ' or pre=='\n':
            text_area.insert(END,i.lower())
            pre=i
        else:
            pre=i
            text_area.insert(END,i.capitalize())

#To search text in file
def search_text(e):
            text_area.tag_remove('found',1.0,END)
            s=search.get()
            if s:
                idx=1.0
                while 1:
                    idx=text_area.search(s,idx,nocase=1,stopindex=END)
                    if not idx:
                        break
                    lastidx='%s+%dc' % (idx,len(s))
                    text_area.tag_add('found',idx,lastidx)
                    idx=lastidx

                text_area.tag_config('found',foreground='red',background='yellow')

       
#function to create find replace words window                
def find_replace_window(text_edit):
    #to find text in a file 
    def find_text():
        text_area.tag_remove('found',1.0,END)
        s=e.get()
        if s:
            idx=1.0
            while 1:
                idx=text_area.search(s,idx,nocase=1,stopindex=END)
                if not idx:
                    break
                lastidx='%s+%dc' % (idx,len(s))
                text_area.tag_add('found',idx,lastidx)
                idx=lastidx

            text_area.tag_config('found',foreground='red',background='yellow')
        window.destroy()
        
    # To replace text in a file   
    def replaceall():
        s=e.get()
        if s:
            idx=1.0
            while 1:
                idx=text_area.search(s,idx,END)
                if not idx:
                    break
                lastidx='%s+%dc' % (idx,len(s))
                text_area.delete(idx,lastidx)
                text_area.insert(idx,e1.get())
                idx=lastidx
        window.destroy()

        
    window=Toplevel()
    window.title(text_edit)
    window.geometry("400x150")
    window.resizable(False,False)
    
            
    if text_edit=='Find':
        label=Label(window,text="Find what :")
        label.place(x=25,y=50)
        e=Entry(window,width=40)
        e.place(x=100,y=50)
        button=Button(window,text='   Find    ',command=find_text)
        button.place(x=150,y=100)
    else:
        label=Label(window,text="Find what      :")
        label.place(x=25,y=30)
        e=Entry(window,width=40)
        e.place(x=110,y=30)
        label_1=Label(window,text="Replace with :")
        label_1.place(x=25,y=80)
        e1=Entry(window,width=40)
        e1.place(x=110,y=80)
        button=Button(window,text='Replace',command=replaceall)
        button.place(x=150,y=115)
    
#To copy a select text of a file
def copy():
    try:
        global text
        if text_area.selection_get():    
            text=text_area.selection_get()
            root.clipboard_clear()
            root.clipboard_append(text)
    except:
        pass

#To cut a select text of a file
def cut():
    try:
        global text
        if text_area.selection_get():    
            text=text_area.selection_get()
            text_area.delete("sel.first","sel.last")
            root.clipboard_clear()
            root.clipboard_append(text)
    except:
        pass
#To paste text in a file    
def paste():
    try:
        global text
        text=root.clipboard_get()
        if text:
            position=text_area.index(INSERT)
            text_area.insert(position,text)
    except:
        pass
  
#to change font style like :- italic,bold,underline,overstrike
def font_style(style):
    try:
        bold_status='normal'
        italic_status='roman'
        underline_status=0
        overstrike_status=0
        
        if style=='bold':
            bold_status='bold'
        if style=='italic':
            italic_status='italic'
        if style=='underline':
            underline_status=1
        if style=='overstrike':
            overstrike_status=1
        
        current_tags=text_area.tag_names("sel.first")
        
        for i in current_tags:
            if i=='bold':
                bold_status='bold'
            if i=='italic':
                italic_status='italic'
            if i=='underline':
                underline_status=1
            if i=='overstrike':
                overstrike_status=1
        
        bold_font=font.Font(text_area,text_area.cget("font"))

        bold_font.configure(weight=bold_status,slant=italic_status,underline=underline_status,overstrike=overstrike_status)
        
        text_area.tag_configure(style,font=bold_font)
        if style in current_tags:
            text_area.tag_remove(style,"sel.first","sel.last")
        else:
            text_area.tag_add(style,"sel.first","sel.last")
    except(TclError):
        pass
    
    
# To change text colour of selected text
def text_colour():
    global fg_colour
    my_colour=colorchooser.askcolor()[1]
    
    if my_colour:
        
        colour_font=font.Font(text_area,text_area.cget("font"))
        
        text_area.tag_configure("colored",font=colour_font,foreground=my_colour)
        
        current_tags=text_area.tag_names("sel.first")
        
        text_area.tag_add("colored","sel.first","sel.last")
        colour_text_button.config(fg=my_colour)

#To align whole text of file in center,left,right       
def alignment(val):
    current_tags=text_area.tag_names("1.0")
    text_area.tag_configure(val,justify=val)
    tag=['left','right','center']
    for i in current_tags:
        for j in tag:
            if i==j:
                text_area.tag_remove(i,1.0,"end")
        
    text_area.tag_add(val,1.0,"end")

#To change font style(family)
def font_name_(e):
    our_font.config(family=font_family.get())

#To change font size
def font_size_(e):
    our_font.config(size=font_size.get())

#To change soacing between to lines
def spacing(value):
    text_area.config(spacing1=value)
    text_area.config(spacing2=value)
    text_area.config(spacing3=value)

#---------------------------Creating A Window-----------------------
    
root=Tk()
root.title("TEXT EDITOR")
root.geometry("1500x750+0+0")
root.resizable(False,False)
icon=PhotoImage(file='images\icon.png')      #putting icon in window
root.iconphoto(False,icon)

#-----------------------Ribbon Frame---------------------------

ribbon=Frame(root,bd=2,height=90,relief=RIDGE)
ribbon.pack(fill=X,side=TOP,padx=70)


#-----------------------Text Area----------------------------------

our_font=font.Font(family="Calibari",size="11")
text_area=scrolledtext.ScrolledText(root,wrap=WORD,undo=True,font=our_font)
text_area.pack(fill=X,padx=130,pady=20)
text_area.config(spacing1=3)
text_area.config(spacing2=3)
text_area.config(spacing3=3)

#------------------------Creating Main Menu --------------------------
my_menu=Menu(root)
root.config(menu=my_menu)

#-----------------------Creating File Menu----------------------------
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="     File",menu=file_menu)

#----------------------Sub File Menu---------------------------------
file_menu.add_command(label="New              Ctrl+N",command=newfile)
file_menu.add_command(label="Open            Ctrl+O",command=openfile)
file_menu.add_command(label="Save              Ctrl+S",command=save)
file_menu.add_command(label="Save As         Ctrl+Shift+S",command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit                Alt+F4",command=close)

#-----------------------Creating Edit Menu-----------------------------
edit_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="  Edit ",menu=edit_menu)

#-----------------------Sub Edit Menu--------------------------------
edit_menu.add_command(label="Copy      Ctrl+C",command=copy)
edit_menu.add_command(label="Cut         Ctrl+X",command=cut)
edit_menu.add_command(label="Paste      Ctrl+V",command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Undo      Ctrl+Z",command=text_area.edit_undo)
edit_menu.add_command(label="Redo      Ctrl+Y",command=text_area.edit_redo)



#-------------------Resize Icon/Button Images -------------------------

undo_text_image=Image.open('images/undo_text.png')
undo_text=undo_text_image.resize((20,20))
undo_text_icon=ImageTk.PhotoImage(undo_text)

redo_text_image=Image.open('images/redo_text.png')
redo_text=redo_text_image.resize((20,20))
redo_text_icon=ImageTk.PhotoImage(redo_text)

copy_text_image=Image.open('images/copy_text.png')
copy_text=copy_text_image.resize((20,20))
copy_text_icon=ImageTk.PhotoImage(copy_text)

cut_text_image=Image.open('images/cut_text.png')
cut_text=cut_text_image.resize((20,20))
cut_text_icon=ImageTk.PhotoImage(cut_text)

paste_text_image=Image.open('images/paste_text.png')
paste_text=paste_text_image.resize((40,40))
paste_text_icon=ImageTk.PhotoImage(paste_text)

center_align_image=Image.open('images/center_align.png')
center_image=center_align_image.resize((30,30))
center_align_icon=ImageTk.PhotoImage(center_image)

left_align_image=Image.open('images/left_align.png')
left_image=left_align_image.resize((30,30))
left_align_icon=ImageTk.PhotoImage(left_image)

right_align_image=Image.open('images/right_align.png')
right_image=right_align_image.resize((30,30))
right_align_icon=ImageTk.PhotoImage(right_image)

bold_text_image=Image.open('images/bold_text.png')
bold_text=bold_text_image.resize((20,20))
bold_text_icon=ImageTk.PhotoImage(bold_text)

italic_text_image=Image.open('images/italic_text.png')
italic_text=italic_text_image.resize((20,20))
italic_text_icon=ImageTk.PhotoImage(italic_text)

underline_text_image=Image.open('images/underline_text.png')
underline_text=underline_text_image.resize((20,20))
underline_text_icon=ImageTk.PhotoImage(underline_text)

strikethrough_text_image=Image.open('images/strikethrough_text.png')
strikethrough_text=strikethrough_text_image.resize((20,20))
strikethrough_text_icon=ImageTk.PhotoImage(strikethrough_text)

separator_image=Image.open('images/separator.png')
separator=separator_image.resize((10,80))
separator_icon=ImageTk.PhotoImage(separator)

search_text_image=Image.open('images/search_text.png')
search_text_=search_text_image.resize((20,20))
search_text_icon=ImageTk.PhotoImage(search_text_)

#----------------------------Undo/Redo Section-------------------------------------

undo_redo_label=Label(ribbon,text="Undo/Redo")
undo_redo_label.grid(row=2,column=0)

undo_text_button=Button(ribbon,image=undo_text_icon,bd=0,command=text_area.edit_undo)
undo_text_button.grid(row=0,column=0,ipadx=30,pady=5)

redo_text_button=Button(ribbon,image=redo_text_icon,bd=0,command=text_area.edit_redo)
redo_text_button.grid(row=1,column=0,ipadx=30,pady=2)

separatorlabel=Label(ribbon,image=separator_icon)
separatorlabel.grid(row=0,column=2,rowspan=3)

#------------------------------Clipboard Command Section--------------------------------

clipboard=Label(ribbon,text="Clipboard")
clipboard.grid(row=2,column=3,columnspan=3)

paste_text_button=Button(ribbon,image=paste_text_icon,bd=0,command=paste)
paste_text_button.grid(row=0,column=3,rowspan=2,columnspan=2,padx=10)

copy_text_button=Button(ribbon,image=copy_text_icon,bd=0,command=copy)
copy_text_button.grid(row=0,column=5)

cut_text_button=Button(ribbon,image=cut_text_icon,bd=0,command=cut,anchor=NW)
cut_text_button.grid(row=1,column=5)

separatorlabel_1=Label(ribbon,image=separator_icon)
separatorlabel_1.grid(row=0,column=8,rowspan=3)

#---------------------------------Text Style Section--------------------------------------

#******************************** Combobox Font Family/Size *************************************
font_name=StringVar()
font_family=ttk.Combobox(ribbon,value=list(font.families()),width=15,textvariable=font_name,state='readonly')
font_family.grid(row=0,column=9,columnspan=4,padx=10)
font_family.current(32)


size=[8,9,10,11,12,14,16,18,20,22,24,26,28,34,36,48,72]
font_size=ttk.Combobox(ribbon,value=size,width=5,state='readonly')
font_size.current(3)
font_size.grid(row=0,column=13)

#***************************************************************************************************

fontlabel=Label(ribbon,text="Font")
fontlabel.grid(row=2,column=9,columnspan=6)

bold_text_button=Button(ribbon,image=bold_text_icon,bd=0,command=lambda:font_style("bold"))
bold_text_button.grid(row=1,column=9)

italic_text_button=Button(ribbon,image=italic_text_icon,bd=0,command=lambda:font_style("italic"))
italic_text_button.grid(row=1,column=10)

underline_text_button=Button(ribbon,image=underline_text_icon,bd=0,command=lambda:font_style("underline"))
underline_text_button.grid(row=1,column=11)

strikethrough_text_button=Button(ribbon,image=strikethrough_text_icon,bd=0,command=lambda:font_style("overstrike"))
strikethrough_text_button.grid(row=1,column=12)

colour_text_button=Button(ribbon,text='AA',font=(20),bd=0,command=text_colour)
colour_text_button.grid(row=1,column=13)

separatorlabel_2=Label(ribbon,image=separator_icon)
separatorlabel_2.grid(row=0,column=14,rowspan=3)

#---------------------------------Text Alignment Section----------------------------------

para=Label(ribbon,text="Paragraph")
para.grid(row=2,column=15,columnspan=3)

center_align_button=Button(ribbon,image=center_align_icon,bd=0,command=lambda: alignment("center"))
center_align_button.grid(row=0,column=15,rowspan=2,padx=5)

left_align_button=Button(ribbon,image=left_align_icon,bd=0,command=lambda: alignment("left"))
left_align_button.grid(row=0,column=16,rowspan=2,padx=5)

right_align_button=Button(ribbon,image=right_align_icon,bd=0,command=lambda: alignment("right"))
right_align_button.grid(row=0,column=17,rowspan=2,padx=5)


separatorlabel_3=Label(ribbon,image=separator_icon)
separatorlabel_3.grid(row=0,column=18,rowspan=3)

#---------------------------------Spacing Section-------------------------------------------------

spacing_label=Label(ribbon,text="Spacing")
spacing_label.grid(row=2,column=19,columnspan=3)


normal_space_button=Button(ribbon,text="Normal",bd=2,relief=SUNKEN,width=15,height=3,command=lambda: spacing(3))
normal_space_button.grid(row=0,column=19,padx=5,pady=10,rowspan=2)

no_space_button=Button(ribbon,text="No Space",bd=2,relief=SUNKEN,width=15,height=3,command=lambda: spacing(0))
no_space_button.grid(row=0,column=20,padx=5,pady=10,rowspan=2)

separatorlabel_4=Label(ribbon,image=separator_icon)
separatorlabel_4.grid(row=0,column=21,rowspan=3)

#------------------------------------Text Case Section-------------------------------

textcase=Label(ribbon,text="Text case")
textcase.grid(row=2,column=22,columnspan=3)

uppercase_button=Button(ribbon,text=" UPPER CASE ",bd=2,relief=GROOVE,command=uppercase)
uppercase_button.grid(row=0,column=22,padx=5,pady=10)

lowercase_button=Button(ribbon,text="   lower case   ",bd=2,relief=GROOVE,command=lowercase)
lowercase_button.grid(row=1,column=22,padx=5)

capitalize_button=Button(ribbon,text="Capitalize Each Word",relief=GROOVE,bd=2,command=capitalcase)
capitalize_button.grid(row=0,column=23,padx=5)

togglecase_button=Button(ribbon,text="       tOGGLE cASE       ",relief=GROOVE,bd=2,command=togglecase)
togglecase_button.grid(row=1,column=23,padx=5)

separatorlabel_5=Label(ribbon,image=separator_icon)
separatorlabel_5.grid(row=0,column=24,rowspan=3)

#-----------------------------------Edit Section -----------------------------------

editing=Label(ribbon,text="Editing")
editing.grid(row=2,column=25,columnspan=3)

find_text_button=Button(ribbon,text="      Find       ",relief=GROOVE,bd=2,command=lambda: find_replace_window('Find'))
find_text_button.grid(row=0,column=25,padx=5,columnspan=2)


replace_all_text_button=Button(ribbon,text="    Replace     ",relief=GROOVE,bd=2,command=lambda: find_replace_window('Replace '))
replace_all_text_button.grid(row=1,column=25,padx=5,columnspan=2)

separatorlabel_5=Label(ribbon,image=separator_icon)
separatorlabel_5.grid(row=0,column=27,rowspan=3)

#------------------------------------Search Section------------------------------------------

searchlabel=Label(ribbon,text="Search")
searchlabel.grid(row=2,column=30,columnspan=3)

search=Entry(ribbon)
search.grid(padx=15,row=0,column=30,rowspan=3)

search_text_button=Button(ribbon,text="          search",image=search_text_icon,bd=0,command=search_text)
search_text_button.grid(row=0,column=31,rowspan=3)

#-------------------------------------key binding-------------------------------------------

font_family.bind("<<ComboboxSelected>>",font_name_)
font_size.bind("<<ComboboxSelected>>",font_size_)
root.bind('<Control-Key-n>',newfile)
root.bind('<Control-Key-o>',openfile)
root.bind('<Control-Key-s>',save)
root.bind('<Control-Shift-s>',save_as)
root.bind('<Alt-F4>',close)
root.bind('<Control-Key-c>',copy)
root.bind('<Control-Key-v>',paste)
text_area.bind('<space>',count)
text_area.bind('<BackSpace>',count)
search.bind('<Return>',search_text)
search.bind('<space>',search_text)

#----------------------------------- Status Bar ----------------------------------------------

status_bar=Label(root,text="Ready                  ",width=215,anchor=E)
status_bar.place(x=0,y=708)
root.mainloop()
