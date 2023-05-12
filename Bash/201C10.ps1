#Quin Garner
#5/11/2023



# Task 1

Get-Process | Sort-Object -Property cpu -Descending

 

# Task 2

Get-Process | Sort-Object Id -Descending

 

# Task 3

Get-Process | Sort-Object -Property WorkingSet -Descending | Select-Object -First 5

 

# Task 4

Start-Process -FilePath "C:\Program Files (x86)\Internet Explorer\iexplore.exe" https://owasp.org/www-project-top-ten/

 

# Task 5

for ($i=1 ; $i -le 10; $i++)

{

    Start-Process -FilePath "C:\Program Files (x86)\Internet Explorer\iexplore.exe" https://owasp.org/www-project-top-ten/

}

 

# Task 6

Stop-Process -name iexplore

 

# Task 7

 

Start-Process -FilePath "C:\Program Files (x86)\Internet Explorer\iexplore.exe" https://owasp.org/www-project-top-ten/

 

Get-Process -Name iexplore | Select-Object -Property Id | Stop-Process

