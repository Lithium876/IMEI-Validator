luhnsTable = {0:0, 1:2, 2:4, 3:6, 4:8, 5:1, 6:3, 7:5, 8:7, 9:9}

def nextTen(checkSum):
	# Finding the next 10
	nextTenth = checkSum
	while 1:
		if nextTenth%10 == 0:
			break
		else:
			nextTenth = nextTenth + 1

	return nextTenth

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

	return checkSum

def ValidateIMEI(number, posistion=None):

	if len(number) < 15:
		return "IMEI too short"
	elif len(number) > 15:
		return "IMEI too long"

	checkDigit = int(number[-1]) #get the last digit in number
	checkSum = 0
	# print(number)

	if posistion is None:
		checkSum = calculateCheckSum(number, len(number)-1)
	else:
		checkSum = calculateCheckSum(number, len(number))


	nextTenth = nextTen(checkSum)
	magic = nextTenth - checkSum 
	# print("Check Sum:",checkSum)
	# print("Next ten:", nextTenth)
	# print(nextTenth,"-",checkSum,"=",magic)

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

# value = ValidateIMEI("864224026430067") #missing 8

# print(value)