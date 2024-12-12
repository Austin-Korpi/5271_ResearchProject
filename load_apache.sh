#! /bin/bash
end=$((SECONDS+300))

while [ $SECONDS -lt $end ]; do
    ab -n 10 localhost/index.html > /dev/null
    sleep 1
done
