#!/bin/bash
#Quin Garner
#Class 301 Challenge 4
#Main
#Make a true statement so that while loop will run
s=z
while [ $s = z ]
do 
echo "Please Choose"
echo "1 Hello World"
echo "2 ping self"
echo "3 ip info"
echo "4 exit"
read x
#Call on x for variable so that will read which option will be used
if [ $x = 1 ]
    then echo "Hello World"
# 3 is there so that is will ping only 3 times instead of continuos
elif [ $x = 2 ]
    then ping -c 3 localhost

elif [ $x = 3 ]
    then ifconfig 

else [ $x = 4 ]
    exit
fi

echo "try again y/n"
read s
done

#End