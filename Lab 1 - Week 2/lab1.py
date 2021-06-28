#CS:2630 Computer Organization Summer 2021: Lab 1.
#author: Annika Heiling 
#date: 6/27/21

#1: accepts string of 1s&0s in unsigned int rep, converts to base 10.
def binToBase10(bin):
  binArr = list(bin)
  decSum = 0
  i=0
  while i < len(binArr):
    #if exists 1 in the position add its places' power of 2 to the sum
    if binArr[-(i+1)] == "1":
      decSum += (2**i)
    i += 1
  return decSum
#TESTS:
 # binToBase10("011") # output: 3
 # binToBase10("000011001") # output: 25
 # binToBase10("10101010") # output: 170

#2: accepts some int in base 10, outputs equivalent unsigned int rep in base 2
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
    return("overflow error")
  else: #add 0s to beginning, if needed to reach bitLen. add sign.
    while len(bin) < bitLen:
      bin = "0"+bin
    bin = sign+bin
    return bin
#TESTS:
 # print(base10ToBin(3,8)) # should give "+00000011"
 # print(base10ToBin(+32,8)) # should give "+00100000"
 # print(base10ToBin(-32,8)) #should give "-00100000"
 # print(base10ToBin(-32, 4)) #should give overflow error

#3: accepts string of 1s&0s in insigned int rep, converts to ONE's complement
def binToOnes(bin):
  if bin[0] == "+":
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
  return ones
#TESTS:
 # binToOnes("+00011100") # output: "00011100"
 # binToOnes("-00011100") # output: "11100011"
 # binToOnes("-11101010") # output: "00010101" says overflow, but think it was mistake

#4: accepts string of 1s&0s in unsigned int rep, converts to TWO's complement
def binToTwos(bin):
  twos = ""
  if bin[0] == "+":
    return bin[1:]
  else:
    ones = binToOnes(bin)
    onesLen = len(ones)
    addedBit = 1
    i=-1
    while addedBit: #while there remains a bit to be added,
      try: # attempt to add the 1 
        if ones[i] == "0":
          twos = ones[:i] + "1"
          twos += (onesLen - len(twos))*"0"
          addedBit = 0
          break
        i-=1
      except: #if the addition makes it overflow, error
        return("overflow error")
    return twos
#TESTS:
 # binToTwos("+00011100")#output: "00011100"
 # binToTwos("-00011100")#ones: 11100011 output: "11100100"
 # binToTwos("-11101010")#ones: 00010101 output: overflow error?? should be 00010110.
 # binToTwos("00000000")#ones: 11111111 output: overflow error (1 00000000)

#5: accepts POS decimal, outputs rounded to CEILING. the only ineq op is <= 0.
def decToCeiling(num):
  ops = 1
  while (ops-num) <= 0:
    ops += 1
    if ops == num:
      return num
  return ops
#TESTS:
 # decToCeiling(2) #should give 2
 # decToCeiling(32.11) #should give 33
 # decToCeiling(13.0011) #should give 14
 # decToCeiling(0.09) #should give 1

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
  return rng
#TESTS:
 # rangeOfThree(2,8,5) #should give 6
 # rangeOfThree(1,2,3) #should give 2
 # rangeOfThree(8,2,9) #should give 7