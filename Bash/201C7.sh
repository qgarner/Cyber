#!bin/bash

# Quinton Garner
#5/4/2023
#LSHW Command Script

echo "CPU"
lshw -C cpu | grep -i product
lshw -C cpu | grep -i vendor
lshw -C cpu | grep -i physical id
lshw -C cpu | grep -i bus info
lshw -C cpu | grep -i width

echo "RAM"
lshw -C ram | grep -i description
lshw -C ram | grep -i physical id
lshw -C ram | grep -i size

echo "Display Adapter"
lshw -C display | grep -i description
lshw -C display | grep -i product
lshw -C display | grep -i vendor
lshw -C display | grep -i physical id
lshw -C display | grep -i bus info
lshw -C display | grep -i width
lshw -C display | grep -i clock
lshw -C display | grep -i capabilities
lshw -C display | grep -i configuration
lshw -C display | grep -i resources

echo "Network Adapter"
lshw -C network | grep -i description
lshw -C network | grep -i product
lshw -C network | grep -i vendor
lshw -C network | grep -i physical id
lshw -C network | grep -i bus info
lshw -C network | grep -i logical name
lshw -C network | grep -i version
lshw -C network | grep -i serial
lshw -C network | grep -i size
lshw -C network | grep -i capacity
lshw -C network | grep -i width
lshw -C network | grep -i clock
lshw -C network | grep -i capabilities
lshw -C network | grep -i configuration
lshw -C network | grep -i resources