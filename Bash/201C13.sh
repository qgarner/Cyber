#!/bin/bash
#Quinton Garenr
#5/13/2023
#WhoIs

echo "Type address"
read address

info(){


whois $address 
dig $address 
host $address 
nslookup $address 
}

info > info.txt