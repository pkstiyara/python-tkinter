import tkinter as tk
import psutil
import platform

# Function to update system information
def update_system_info():
    # Get system information
    system_info = f"System: {platform.system()} {platform.release()}\n"
    cpu_info = f"CPU Usage: {psutil.cpu_percent()}%\n"
    memory_info = f"Memory Usage: {psutil.virtual_memory().percent}%\n"
    disk_info = f"Disk Usage: {psutil.disk_usage('/').percent}%\n"

    # Update text widget with system information
    text.delete(1.0, tk.END)  # Clear previous output
    text.insert(tk.END, system_info)
    text.insert(tk.END, cpu_info)
    text.insert(tk.END, memory_info)
    text.insert(tk.END, disk_info)

# Create the main application window
root = tk.Tk()
root.title("DevOps Server Monitor")  # Set the title of the window

# Create a button to update system information
update_button = tk.Button(root, text="Update System Info", command=update_system_info)
update_button.pack(pady=5)  # Add padding around the button

# Create a text widget to display system information
text = tk.Text(root, height=10, width=50)
text.pack(pady=5)  # Add padding around the text widget

# Run the Tkinter event loop
root.mainloop()
