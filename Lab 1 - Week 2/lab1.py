#BEFORE TURN IN: delete all print statements?
#1: DONE.
#2: DONE.
#3: DONE? but ask about the 'overflow' issue.
#4: DONE? but again, ask about 'overflow'...
#5: not a clue.
#6: DONE.

#1: accepts string of 1s&0s in unsigned int rep, converts to base 10.
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
  print ("binary: "+str(bin)+", base10: "+str(decSum)) #DELETE. uncomment line below for turn-in.
  #print(decSum)
  return decSum
#TESTS:
# binToBase10("011") # output: 3
# binToBase10("000011001") # output: 25
# binToBase10("10101010") # output: 170

#2: accepts some int in base 10, outputs equivalent unsigned int rep in base-2
def base10ToBin(dec, bitLen):
  bin = ""
  sign = "+"
  if dec < 0:
    sign = "-"
    dec *= -1

  powers = []
  i=0
  #compare to increasing powers of 2 until find one that is >= the number.
  while i < dec: #FIX: gotta be smth better here but oh well
    if (2**i) > dec:
      break
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
  if len(bin) > bitLen:
    #FIX: should I j print a message of my own, or do smth with the error class?
    print("overflow error")
  else: #add 0s to beginning, if needed to reach bitLen. add sign.
    while len(bin) < bitLen:
      bin = "0"+bin
    bin = sign+bin
    print(bin)
    return bin
#TESTS:
# base10ToBin(3,8) # should give "+00000011"
# base10ToBin(+32,8) # should give "+00100000"
# base10ToBin(-32,8) #should give "-00100000"
# base10ToBin(-32, 4) #should give overflow error

#3: accepts string of 1s&0s in insigned int rep, converts to ONE's complement
def binToOnes(bin):
  if bin[0] == "+":
    #print(bin[1:])
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
  #print (ones)
  return ones
#TESTS:
# binToOnes("+00011100") # output: "00011100"
# binToOnes("-00011100") # output: "11100011"
# binToOnes("-11101010") # output: says overflow, but I think it was mistake
# FIX: ask about the overflow issue. how would one get that from this conversion?

#4: accepts string of 1s&0s in unsigned int rep, converts to TWO's complement
def binToTwos(bin):
  twos = ""
  if bin[0] == "+":
    print(bin[1:])
    return bin[1:]
  else:
    ones = binToOnes(bin)
    onesLen = len(ones)
    addedBit = 1
    i=-1
    while addedBit: #while there remains a bit to be added,
      try:
        if ones[i] == "0":
          twos = ones[:i] + "1"
          twos += (onesLen - len(twos))*"0"
          addedBit = 0
          break
        i-=1
      except:
        print("overflow error")
        return 0
    print("twos: "+str(twos))
    return twos
#TESTS:
# binToTwos("+00011100")#output: "00011100"
# binToTwos("-00011100")#ones: 11100011 output: "11100100"
# binToTwos("-11101010")#ones: 00010101 output: overflow error?? why not 00010110?
# FIX: but is that ^ really overflow? why?? isn't it just 00010110? same amt digits...
# binToTwos("00000000")#ones: 00010101 output: overflow error

#5: accepts POS decimal value, outputs value rounded to the CEILING.
#the only inequality operator is <= 0. can use a loop, the equality operator (==), and arithmetic.
#can't cast as a string and split on decimal.
def decToCeiling(num):
#essentially we want to see if any numb after the . is >0, if so, delete it and all after it and add 1?

  pass
#TESTS:
decToCeiling(32.11) #should give 33
decToCeiling(13.0011) #should give 14
decToCeiling(0.09) #should give 1

#6: a func that takes 3 POS numbers, returns range. only ineq operator is <= 0.
def rangeOfThree(num1, num2, num3):
#find each difference
  diffs = [num1 - num2, num1 - num3, num2 - num3]
#make them all positive
  i=0
  for num in diffs:
    if num <= 0:
      num *= -1
      diffs[i] = num
    i+=1
#compare them all to find the biggest
  rng = diffs[0]
  if rng-diffs[1] <= 0:
    rng = diffs[1]
  if rng-diffs[2] <= 0:
    rng = diffs[2]
  print(rng)
  return rng
#TESTS:
# rangeOfThree(2,8,5) #should give 6
# rangeOfThree(1,2,3) #should give 2
# rangeOfThree(8,2,9) #should give 7