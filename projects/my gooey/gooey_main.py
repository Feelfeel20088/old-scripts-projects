import tkinter as tk

def open_second_window():
    second_window = tk.Tk()
    second_window.title("Second Window")
    second_window.minsize(200, 100)  # Set minimum width and height for the second window
    second_label = tk.Label(second_window, text="This is the second window.")
    second_label.pack()
    second_window.mainloop()

# Create the first window
root = tk.Tk()
root.title("First Window")
root.minsize(600, 600)  # Set minimum width and height for the first window
label = tk.Label(root, text="This is the first window.")
cool = tk.Entry(root)
cool.pack()
label.pack()

# Create a button to open the second window
button = tk.Button(root, text="Open Second Window", command=open_second_window)
button.pack()

# Start the main event loop for the first window
root.mainloop()