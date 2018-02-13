def calculateCheckSum(number, val):
	checkSum = 0
	#loop up to the second to last number in number
	for i in range(val):
		#if posistion is even, get the luhns value 
		if i%2!=0:
			value = luhnsTable[int(number[i])]
			checkSum = checkSum + value
		#else use original value
		else:
			checkSum = checkSum + int(number[i])

def ValidateIMEI(number, posistion=None):

	if len(number) < 15:
		return "IMEI too short"
	elif len(number) > 15:
		return "IMEI too long"

	checkDigit = int(number[-1]) #get the last digit in number
	checkSum = 0

	if posistion is None:
		checkSum = calculateCheckSum(number, len(number)-1)
	else:
		checkSum = calculateCheckSum(number, len(number))

	nextTenth = nextTen(checkSum)
	magic = nextTenth - checkSum 
  
	if posistion is not None:
		if posistion%2==0:
			value = [k for k, v in luhnsTable.items() if v == magic][0]
			return "The missing value is " + str(value)
		else:
			return "The missing value is " + str(magic)
	elif magic == checkDigit:
		return "Valid IMEI"
	else:
		return "Invalid IMEI"

if __name__ == '__main__':
	valueA = ValidateIMEI("864224026430067") 
	valueB = ValidateIMEI("064224026430067", 1) # missing first value 8
	print(valueA)
	print(valueB)
