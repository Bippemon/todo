import tkinter as tk
from tkinter import ttk
import todo_manager
import os
from PIL import Image, ImageTk

# standardvärden för fönsterstorlek
W_HEIGHT = 400
W_WIDTH = 300

def run_gui():
    # laddar in data från fil
    todos = todo_manager.load_todos()

    def change_bg_color():
        # background
        root.config(bg="gray25")
        style.configure("TFrame", background="gray25")
        
        # buttons
        style.configure("TButton", background="dimgray", foreground="black")
        style.map("TButton",
                foreground=[("active", "black")],
                background=[("active", "gray")])
        
        # entry box
        style.configure("TEntry", fieldbackground="gray", foreground="black")
        
        # listbox
        list_todos.config(bg="gray")
        
        dark_mode.place_forget()

    def add_task():
        # lägger till ny från text-inmatning
        new_todo = entry.get()
        if new_todo:
            print(f"New todo added: {new_todo}")
            # lägger till i listorna
            todos.append(new_todo)
            list_todos.insert(tk.END, new_todo)
            # rensar textfönster
            entry.delete(0, tk.END)
            show_remove()
            
    def exit():
        # sparar och stänger av
        todo_manager.save_todos(todos)
        root.destroy()
        
    def remove_task():
        index = list_todos.curselection()
        if index: # om något är valt
            # sparar objektet på index
            task_to_remove = list_todos.get(index)
            #tar bort enligt index
            list_todos.delete(index)
            #tar bort i todos efter obejekte
            todos.remove(task_to_remove)
            
            show_remove()
            
    def hide_rm():
        # byt knapp
        rm_all_button.place_forget()
        r_u_sure_button.place(x=40, y=100)
        
    def remove_all():
        #rensa listor
        list_todos.delete(0, tk.END)
        todos.clear()
        
        #byt knapp till original
        r_u_sure_button.place_forget()
        rm_all_button.place(x=50, y=100)
        
        show_remove()
        
    def show_remove():
        if len(todos) > 1:
            rm_all_button.place(x=50, y=100)
        else:
            rm_all_button.place_forget()
            

    # main window
    root = tk.Tk()
    root.geometry(f"{W_HEIGHT}x{W_WIDTH}")
    root.config(bg="lightgray")

    # ladda bild
    image_path = os.path.join(os.path.dirname(__file__), "assets", "background.png")
    image = Image.open(image_path)
    bg_image = ImageTk.PhotoImage(image)
    
    #skapa label för image
    #bg_label = tk.Label(root, image=bg_image)
    #bg_label.place(relwidth=1, relheight=1, x=0, y=0)
    
    # frame 
    frm = ttk.Frame(root, padding=10)
    frm.place(relheight=1, relwidth=1)

    # styles
    style = ttk.Style()
    style.configure("TFrame", background="lightgray")
    
    # entry widget
    entry = ttk.Entry(frm)
    entry.grid(column=1, row=1, padx=10, pady=10)

    # task button widget
    button = ttk.Button(frm, text="Add task", command=add_task)
    button.grid(column=2, row=1)
    
    # remove button
    rm_button = ttk.Button(frm, text="Remove task", command=remove_task)
    rm_button.place(x=50, y=50)
    
    # remove all button
    rm_all_button = ttk.Button(frm, text="Remove ALL!", command=hide_rm)
    r_u_sure_button = tk.Button(frm, text="Are you sure?", bg="red", activebackground="red", command=remove_all)
    show_remove()
    
    # color button
    dark_mode = tk.Button(frm, text="?", command=change_bg_color)
    dark_mode.place(x=340, y=5)

    # exit button
    exit = ttk.Button(frm, text="Quit", command=exit)
    exit.place(x=10, y= 240)

    # Listbox 
    list_todos = tk.Listbox(frm)
    list_todos.grid(row=2, column=2, padx=10, pady=10)
    for todo in todos:
        list_todos.insert(tk.END, todo)
        

    root.mainloop()
    
if __name__ == "__main__":
    run_gui()