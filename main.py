from tkinter import *
from tkinter.filedialog import *
from tkinter import font
from tkinter.colorchooser import *
from tkinter.messagebox import *

app = Tk()
app.title("NotePady")

def save():
    file = asksaveasfile(mode="w", defaultextension=".txt", filetypes=[
        ("All Files", "*.*"),
        ("Text Files", "*.txt")
    ], initialfile="untitled")
    app.title(f"NotePady - {file.name}")
    file.write(text.get(1.0, END))

def openfile():
    file = askopenfile(mode="r", defaultextension=".txt", filetypes=[
        ("Text Files", "*.txt"),
        ("All Files", "*.*")
    ])
    text.delete(1.0, END)
    text.insert(1.0, file.read())
    app.title(f"NotePady - {file.name}")
    
def new():
    app.title("NotePady untitled")
    text.delete(1.0, END)

def copytext():
    text.event_generate("<<Copy>>")

def cut():
    text.event_generate("<<Cut>>")

def paste():
    text.event_generate("<<Paste>>")

def font_change(*args):
    text.config(font=(Font_name.get(), font_size.get()))

def color_change():
    colorr = askcolor()
    text.config(fg=colorr[1])

def undot():
    text.edit_undo()

def redot():
    text.edit_redo()

Font_name = StringVar()
Font_name.set("Arial")
font_size = StringVar()
font_size.set("25")

frame = Frame(app)
logo = Label(frame).grid(row=0, column=0)
fontsoption = OptionMenu(frame, Font_name, *font.families(), command=font_change)
fontsoption.grid(row=0, column=1)
font_size_op = Spinbox(frame, textvariable=font_size, command=font_change, from_=1, to=100)
font_size_op.grid(row=0, column=2)
color = Button(frame, command=color_change, text="Color").grid(row=0, column=3)
frame.pack()

menubar = Menu(app)
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu, font=23)
file_menu.add_command(label="Save", command=save)
file_menu.add_command(label="Open", command=openfile)
file_menu.add_command(label="New", command=new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu, font=23)
edit_menu.add_command(label="Copy", command=copytext)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=undot)
edit_menu.add_command(label="Redo", command=redot)

help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu, font=23)
help_menu.add_command(label="About", command=lambda: showinfo("About", "NotePady: A program made by Mahdi Ali, the youngest multi-language developer in the world."))
help_menu.add_separator()
help_menu.add_command(label="How", command=lambda: showinfo("How to Use", "In NotePady, you can type text, format it, save files, open files, create new files, and more!"))

# Format Menu
format_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Format", menu=format_menu, font=23)

def toggle_bold():
    if text.tag_ranges("sel"):
        current_tags = text.tag_names("sel.first")
        if 'bold' in current_tags:
            text.tag_remove('bold', "sel.first", "sel.last")
        else:
            text.tag_add('bold', "sel.first", "sel.last")
        text.tag_config('bold', font=(Font_name.get(), font_size.get(), "bold"))

def toggle_italic():
    if text.tag_ranges("sel"):
        current_tags = text.tag_names("sel.first")
        if 'italic' in current_tags:
            text.tag_remove('italic', "sel.first", "sel.last")
        else:
            text.tag_add('italic', "sel.first", "sel.last")
        text.tag_config('italic', font=(Font_name.get(), font_size.get(), "italic"))

def toggle_underline():
    if text.tag_ranges("sel"):
        current_tags = text.tag_names("sel.first")
        if 'underline' in current_tags:
            text.tag_remove('underline', "sel.first", "sel.last")
        else:
            text.tag_add('underline', "sel.first", "sel.last")
        text.tag_config('underline', font=(Font_name.get(), font_size.get(), "underline"))

format_menu.add_command(label="Bold", command=toggle_bold)
format_menu.add_command(label="Italic", command=toggle_italic)
format_menu.add_command(label="Underline", command=toggle_underline)

app.config(menu=menubar)

text = Text(app, font=(Font_name.get(), font_size.get()), undo=True)
scorll = Scrollbar(app)
text.config(yscrollcommand=scorll.set)
text.pack()
scorll.pack()

Label1 = Label(frame, text="0 Words", font=("Comic Sans MS", 10))
Label1.grid(row=1, column=0)
Label2 = Label(frame, text="0 Chars", font=("Comic Sans MS", 10))
Label2.grid(row=1, column=1)

def count():
    words = len(text.get(1.0, END).split(" "))
    Label1.config(text=f"{words} Words")
    Label2.config(text=f"{len(text.get(1.0, END))} Chars")
    app.after(1, count)

count()

app.mainloop()
