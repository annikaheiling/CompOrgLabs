#binary to two's complement
#x = [x__1, x__2, ... x0] #b2Tw(x) = -x__1 * 2 ^ w-1  + sigma(w-2 i=0 xi 2^i)

#1: a func that accepts a string of 1s and 0s (ie, 0001110001) in 
#unsigned int rep and converts to base 10. no casting!
def binToBase10(bin):
  binArr = list(bin)
  binArr.reverse() #FIX: do w/o reversal, make binArr from R instead of L
  decSum = 0
  i=0
  while i < len(binArr):
    #if 1 in the position add the power of 2 to the sum, else continue
    if binArr[i] == "1":
      decSum += (2**i)
    i += 1
  print (decSum)
#Tests:
#binToBase10("011") # output: 3
#binToBase10("000011001") # output: 25
#binToBase10("10101010") # output: 170

#2: a func that accepts some int in base 10 (ie, 32) and outputs
#its equivalent unsigned int rep in base-2
def base10ToBin(dec, bitLen):
  bin = "+"
  if dec < 0:
    bin = "-"
    dec *= -1

  powers = []
  i=0
  #compare to increasing powers of 2 until find one that is >= the number.
  while i < dec: #FIX: gotta be smth better here but oh well
    if (2**i) > dec:
      break #does it break the while? FIX: how to break the while
    else: 
      powers.append(2**i)
      i += 1
  for power in reversed(powers):
    if dec >= power:
      bin += "1"
      rem = dec % power
      dec = rem
    else: 
      bin += "0"
  print(bin)
  #FIX: if length of bin is smaller than bitLen, add the difference in 0s to the front but after the sign...
  #if len(bin) > bitLen: #FIX: it just don't work
    #FIX: should I j print a message of my own, or do smth with the error class?
  pass
base10ToBin(3,8) #3 should give "+00000011"
base10ToBin(35,8)
base10ToBin(-32, 4) #should give overflow error

#3: a func that accepts string of 1s and 0s in insigned int rep and 
#converts to one's complement
def binToOnes(bin):
  if bin[0] == "+":
    print(bin[1:])
    return bin[1:]
  else:
    ones = ""
    i=1
    while i < len(bin):
      if bin[i] == "1":
        ones += "0"
      else:
        ones += "1"
      i += 1
  print (ones)
  return ones
#binToOnes("+00011100") # output: "00011100"
#binToOnes("-00011100") # output: "11100011"

#4: a func that accepts string of 1s and 0s in unsigned int rep and
#converts to two's complement (so, one's, and then add 1 to the binary)
def binToTwos(bin):
  if bin[0] == "+":
    print(bin[1:])
    return bin[1:]
  else:
    twos = ""
    binToOnes(bin)
    #OR FIX: could I just... take the bin, convert to dec, add one to the dec, convert that to binary, return that?
  pass

#5: a func that accepts some decimal value and outputs value rounded to the CEILING.
#don't use round() obviously. also, no inequality operators (> or <). 
#instead, use a loop and the equality operator (==) and arithmetic.
#ie, accepts 13.0011 and returns 14. 
#NOTE: Don't cast as a string and split on decimal. Use arithmetic operations only
def decimalToCeiling(num):

  pass
decimalToCeiling(32.11) #should give 33

#6: a func that takes 3 POSITIVE numbers and returns the range
#don't use any inbuilt func - or inequality operators (> or <).
def rangeOfThree(num1, num2, num3):

  pass
rangeOfThree(1,2,3) #should give 2
rangeOfThree(2,8,5) #should give 6