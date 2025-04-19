# DaVinci Resolve Project (.drp) Recovery Tool

This tool helps fix corrupted DaVinci Resolve project files by resetting the current timeline index in the project's database. It's intended for situations where your .drp file crashes when opened in DaVinci Resolve.

## Prerequisites

- **Python**: You need Python installed on your computer. If you don't have Python installed:
  - **Windows**: Download and install from [python.org](https://www.python.org/downloads/)
  - **Mac**: Python is usually pre-installed, but you can install the latest version from [python.org](https://www.python.org/downloads/)
  - **Linux**: Use your distribution's package manager (e.g., `sudo apt install python3` for Ubuntu)

## Finding Your Project.db File

1. In DaVinci Resolve, open the Project Manager window
2. Open the Database panel on the left side
3. Right-click on the database where your project is located 
4. Click 'Open File Location'
5. Navigate through these folders:
   - Click "Resolve Projects" directory
   - Click "Users" directory
   - Click your username (may be "guest" or "admin")
   - Click "Projects" directory
   - Click the folder with the name of your corrupted project
   - Inside you should find a file called `Project.db`

⚠️ **IMPORTANT: Before making any changes:**
- Make a copy of the Project.db file
- Only modify the copy, never the original
- Keep an unmodified backup of the original file in case something goes wrong

## Using the Recovery Tool

### For Windows Users

#### Option 1: Using the Batch File (Easiest)

*If you're already familiar with running batch files, you can skip to step 3.*

1. Make sure both the Python script (`update_timeline_index.py`) and the batch file (`fix_drp_file.bat`) are in the same folder
2. Double-click the `fix_drp_file.bat` file to run it
3. When prompted, drag and drop your Project.db file from File Explorer into the command window
4. Press Enter
5. If successful, you'll see a message: "Update successful."

#### Option 2: Using Command Line

1. Open Command Prompt:
   - Press Windows Key + R
   - Type `cmd` and press Enter
2. Navigate to the folder containing the script:
   ```
   cd path\to\script\folder
   ```
3. Run the script, replacing the path with your actual path to the Project.db copy:
   ```
   python update_timeline_index.py "C:\Path\To\Your\Project.db"
   ```

### For Mac/Linux Users

#### Option 1: Using the Shell Script (Easiest)

*If you're already familiar with running shell scripts, you can skip to step 4.*

1. Make sure both the Python script (`update_timeline_index.py`) and the shell script (`fix_drp_file.sh`) are in the same folder
2. First, you need to give the shell script permission to run:
   - Open Terminal (Applications → Utilities → Terminal)
   - Navigate to the folder containing the script:
     ```
     cd /path/to/script/folder
     ```
   - Run this command to make the script executable:
     ```
     chmod +x fix_drp_file.sh
     ```
3. Run the shell script:
   ```
   ./fix_drp_file.sh
   ```
4. When prompted, drag and drop your Project.db file from Finder into the Terminal window
5. Press Enter
6. If successful, you'll see a message: "Update successful."

#### Option 2: Using Terminal

1. Open Terminal (Applications → Utilities → Terminal)
2. Navigate to the folder containing the script:
   ```
   cd /path/to/script/folder
   ```
3. Run the script, replacing the path with your actual path to the Project.db copy:
   ```
   python3 update_timeline_index.py "/Path/To/Your/Project.db"
   ```

## After Running the Tool

1. Once you've successfully fixed the copy of your Project.db file:
   - Replace the original Project.db with your fixed copy
   - Keep your original backup just in case
2. Try opening your DaVinci Resolve project again

## Troubleshooting

- **"Python is not recognized as an internal or external command"**: This means Python is not installed or not in your system PATH. Install Python and ensure you check "Add Python to PATH" during installation.
- **File not found errors**: Double-check your file paths. Make sure there are no typos.
- **Permission denied**: Make sure you have the necessary permissions to access and modify the files.
- **Script did nothing**: Check that you're using the correct path to your Project.db file.

## What This Tool Does

This tool simply resets the CurrentTimelineIndex in your project database to 0, which can fix issues where DaVinci Resolve crashes when trying to open a project. It does not modify any of your actual project content, just the index that tells Resolve which timeline to open first.

## Help and Support

If you encounter issues with this tool, please open an issue on the GitHub repository or reach out for support.

---

*Disclaimer: Use this tool at your own risk. Always back up your files before attempting any repairs.*
