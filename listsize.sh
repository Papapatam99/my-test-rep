#!/bin/bash

get_size() {
    local path="$1"
    local size=$(du -hs "$path" 2>/dev/null | cut -f1)
    echo $size
    }

files=$(ls -A)

for item in $files;
    do
	size=$(get_size "$item")
	echo -e "$size\t$item"
    done | sort -hr -k1,1

echo -e "\n КОНЕЦ!"
