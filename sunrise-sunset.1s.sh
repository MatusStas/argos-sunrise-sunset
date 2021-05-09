#!/bin/bash

wget -q --spider http://google.com

if [ $? -eq 0 ]; then
	out=$(python3 /your/path/to/file/main.py)
	echo $out
else
    echo "offline"
fi