def convertToDictionary(pokerHandList):
    pokerHandDict = {}
    for card in pokerHandList:
        pokerHandDict['rank'] = card[0]
        pokerHandDict['suit'] = card[1]
        print('The rank is {0} and the suit is {1}'.format(pokerHandDict['rank'],pokerHandDict['suit']))

pokerFile = open('poker.txt', encoding = 'utf-8')
for line in pokerFile:

    aPokerHand = (line.rstrip()).split(' ')
    player1PokerHandList = aPokerHand[0:4]
    player2PokerHandList = aPokerHand[5:9]
    player1PokerHandDict = convertToDictionary(player1PokerHandList)
    