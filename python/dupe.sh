#!/bin/bash

for i in $(seq -f "%02g" 8 25)
do
  cp day07.py "day$i.py"
done