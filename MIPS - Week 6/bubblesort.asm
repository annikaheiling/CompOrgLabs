# Author: Annika Heiling, 7/22/2021
# CS: 2630, Computer Organization, Summer 2021
# Lab2 1) Create a MIPS program that performs a bubble sort on an array of values declared in .data
#
# Registers in use:
# $t0 : start index of the array
# $t1 : arrLen (length of 'array'
# $t2 : array[i] (as in bubbleSort pseudocode)
# $t3 : array[i+1] (as in bubbleSort pseudocode)
# $t6 : outerFor loop counter
# $t7 : innerFor loop counter

.data
array: .byte 3, 7, 4, 1, 5, 2 #array to be sorted
#array: .ascii "374152" #only works for values < 10... since reads in 1 char at time
arrLen: .word 6 #number of elements in the array

.text
.globl main
#bubbleSort(array, n) #where array is array, arrLen is its length
main:
la    $t0, array
lw    $t1, arrLen
move  $t6, $t1
move  $t7, $t1

lb    $t2, 0($t0) #del this
lb    $t3, 1($t0) #and this

#for arrLen to arrLen-1
outerFor:
#conditional: if $t6 > 0, run it, else, finish program?
bgtz 
addi $t6, $t6, -1

#  for 0 to arrLen-2
innerFor:
#conditional: if $t7 > 0, run it, else, break innerFor?

#    if array[i] > array[i+1]
if:

#      swap places of array[i], array[i+1]
swap:

end: