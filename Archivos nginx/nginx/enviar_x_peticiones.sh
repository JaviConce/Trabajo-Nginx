#!/bin/bash

num=$1

for i in $(seq 1 $num)
do
  curl http://localhost:80/ > /dev/null
done

