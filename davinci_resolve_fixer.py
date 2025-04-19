import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import sys
import sqlite3
import threading
import traceback

class DaVinciResolveFixer:
    def __init__(self, root):
        self.root = root
        self.root.title("DaVinci Resolve Project Fixer")
        self.root.geometry("550x400")
        self.root.minsize(550, 300)
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#4CAF50")
        self.style.configure("Accent.TButton", background="#4CAF50", foreground="white")
        
        # Main frame
        self.main_frame = ttk.Frame(root, padding="20 20 20 20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # App title
        title_label = ttk.Label(self.main_frame, text="DaVinci Resolve Project Fixer", font=("Helvetica", 14, "bold"))
        title_label.pack(anchor=tk.W, pady=(0, 15))
        
        # File selection section
        file_label = ttk.Label(self.main_frame, text="Select your extracted .db file from the DaVinci Resolve project:")
        file_label.pack(anchor=tk.W, pady=(0, 5))
        
        file_frame = ttk.Frame(self.main_frame)
        file_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.file_entry = ttk.Entry(file_frame)
        self.file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        browse_button = ttk.Button(file_frame, text="Browse", command=self.select_file)
        browse_button.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Progress bar
        self.progress = ttk.Progressbar(self.main_frame, orient=tk.HORIZONTAL, length=100, mode='indeterminate')
        self.progress.pack(fill=tk.X, pady=(0, 15))
        self.progress.pack_forget()  # Hide initially
        
        # Status label
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_label = ttk.Label(self.main_frame, textvariable=self.status_var)
        status_label.pack(anchor=tk.W, pady=(0, 15))
        
        # Fix button
        self.fix_button = ttk.Button(
            self.main_frame, 
            text="Fix Project Database", 
            command=self.run_fix,
            style="Accent.TButton"
        )
        self.fix_button.pack(fill=tk.X, ipady=5)
        
        # Instructions
        instructions_frame = ttk.LabelFrame(self.main_frame, text="Instructions")
        instructions_frame.pack(fill=tk.X, pady=(15, 0))
        
        instructions_text = (
            "1. Extract your .drp project file (rename to .zip and extract)\n"
            "2. Select the .db file from the extracted folder\n"
            "3. Click 'Fix Project Database'\n"
            "4. Repackage the fixed .db file back into your .drp project"
        )
        
        instructions = ttk.Label(
            instructions_frame, 
            text=instructions_text,
            wraplength=500, 
            justify=tk.LEFT
        )
        instructions.pack(anchor=tk.W, padx=10, pady=10)
    
    def select_file(self):
        filepath = filedialog.askopenfilename(
            title="Select DaVinci Resolve .db file",
            filetypes=[("Database files", "*.db"), ("All files", "*.*")]
        )
        if filepath:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, filepath)
    
    def run_fix(self):
        db_path = self.file_entry.get()
        if not db_path:
            messagebox.showerror("Error", "Please select a database file first")
            return
        
        # Start progress bar
        self.progress.pack(fill=tk.X, pady=(0, 15))
        self.progress.start()
        self.fix_button.config(state=tk.DISABLED)
        self.status_var.set("Fixing database...")
        
        # Run in a separate thread to keep GUI responsive
        thread = threading.Thread(target=self.update_database, args=(db_path,))
        thread.daemon = True
        thread.start()
    
    def update_database(self, db_path):
        try:
            result = update_timeline_index(db_path)
            
            # Update UI in the main thread
            self.root.after(0, self.on_complete, True, "Database updated successfully!")
        except Exception as e:
            error_msg = f"Error: {str(e)}\n\n{traceback.format_exc()}"
            self.root.after(0, self.on_complete, False, error_msg)
    
    def on_complete(self, success, message):
        # Stop and hide progress bar
        self.progress.stop()
        self.progress.pack_forget()
        self.fix_button.config(state=tk.NORMAL)
        
        # Show result
        if success:
            self.status_var.set("Fix completed successfully!")
            messagebox.showinfo("Success", message)
        else:
            self.status_var.set("Failed to fix database")
            messagebox.showerror("Error", message)


def update_timeline_index(db_path):
    """Fix DaVinci Resolve project database by updating timeline index."""
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Update the timeline items with sequential indices

        cursor.execute("UPDATE SM_Project SET CurrentTimelineIndex = 0")
        cursor.execute("SELECT CurrentTimelineIndex FROM SM_Project")
        rows = cursor.fetchall()
        
        # Commit the changes
        conn.commit()
        conn.close()
        
        return True
    except sqlite3.Error as e:
        raise Exception(f"SQLite error: {e}")
    except Exception as e:
        raise Exception(f"Failed to update database: {e}")


def main():
    root = tk.Tk()
    app = DaVinciResolveFixer(root)
    
    # Set icon if available
    try:
        # For frozen executables, use the resource path
        if getattr(sys, 'frozen', False):
            base_dir = sys._MEIPASS
        else:
            base_dir = os.path.abspath(os.path.dirname(__file__))
        
        icon_path = os.path.join(base_dir, "icon.ico")
        if os.path.exists(icon_path):
            root.iconbitmap(icon_path)
    except Exception:
        # If icon loading fails, continue without icon
        pass
    
    root.mainloop()


if __name__ == "__main__":
    main()