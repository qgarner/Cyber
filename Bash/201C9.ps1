# Quinton Garner
#5/9/2023
#Powershell Script

# Task 1
$Begin = Get-Date -Date '05/07/2023 00:00:00'
$End = Get-Date -Date '05/08/2023 23:59:59'
Get-Everything -LogName System -After $Begin -Before $End >C:\Users\q4998\Desktop\last_24.txt

#Task 2
Get-EventLog -LogName System -EntryType Error >C:\Users\q4998\Desktop\error.txt

#Task 3
Get -EventLog -LogName System -InstanceID 16

#Task 4
Get -EventLog -LogName System -InstanceID 20

#Task 5
$Events = Get-EventLog -LogName System -Newest 500
$Events / Group-Object -Property Source -NoElement / Sort-Object -Property Count -Descending >
