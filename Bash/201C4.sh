#!/bin/bash

#Script:Ops 201 Class 4 Challenge
#Author Quin Garner
#Date of revision 5/1/2023
#Purpose: Make an array

#Main

mkdir dir1
mkdir dir2
mkdir dir3
mkdir dir4

folders=("dir1" "dir2" "dir3" "dir4")

touch ${folders[0]}/file.txt
touch ${folders[1]}/file.txt
touch ${folders[2]}/file.txt
touch ${folders[3]}/file.txt

#End

