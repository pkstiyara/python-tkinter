import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("My GUI Application")  # Set the title of the window

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)  # Add padding around the label

# Create a button widget
button = tk.Button(root, text="Click Me!")
button.pack(pady=5)  # Add padding around the button

# Run the Tkinter event loop
root.mainloop()
