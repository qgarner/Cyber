#!/bin/bash
# Script: Ops 301 Class 03 Ops Challenge Solution
# Author: Quin Garner
# Date of latest revision: 06/07/23
# Prompts user for input directory path.
# Prompts user for input permissions number (e.g. 777 to perform a chmod 777).
# Navigates to the directory input by the user and changes all files inside it to the input setting.
# Prints to the screen the directory contents and the new permissions settings of everything in the directory.
# Main
echo "Please input directory path."
ls
read File
echo "Please input permissions number."
read PermNum
chmod $PermNum $File
echo "Permission has been granted to $File."
ls -l $File
# End