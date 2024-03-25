import tkinter as tk
from tkinter import filedialog
selected_path = ''
selected_file = ''
def GUI_path():
    global selected_path
    def choose_directory():
        # Display the file dialog and get the chosen path
        chosen_path = filedialog.askdirectory()
        # Update the label text with the chosen path
        path_label.config(text=chosen_path)
        # Update the rectangle length to match the label width
        rectangle.config(width=len(chosen_path))
        # Update the border width to match the rectangle width
        border_width = max(1, int(len(chosen_path) / 10))
        rectangle.config(highlightthickness=border_width)
        # Save the chosen path in a variable
        global selected_path
        selected_path = chosen_path

    def confirm_selection():
        # Close the window
        root.destroy()

    # Create the main window
    root = tk.Tk()
    root.title("Source file directory")
    root.geometry("550x250")
    # Create a button to choose a directory
    choose_button = tk.Button(root, 
                font=('Arial', 15, 'bold'),
                fg="white",
                bg="black",
                text="Choose Directory", 
                command=choose_directory)
    choose_button.place(x = 55, y = 0)
    choose_button.pack()

    # Create a label to display the chosen path
    path_label = tk.Label(root, text="",font=('Arial',15,'bold'),)
    path_label.pack()

    # Create a rectangle to display the chosen path
    rectangle = tk.Canvas(root, width=0, height=20, bd=0, highlightthickness=0, relief='ridge')
    rectangle.pack()

    # Create a button to confirm the selection
    confirm_button = tk.Button(root,
                font=('Arial', 15, 'bold'),
                text="Confirm",
                fg="white",
                bg="black", 
                command=confirm_selection)
    confirm_button.pack()

    #Displayed message 1
    label = tk.Label(root,
             text = "Choose a directory where you want to save the generated source code",
             font=('Arial',10,'bold'),
             fg="#00ff00",
             bg = "black",
             bd = 4,
             padx = 20,
             pady = 20)
    label.pack()
    label.place(x=40,y= 180)


    # Start the main event loop
    root.mainloop()
    if selected_path == '':
        quit(print("Script terminated. Exiting ..."))
    return selected_path

file_name = None
def getpath():
    global file_name
    global selected_file

    def sub_open():
        global file_name
        file_name = filedialog.askopenfilename(title="Opening file",
                                               filetypes=[("Text files","*.txt"),
                                                          ("Assembly files","*.s"),
                                                          ("Assembly Files","*.S"),
                                                          ("Assembly Files","*.asm")])
        global selected_file
        # Update the label text with the chosen path
        path_label.config(text=file_name)
        # Update the rectangle length to match the label width
        rectangle.config(width=len(file_name))
        # Update the border width to match the rectangle width
        border_width = max(1, int(len(file_name) / 10))
        rectangle.config(highlightthickness=border_width)
        # Save the chosen path in a variable
        selected_file = file_name


    def submit_command():
        window.destroy()

    #window parameters
    window = tk.Tk()
    window.title("Assembly file selection")
    window.geometry("550x340")
    #Submit button
    submit = tk.Button(text="Submit",
                    command=submit_command,
                    font=('Arial', 15, 'bold'),
                    fg="white",
                    bg="black",
                    padx = 30,
                    pady = 5)
    submit.pack()
    submit.place(x=225,y=210)
    #Open file button
    open_file_btn = tk.Button(text="Open file",
                    command=sub_open,
                    font=('Arial', 15, 'bold'),
                    fg="white",
                    bg="black",
                    padx = 20,
                    pady = 5)
    open_file_btn.pack()
    open_file_btn.place(x=225,y=90)
    #Displayed message 1
    label = tk.Label(window,
             text = "Choose your assembly file",
             font=('Arial',10,'bold'),
             fg="#00ff00",
             bg = "black",
             relief = tk.RAISED,
             bd = 4,
             padx = 20,
             pady = 20)
    label.pack()
    label.place(x=186,y=10)
    #Display message 2
    label1 = tk.Label(window,
             text = "File name :",
             font=('Arial',13,'bold'),
             relief = tk.RAISED,
             bd = 0,
             padx = 0,
             pady = 8.5)
    label1.pack()
    label1.place(x=80,y=150)

    # Create a label to display the chosen path
    path_label = tk.Label(window, text="",font=('Arial',13,'bold'),)
    path_label.pack()
    path_label.place(x=170,y=156)
    

    # Create a rectangle to display the chosen path
    rectangle = tk.Canvas(window, width=0, height=20, bd=0, highlightthickness=0, relief='ridge')
    rectangle.pack()
    rectangle.place(x=0,y=0)

    window.mainloop()

    if file_name == None:
        quit(print('... Script terminated, please enter a valid file name'))
    return str(file_name)