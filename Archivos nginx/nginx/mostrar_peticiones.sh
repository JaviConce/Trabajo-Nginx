#!/bin/bash

countb1=$(grep -o '\b127\w*' backend1.log | wc -l)
echo "Peticiones backend 1: $countb1"

countb2=$(grep -o '\b127\w*' backend2.log | wc -l)
echo "Peticiones backend 2: $countb2"

countb3=$(grep -o '\b127\w*' backend3.log | wc -l)
echo "Peticiones backend 3: $countb3"
