#!/bin/bash
# Push any coding issues into an array
ISSUES=()

# Iterate over all of the files in directory
find . -type f | while read line; do
    # FIND ALL FILES THAT DON'T HAVE AN EXTENSION
    # 1: invalid naming $line
    if ! [[ $line =~ (.\/)(.*)\.(.+)$ ]] ; then 
        ISSUES+=('invalid naming $line')
    fi
    # FIND ALL LONG FILE PATHS
    # 2: long file path
    if [[ expr length $line \> 20 ]] ; then
        echo long path $line
    fi

done

# Print results
echo "${ISSUES[*]}"