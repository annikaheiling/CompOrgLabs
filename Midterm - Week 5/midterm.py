#CS:2630 Computer Organization Summer 2021: Midterm
#author: Annika Heiling 
#date: 7/15/2021

#1A: takes unsigned base-2 number as string (lead with a decimal point). outputs 
# rep in base-10.
def dec2To10(b2dec):
  binArr = list(b2dec[1:])
  decSum = 0
  i = 0
  while i < len(binArr):
    #if exists 1 in the position add its places' power of 2 to the sum
    if binArr[i] == "1":
      decSum += (2**(-(i+1)))
    i += 1
  print(decSum)
  return decSum
dec2To10(".100") # Output: .5
dec2To10(".101") # Output: .625
dec2To10(".1101") # Output: .8125

#1B: takes some fraction in decimal form & bit-length. outputs rep in unsigned base-2 
# (restricted to the bit-length).
def dec10to2(dec, bitLen):
  bin = ""
  while dec != 0:
    if len(bin) == bitLen:
      break
    dec = dec*2
    if dec >= 1:
      dec -= 1
      bin += "1"
    else:
      bin += "0"
  while len(bin) < bitLen:
    bin += "0"
  bin = "." + bin
  print(bin)
  return bin
dec10to2(.625, 4) # Input1: .625; Input2: 4; Output:.1010
dec10to2(.81252, 4) # Input1: .81252; Input2: 4; Output: .1101
dec10to2(.81252, 2) # Input1: .81252; Input2: 2; Output: .11
dec10to2(.81252, 3) # Input1: .81252; Input2: 3; Output: .110