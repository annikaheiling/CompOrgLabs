# Author: Annika Heiling, 7/26/2021
# CS: 2630, Computer Organization, Summer 2021
# Lab2 1) Create a MIPS program that performs a bubble sort
# on an array of values declared in .data
#
# Registers in use:
# $t0 : start address of the array
# $t1 : arrLen (length of 'array')
# $t2 : array[j] address (as in bubbleSort pseudocode)
# $t3 : array[j] value
# $t4 : array[j+1] value
# $t6 : outerFor loop counter (i)
# $t7 : innerFor loop counter (j)

.data
array: .word 7, 3, 4, 1, 5, 2 #array to be sorted
arrLen: .word 6 #number of elements in the array

.text
.globl main
#bubbleSort(array, n) #where array is array, n is its length
main:
la    $t0, array #loads array address into t0
lw    $t1, arrLen #puts length of array into t1
move  $t6, $t1 #initialize outerFor counter
li    $t7, 0 #initialize innerFor counter reg to 0 in t7

###for n-1 to 1
outerForCheck:
#conditional: if $t6 > 0, run it, else, end
bgtz $t6, outerFor
j end

outerFor:
addi $t6, $t6, -1
li   $t7, 0 #resets innerFor counter for each new outer iter
j innerForCheck

###  for 0 to arrLen-2
innerForCheck:
#conditional: if $t7 < i-1, run it, else break and go to outer loop
move   $s0, $t6
blt  $t7, $s0, ifCheck
j outerForCheck

###    check if array[j] > array[j+1]
ifCheck: 
# $t2 : array[j]
mul   $t2, $t7, 4
add   $t2, $t2, $t0
lb    $t3, 0($t2)

# $t3 : array[j+1]
add   $t2, $t2, 4
lb    $t4, 0($t2)

bgt   $t3, $t4, swap #swap the values in the array mem if array[j] > array[j+1]
addi $t7, $t7, 1
j innerForCheck 

### 	  swap places of array[j], array[j+1]
swap: #use temps to swap the values
move  $s0, $t2  #put add of arr[j+1] into temp s0
sub   $s1, $s0, 4 #get to address of arr[j]
sw    $t4, ($s1) #put them back into array memory, but in swapped positions
sw    $t3, ($s0)
j innerForCheck

end: