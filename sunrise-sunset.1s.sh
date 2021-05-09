#!/bin/bash

wget -q --spider http://google.com

if [ $? -eq 0 ]; then
	out=$(python3 /FULL/PATH/TO/main.py)
	echo $out
else
    echo "offline and no data available"
fi