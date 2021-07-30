# Author: Annika Heiling, 7/29/2021
# CS: 2630, Computer Organization, Summer 2021
# Lab3a 1) Create a MIPS program that performs a binary search
# on an array of values declared in .data
#
# Registers in use:
# $t0 : start address of the array
# $t1 : arrLen (length of 'array')
# $t2 : array[test] address (arr[low] in last if/else) (as in binSearch pseudocode)
# $t3 : array[test] value (arr[low] in last if/else)
# $t4 : low
# $t5 : high
# $t6 : temp, used for many things (low+1, etc)
# $t7 : target value
#
# "##" denotes python code, translated into MIPS after it

.data
array: .word 1, 5, 15, 19, 20, 21, 25, 30, 39 #array to be sorted
arrLen: .word 9 #number of elements in the array
inputStr: .asciiz "Input target value: "
foundStr: .asciiz "Target value discovered at index: "
notFoundStr: .asciiz "Target value not found in array "

.text
.globl main
##binarySearch(array, size, target)
main:
#target value input:
li $v0, 4
la $a0, inputStr
syscall
li $v0, 5
syscall
move $t7, $v0

la    $t0, array #loads array address into t0
lw    $t1, arrLen #puts length of array into t1
##low=0
li    $t4, 0 #set low to 0
##high=size
move  $t5, $t1 #set high to array size

##while low+1 < high:
while:
addi $t6, $t4, 1 #use temp t6 to store low+1 for the branch check
bge  $t6, $t5, done #condition not met, go to done, else continue
##  test = (low+high)//2
add  $t6, $t4, $t5 #use temp t6 to store low+high
div  $t6, $t6, 2
mflo $t6 #temp t6 stores quotient of division, effectively integer division result

##  if arr[test] > target:
ifWhile:
#branch to elseWhile if condition false, else do high=test and then go back to While
mul   $t2, $t6, 4
add   $t2, $t2, $t0 #calculate the address of array[test]
lb    $t3, 0($t2) #loads the value of array[test] into t3 
#if target greater than or equal to arr[test], branch to elseWhile ##FIX
bge   $t7, $t3, elseWhile
##      high=test
move  $t5, $t6
j while

##  else:
elseWhile:
##      low=test
move  $t4, $t6
#then go back to while
j while

done:
#conditional to jump to found
mul   $t2, $t4, 4
add   $t2, $t2, $t0 #calculate the address of array[low]
lb    $t3, 0($t2) #loads the value of array[low] into t3
beq   $t3, $t7, found #arr[low], target, found
##else:
##  print "target not found in array"
li $v0, 4
la $a0, notFoundStr
syscall
j end

##if arr[low]==target:
found:
##  print "target found at index: " + low
li   $v0, 4
la   $a0, foundStr
syscall
move $a0, $t4 #put low (aka found index) to be printed
li   $v0, 1
syscall
j end

end:
li       $v0, 10
syscall  #end program