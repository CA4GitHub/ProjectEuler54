def convertToListDictionary(pokerHandList):
        
    pokerHandDict = {}
    pokerHandListDict = []
    
    for i in range(len(pokerHandList)):
        pokerHandListDict.append({'suit':pokerHandList[i][1], 'rank':pokerHandList[i][0]})

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

def rankHand(pokerHand):
    ''' High Card => rank = 1
        One Pair => rank = 2
        Two Pairs => rank = 3
        Three of a Kind => rank = 4
        Straight => rank = 5
        Flush => rank = 6
        Full House => rank = 7
        Four of a Kind => rank = 8
        Straight Flush => rank = 9
        Royal Flush => rank = 10
    '''
    rank = -1
    if royalFlush(pokerHand):
        rank = 10
    elif straightFlush(pokerHand):
        rank = 9
    elif fourOfAKind(pokerHand):
        rank = 8
    elif fullHouse(pokerHand):
        rank = 7
    elif flush(pokerHand):
        rank = 6
    elif straight(pokerHand):
        rank = 5
    elif threeOfAKind(pokerHand):
        rank = 4
    elif twoPairs(pokerHand):
        rank = 3
    elif onePair(pokerHand):
        rank = 2
    else:
        rank = 1
        
    return rank

def playPoker(player1PokerHandListDict, player2PokerHandListDict):
    
    player1HandRank = rankHand(player1PokerHandDict)
    player2HandRank = rankHand(player2PokerHandDict)
    
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
    rank = rankHand(player1PokerHandListDict)
'''    winner = playPoker(player1PokerHandListDict, player2PokerHandListDict)
    if winner == 1:
        numPlayer1Wins += 1
    elif winner == 2:
        numPlayer2Wins
    elif winner == -1:
        print('It\s a tie')
    else:
        print('Nobody won or tied? There\s a bug in the program!')
'''