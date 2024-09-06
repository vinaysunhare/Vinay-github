#!/bin/bash

Array
myArray1 20 30.5 HelloHey Buddy!")

echoAll the values in the array are ${myArray[*]}"

echo "Value at index 3 is ${myArray[3]}"

# How to find the number of values, length of the array
echo "Number of values, length of the array is ${#myArray[@]}"
