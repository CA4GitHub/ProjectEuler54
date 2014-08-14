def convertToDictionary(pokerHandList):
        
    pokerHandDict = {}
    pokerHandListDict = []
    for i in range(len(pokerHandList)):
        pokerHandDict['rank'] = pokerHandList[i][0]
        pokerHandDict['suit'] = pokerHandList[i][1]
        pokerHandListDict.append(pokerHandDict)

    print(pokerHandListDict)
    return pokerHandDict


pokerFile = open('poker.txt', encoding = 'utf-8')

numPlayer1Wins = 0
numPlayer2Wins = 0

for line in pokerFile:

    aPokerHand = (line.rstrip()).split(' ')
    
    player1PokerHandList = aPokerHand[0:5]
    player2PokerHandList = aPokerHand[5:10]
  
    player1PokerHandDict = convertToDictionary(player1PokerHandList)
    player2PokerHandDict = convertToDictionary(player2PokerHandList)
'''    
    winner = playPoker(player1PokerHandDict, player2PokerHandDict)
    '''