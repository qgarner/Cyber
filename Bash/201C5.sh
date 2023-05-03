#!/bin/bash

#Author: Quinton Garner
#Date:5/2/2023
#Assignment: Creating a Loop

#Add variable for script understanding
y="x"

#Create loop as long as y="x" 
#choose a pid on terminal that is echoed to terminal
#once choose the pid it will kill that process running
#$ to show that the task or variable has been chosen and needs to be called on
#Use brackets to list variables
while [ $y == "x" ]
do 
  ps aux
  echo "Choose a PID"
  read pid 
  kill $pid
  break
done


 