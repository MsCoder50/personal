from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
from tkinter import messagebox

root = Tk()
#root.iconbitmap('Mscode.ico')
root.title('Mscode')
file_path = ''
root.geometry("1000x1000")
def close():
    msg= messagebox.askyesno("Mscode", "Do you want to save your file?")
    # print(msg)
    if msg == True:
        save_as()
        exit()
    elif msg == False:
        exit()
    else:
        pass

def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def run():
    if file_path == '':
        messagebox.showinfo("Mscode", "Please Save your file first")
        save_as()
        return
    save_as()
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0',output)
    code_output.insert('1.0',  error)

editor_frame= Frame(width=170,height=33)
output_frame= Frame(width=170,height=12)

editor_frame.pack()
output_frame.pack()

menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=close)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

root.config(menu=menu_bar)
editor_scroll = Scrollbar(editor_frame,orient='vertical')
editor_scroll.pack(side=RIGHT,fill='y')
editor = Text(editor_frame,width=170,height=33,yscrollcommand=editor_scroll.set)
editor.pack()


output_scroll = Scrollbar(output_frame,orient='vertical')
output_scroll.pack(side=RIGHT,fill='y')
code_output = Text(output_frame,height=12, width=170,yscrollcommand=output_scroll.set)
code_output.pack()

editor_scroll.config(command=editor.yview)
output_scroll.config(command=code_output.yview)

root.mainloop()


