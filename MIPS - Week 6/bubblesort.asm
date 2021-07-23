# Program written by Annika Heiling
# CS: 2630, Computer Organization, Summer 2021

# Use meaningful labels for all pieces of data. Please include in comments each register
# that is being used and what it is being used for. Place these near the top of the file. 
# 1) Create a MIPS program that performs a bubble sort on some array of values declared in the .data
# directive. Use a meaningful label for this array of values and the array’s associated length.

.data
unsorted: .word 2, 7, 4, 1, 5, 3 #array to be sorted
arrLen: .word 6 #number of elements in the array

.text

.globl main

main:
