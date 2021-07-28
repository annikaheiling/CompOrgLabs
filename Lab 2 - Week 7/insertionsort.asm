# Author: Annika Heiling, 7/26/2021
# CS: 2630, Computer Organization, Summer 2021
# Lab2 2) Create a MIPS program that performs an insertion sort
# on an array of values declared in .data 
# 
# Registers in use:
# $t0 : start address of the array
# $t1 : arrLen (length of 'array')
# $t2 : array[j] address (as in insertionSort pseudocode)
# $t3 : array[j] value
# $t4 : array[j+1] value
# $t5 : address of arrLen
# $t6 : i
# $t7 : j

.data
array: .word 3, 7, 4, 1, 5, 2 #array to be sorted
arrLen: .word 6 #number of elements in the array

.text
.globl main
#insertionSort(array, n) #where array is array, n is its length
main:
la    $t0, array #loads array address into t0
lw    $t1, arrLen #puts length of array into t1
li    $t6, 0  #initialize i

##for i=1 to len-1
forLoop:
#addi $t6, $t6, 1
##   j=i
bge  $t6, $t1, end
move $t7, $t6
addi $t6, $t6, 1

while:
##   while j>0 and arr[j] < arr[j-1]
#get vals of arr[j], arr[j-1]
# $t2 : array[j]
mul   $t2, $t7, 4
add   $t2, $t2, $t0
lb    $t3, 0($t2)

# $t3 : array[j+1]
add   $t2, $t2, 4
lb    $t4, 0($t2)

#conditional j to swapVals: if either condition is false, go
#	back to for loop and don't swap the values
bltz $t7, forLoop
bge  $t4, $t3, forLoop #arr[j-1], arr[j]
j swapVals
  
swapVals:
##      swap arr[j], arr[j-1]
move  $s0, $t2  #put add of arr[j+1] into temp s0
#if the address is that of the length, end
la    $t5, arrLen
beq   $s0, $t5, end

sub   $s1, $s0, 4 #get to address of arr[j]
sw    $t4, ($s1) #put them back into array memory, but in swapped positions
sw    $t3, ($s0)
##      j=j-1
addi  $t7, $t7, -1
j while

end:
