#!/bin/bash

num=$1
contador=0

for i in $(seq 1 $num)
do
  sleep 0.5
  contador=$((contador + 1))
  curl http://localhost:80/ > /dev/null
done

echo "Iteración $i: contador = $contador"
