def convertToListDictionary(pokerHandList):
        
    pokerHandDict = {}
    pokerHandListDict = []
    for i in range(len(pokerHandList)):
        pokerHandDict['rank'] = pokerHandList[i][0]
        pokerHandDict['suit'] = pokerHandList[i][1]
        pokerHandListDict.append(pokerHandDict)

    print(pokerHandListDict)
    return pokerHandListDict

def getHighCard(pokerHandListDict):
    highCard = 0
    for i in range(len(pokerHandListDict)):
        if pokerHandListDict[i]['rank'] == 'T':
            pokerHandListDict[i]['rank'] = '10'
        elif pokerHandListDict[i]['rank'] == 'J':
            pokerHandListDict[i]['rank'] = '11'
        elif pokerHandListDict[i]['rank'] == 'Q':
            pokerHandListDict[i]['rank'] = '12'
        elif pokerHandListDict[i]['rank'] == 'K':
            pokerHandListDict[i]['rank'] = '13'
        elif pokerHandListDict[i]['rank'] == 'A':
            pokerHandListDict[i]['rank'] = '14'
        else:
            #not a face card
            pass
        
        if int(pokerHandListDict[i]['rank']) > highCard:
            highCard = int(pokerHandListDict[i]['rank'])
           
    return highCard
        

def compareHighCards(player1PokerHandListDict,player2PokerHandListDict):
    player1HighCard = getHighCard(player1PokerHandListDict)
    player2HighCard = getHighCard(player2PokerHandListDict)
    if player1HighCard > player2HighCard:
        winner = 1
    elif player2HighCard > player1HighCard:
        winner = 2
    else:
        #it's a tie
        winner = -1
    
    return winner
'''
def playPoker(player1PokerHandDict, player2PokerHandDict):
    
    player1HandRank = getRankedHand(player1PokerHandDict)
    player2HandRank = getRankedHand(player2PokerHandDict)
    
    if player1HandRank == player2HandRank:
        winner = compareHighCards(player1PokerHandDict,player2PokerHandDict)
    elif player1HandRank > player2HandRank:
        winner = 1
    else:
        winner = 2

    return winner
'''
pokerFile = open('poker.txt', encoding = 'utf-8')

numPlayer1Wins = 0
numPlayer2Wins = 0

for line in pokerFile:

    aPokerHand = (line.rstrip()).split(' ')
    
    player1PokerHandList = aPokerHand[0:5]
    player2PokerHandList = aPokerHand[5:10]
  
    player1PokerHandListDict = convertToListDictionary(player1PokerHandList)
    player2PokerHandListDict = convertToListDictionary(player2PokerHandList)
    winner = compareHighCards(player1PokerHandListDict,player2PokerHandListDict)
    
'''    winner = playPoker(player1PokerHandDict, player2PokerHandDict)
    if winner == 1:
        numPlayer1Wins += 1
    elif winner == 2:
        numPlayer2Wins
    elif winner == -1:
        print('It\s a tie')
    else:
        print('Nobody won or tied? There\s a bug in the program!')
'''