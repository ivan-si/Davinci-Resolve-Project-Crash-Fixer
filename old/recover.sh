#!/bin/bash
echo "DaVinci Resolve Project Recovery Tool"
echo "==================================="
echo
echo "This tool will attempt to fix your corrupted DRP file"
echo
read -p "Drag and drop your extracted .db file here and press Enter: " drp_file
python3 update_timeline_index.py "$drp_file"
echo
echo "If successful, you can now repackage the db file back into your .drp"
echo "If you see an error, copy and paste all of the text you see into ChatGPT and ask what went wrong)"
read -p "Press Enter to exit"