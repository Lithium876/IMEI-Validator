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
