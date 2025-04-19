import sqlite3
import sys
import os
import re

def update_timeline_index(db_input):
    # Remove any surrounding quotes that might be present
    db_input = re.sub(r'^["\']\s*|["\']$', '', db_input)
    
    # Determine whether input is a full path or just a filename
    if os.path.isabs(db_input):
        db_path = db_input
    else:
        # Use the current script directory and join with the provided filename
        script_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(script_dir, db_input)
    
    # Validate path
    if not os.path.exists(db_path):
        print(f"Error: Database file not found at: {db_path}")
        return
    
    if not db_path.endswith(".db"):
        print("Error: The file must be a .db SQLite database.")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE SM_Project SET CurrentTimelineIndex = 0")
        cursor.execute("SELECT CurrentTimelineIndex FROM SM_Project")
        rows = cursor.fetchall()
        print(rows)
        conn.commit()
        print("Update successful.")
    except sqlite3.Error as error:
        print("Error while updating the database:", error)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <database_filename_or_full_path>")
    else:
        # Handle the case where the path might contain spaces
        db_path = ' '.join(sys.argv[1:])
        update_timeline_index(db_path)
