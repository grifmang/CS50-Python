def badCredit(cc):
    sumList = []
    ccCopy = str(cc)
    sumNum = 0
    sumForward = 0

    # Validate provider
    if ccCopy.startswith('37') == True or ccCopy.startswith('34') == True and len(ccCopy) == 15:
        provider = "AMEX"
    elif ccCopy.startswith('4') == True:
        if len(ccCopy) != 13 or len(ccCopy) != 16:
            print "INVALID"
            return "INVALID"
        else:
            provider = "VISA"
    elif ccCopy.startswith('51') == True or ccCopy.startswith('52') == True or ccCopy.startswith('53') == True or ccCopy.startswith('54') == True or ccCopy.startswith('55') == True and len(ccCopy) == 16:
        provider = "MASTERCARD"
    else:
        print "INVALID"
        return "INVALID"

    # Multiply every other digit starting with second to last
    for i in ccCopy[-2::-2]:
        sumList.append(int(i) * 2)

    # Make list one string
    sumString = (str(i) for i in sumList)
    sumString = ''.join(sumString)

    # Add all digits
    for i in sumString:
        sumNum += int(i)

    # Add sumNum to the sum of the unused digits in cc
    for i in ccCopy[0::2]:
        sumForward += int(i)

    sumForward += sumNum

    print provider
