#!/bin/bash

poetry run python3 src/run.py

while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5000/ping)" != "200" ]]; 
  do sleep 1; 
done

poetry run robot src/tests/robot

status=$?

kill $(lsof -t -i:5000)

exit $status