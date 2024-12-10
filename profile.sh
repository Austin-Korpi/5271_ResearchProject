#!/bin/bash

# Check if exactly one argument is provided
if [ "$#" -ne 2 ]; then
    echo "Usage:   ./profile.py <process name> <library>"
    exit 1
fi

# Check if correct library name is provided
if [ "$2" != "libc" ] && [ "$2" != "ffmalloc" ] && [ "$2" != "ffmallocnu" ]; then
    echo "Usage:   ./profile.py <process name> <library>"
    echo '<library> must be one of "libc" "ffmalloc" "ffmallocnu"'
    exit 1
fi

# Build output file name
OUTPUT_FILE="$1_$2.txt"

# Write header
if [ ! -s $OUTPUT_FILE ]; then
    echo "Timestamp    Virtual Physical" > $OUTPUT_FILE
fi

# Poll memory of process
while true; do
    # Check if program is running
    if  [ $(pgrep -x "$1") ]; then
        # Get timestamp
        TIMESTAMP=$(date +"%H:%M:%S.%3N")
        # Get virtual and physical memory
        GET_MEMORY=$(pmap -x `pgrep $1` | tail -n 1 | awk '{print $3, $4}')

        # Write data to file
        echo "$TIMESTAMP $GET_MEMORY" >> $OUTPUT_FILE

        sleep 1
    fi
done
