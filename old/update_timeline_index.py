import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
import sys

def select_file():
    filepath = filedialog.askopenfilename(
        title="Select DaVinci Resolve .db file",
        filetypes=[("Database files", "*.db"), ("All files", "*.*")]
    )
    if filepath:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filepath)

def run_fix():
    db_path = file_entry.get()
    if not db_path:
        messagebox.showerror("Error", "Please select a database file first")
        return
    
    # Get the directory of the current script/executable
    if getattr(sys, 'frozen', False):
        script_dir = os.path.dirname(sys.executable)
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
    
    python_script = os.path.join(script_dir, "update_timeline_index.py")
    
    try:
        if getattr(sys, 'frozen', False):
            # If running as executable, import and run directly
            sys.path.append(script_dir)
            from update_timeline_index import update_timeline_index
            update_timeline_index(db_path)
            messagebox.showinfo("Success", "Database updated successfully!")
        else:
            # If running as script, call the other script
            result = subprocess.run([sys.executable, python_script, db_path], 
                                   capture_output=True, text=True)
            if "successful" in result.stdout:
                messagebox.showinfo("Success", "Database updated successfully!")
            else:
                messagebox.showerror("Error", f"Something went wrong:\n{result.stdout}\n{result.stderr}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run script: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("DaVinci Resolve Project Fixer")
root.geometry("500x200")
root.resizable(False, False)

# Create the widgets
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill=tk.BOTH, expand=True)

label = tk.Label(frame, text="Select your extracted .db file from the DaVinci Resolve project:")
label.pack(anchor=tk.W, pady=(0, 10))

file_frame = tk.Frame(frame)
file_frame.pack(fill=tk.X, pady=(0, 20))

file_entry = tk.Entry(file_frame)
file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

browse_button = tk.Button(file_frame, text="Browse", command=select_file)
browse_button.pack(side=tk.RIGHT, padx=(10, 0))

fix_button = tk.Button(frame, text="Fix Project Database", command=run_fix, bg="#4CAF50", fg="white", pady=10)
fix_button.pack(fill=tk.X)

instructions = tk.Label(frame, text="Remember to repackage the fixed .db file back into your .drp project.", 
                      wraplength=460, justify=tk.LEFT)
instructions.pack(anchor=tk.W, pady=(20, 0))

root.mainloop()