# DaVinci Resolve Project Fixer

This tool helps fix corrupted DaVinci Resolve project files by repairing the timeline index in the project's database. It's designed for situations where your .drp file crashes when opened in DaVinci Resolve.

## Download and Installation

Download the latest executable from the [Releases](https://github.com/ivan-si/Davinci-Resolve-Project-Crash-Fixer/releases) page.

- **Windows users**: Download the `.exe` file and run it directly.
- No installation required - the application is ready to use out of the box.
- No Python installation needed.

## How to Use

### Fixing DaVinci Resolve Projects (.drp files)

1. **Back up your original project file**
   - Always make a copy of your .drp file before attempting any repairs

2. **Extract your .drp project file**
   - Rename your `.drp` file to `.zip`
   - Extract the contents to a folder

3. **Run the Fixer**
   - Launch the DaVinci Resolve Fixer application
   - Click "Browse" and select the `.db` file from your extracted project
   - Click "Fix Project Database"
   - Wait for the confirmation message

4. **Repackage your project**
   - Once fixed, zip the folder contents back up
   - Rename the `.zip` file back to `.drp`
   - Open the fixed project in DaVinci Resolve

### Alternative Method (Using Project.db directly)

If you prefer to fix the database directly from DaVinci Resolve:

1. In DaVinci Resolve, open the Project Manager window
2. Open the Database panel on the left side
3. Right-click on the database where your project is located 
4. Click 'Open File Location'
5. Navigate through:
   - "Resolve Projects" directory
   - "Users" directory
   - Your username (may be "guest" or "admin")
   - "Projects" directory
   - The folder with the name of your corrupted project
   - Locate the `Project.db` file
6. Make a backup copy of this file
7. Use the Fixer application on this copy
8. Replace the original with your fixed copy if successful

⚠️ **IMPORTANT: Before making any changes:**
- Always make a backup copy of the original Project.db file
- Only modify the copy, never the original

## What This Tool Fixes

This application specifically repairs the `media_pool_v_timeline_item` table in your project database by:
- Reindexing all timeline items
- Ensuring sequential ordering of timeline items
- Fixing the common corruption that causes DaVinci Resolve to crash when opening projects

The tool does not modify your actual project content or media, just the database indices that tell Resolve how to organize your timeline items.

## Troubleshooting

- **Application won't start**: Make sure you have Windows administrator privileges
- **"Database not found" error**: Verify that you selected a valid DaVinci Resolve .db file
- **"Fix failed" message**: Check the error details and ensure the file is not read-only
- **Project still crashes**: Your project may have additional issues beyond timeline indices

## Building from Source

If you want to build the executable yourself:

1. Clone this repository
2. Install Python requirements:
   ```
   pip install pyinstaller tkinter
   ```
3. Create an icon file named `icon.ico` (optional)
4. Run the build command:
   ```
   pyinstaller davinci_fixer.spec
   ```

## Help and Support

If you encounter issues with this tool, please open an issue on the GitHub repository or reach out for support.

---

*Disclaimer: Use this tool at your own risk. Always back up your files before attempting any repairs.*
