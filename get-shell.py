import tkinter as tk
import subprocess

# Function to execute shell command
def execute_command():
    command = entry.get()
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        text.delete(1.0, tk.END)  # Clear previous output
        text.insert(tk.END, output)
    except subprocess.CalledProcessError as e:
        text.delete(1.0, tk.END)  # Clear previous output
        text.insert(tk.END, f"Error: {e.output}")

# Create the main application window
root = tk.Tk()
root.title("DevOps Command Executor")  # Set the title of the window

# Create an entry widget for command input
entry = tk.Entry(root, width=50)
entry.pack(pady=5)  # Add padding around the entry widget

# Create a button to execute the command
execute_button = tk.Button(root, text="Execute Command", command=execute_command)
execute_button.pack(pady=5)  # Add padding around the button

# Create a text widget to display command output
text = tk.Text(root, height=20, width=70)
text.pack(pady=5)  # Add padding around the text widget

# Run the Tkinter event loop
root.mainloop()
