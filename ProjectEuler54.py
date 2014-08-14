#sys has exit method to stop program
import sys

def getNumOfEachRank(pokerHand):
    #store total number of each rank in the hand
    numOfEachRank = [0]*13
    
    for i in range(len(pokerHand)):
        if pokerHand[i]['rank'] == '2':
            numOfEachRank[0] += 1
        elif pokerHand[i]['rank'] == '3':
            numOfEachRank[1] += 1
        elif pokerHand[i]['rank'] == '4':
            numOfEachRank[2] += 1
        elif pokerHand[i]['rank'] == '5':
            numOfEachRank[3] += 1
        elif pokerHand[i]['rank'] == '6':  
            numOfEachRank[4] += 1      
        elif pokerHand[i]['rank'] == '7':
            numOfEachRank[5] += 1
        elif pokerHand[i]['rank'] == '8':
            numOfEachRank[6] += 1
        elif pokerHand[i]['rank'] == '9':
            numOfEachRank[7] += 1
        elif pokerHand[i]['rank'] == '10':
            numOfEachRank[8] += 1
        elif pokerHand[i]['rank'] == '11':
            numOfEachRank[9] += 1
        elif pokerHand[i]['rank'] == '12':
            numOfEachRank[10] += 1
        elif pokerHand[i]['rank'] == '13':
            numOfEachRank[11] += 1
        elif pokerHand[i]['rank'] =='14':
            numOfEachRank[12] += 1
        else:
            sys.exit("Error: invalid rank of card.")
    
    return numOfEachRank
            
def onePair(pokerHand):
    #return true if there is a pair in the deck
    for i in range(len(pokerHand)-1):
        for j in range(i+1,len(pokerHand)):
            if pokerHand[i]['rank'] == pokerHand[j]['rank']:
                return True
    
    return False

def twoPair(pokerHand):
    
    numOfEachRank = getNumOfEachRank(pokerHand)
    
    numSuitsWithMoreThanTwo = 0
    
    for i in range(len(numOfEachRank)):
        if numOfEachRank[i] >= 2:
            numSuitsWithMoreThanTwo += 1
        
    if numSuitsWithMoreThanTwo == 2:
        return True
    else:
        return False
    
def threeOfAKind(pokerHand):
    
    numOfEachRank = getNumOfEachRank(pokerHand)
    for num in numOfEachRank:
        if num == 3:
            return True
        
    return False

def fourOfAKind(pokerHand):
    
    numOfEachRank = getNumOfEachRank(pokerHand)
    print(numOfEachRank)
    for num in numOfEachRank:
        if num == 4:
            return True
        
    return False


def convertToListDictionary(pokerHandList):
        
    pokerHandListDict = []
    
    for i in range(len(pokerHandList)):
        pokerHandListDict.append({'suit':pokerHandList[i][1], 'rank':pokerHandList[i][0]})

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
def rankHand(pokerHand):
     High Card => rank = 1
        One Pair => rank = 2
        Two Pairs => rank = 3
        Three of a Kind => rank = 4
        Straight => rank = 5
        Flush => rank = 6
        Full House => rank = 7
        Four of a Kind => rank = 8
        Straight Flush => rank = 9
        Royal Flush => rank = 10
    
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

    
result = fourOfAKind([{'suit':'A','rank':'2'},{'suit':'A','rank':'10'},{'suit':'A','rank':'10'},{'suit':'A','rank':'10'},{'suit':'A','rank':'10'}])
print(result)

'''
    winner = playPoker(player1PokerHandListDict, player2PokerHandListDict)

    if winner == 1:
        numPlayer1Wins += 1
    elif winner == 2:
        numPlayer2Wins
    elif winner == -1:
        print('It\s a tie')
    else:
        print('Nobody won or tied? There\s a bug in the program!')
'''