import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

# Function to install weather-util
def install_weather_util():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "weather-util"])
        messagebox.showinfo("Success", "weather-util installed successfully")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to install weather-util")

# Function to run weather-util and display output
def run_weather_util():
    zip_code = zip_code_entry.get()
    if not zip_code:
        messagebox.showwarning("Input Error", "Please enter a ZIP code")
        return
    try:
        output = subprocess.check_output(["weather", zip_code], universal_newlines=True)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, output)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to run weather-util: {e}")

# Create the main window
root = tk.Tk()
root.title("Weather Util GUI")

# Create a frame for the buttons and entry
frame = tk.Frame(root)
frame.pack(pady=10)

# Create and pack the ZIP code entry
zip_code_label = tk.Label(frame, text="Enter ZIP Code:")
zip_code_label.pack(side=tk.LEFT, padx=5)
zip_code_entry = tk.Entry(frame)
zip_code_entry.pack(side=tk.LEFT, padx=5)

# Create and pack the install button
install_button = tk.Button(frame, text="Install weather-util", command=install_weather_util)
install_button.pack(side=tk.LEFT, padx=5)

# Create and pack the run button
run_button = tk.Button(frame, text="Run weather-util", command=run_weather_util)
run_button.pack(side=tk.LEFT, padx=5)

# Create a text widget to display the output
output_text = tk.Text(root, wrap=tk.WORD, width=60, height=20)
output_text.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
