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

def getNumOfEachSuit(pokerHand):
    
    #store total number of each suit in the hand
    numOfEachSuit = [0]*4
    for i in range(len(pokerHand)):
        if pokerHand[i]['suit'] == 'C':
            numOfEachSuit[0] += 1
        elif pokerHand[i]['suit'] == 'D':
            numOfEachSuit[1] += 1
        elif pokerHand[i]['suit'] == 'H':
            numOfEachSuit[2] += 1
        elif pokerHand[i]['suit'] == 'S':
            numOfEachSuit[3] += 1
        else:
            sys.exit("Error: invalid suit of card.")
    
    return numOfEachSuit
            
def onePair(pokerHand):
    #return true if there is a pair in the deck
    
    numOfEachRank = getNumOfEachRank(pokerHand)
    
    for num in numOfEachRank:
        if num == 2:
            return True
        
    return False

def twoPairs(pokerHand):
    #return true if there are two pairs in the deck
    
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
    #return true if there are 3 card of the same rank in the deck
    
    numOfEachRank = getNumOfEachRank(pokerHand)
    for num in numOfEachRank:
        if num == 3:
            return True
        
    return False

def straight(pokerHand):
    #return true if the hand has a straight
    
    rankList = [int(pokerHand[i]['rank']) for i in range(len(pokerHand))]
    rankList.sort()
    
    for i in range(len(rankList)-1):
        
        if (rankList[i] + 1) != rankList[i+1]:
            return False
    
    return True

def flush(pokerHand):
    #return true if all cards in the hand have the same suit
    
    numOfEachSuit = getNumOfEachSuit(pokerHand)
    for i in range(len(numOfEachSuit)):
        if numOfEachSuit[i] == 5:
            return True
    
    return False

def fullHouse(pokerHand):
    #return true if there is a pair and a three of a kind
    
    if onePair(pokerHand) and threeOfAKind(pokerHand):
        return True
    
    return False

def fourOfAKind(pokerHand):
    #return true if there are 4 cards with the same rank in the hand
    
    numOfEachRank = getNumOfEachRank(pokerHand)

    for num in numOfEachRank:
        if num == 4:
            return True
        
    return False

def straightFlush(pokerHand):
    #return true if the hand is a straight and a flush
    
    if flush(pokerHand) and straight(pokerHand):
        return True
    
    return False

def royalFlush(pokerHand):
    #return true if the hand is a straight flush and contains an 'A'
    
    rankList = []

    for i in range(len(pokerHand)):
        rankList.append(int(pokerHand[i]['rank']))      
    
    #if straightFlush contains an 'A' (e.g. rank '14'), it's a royal flush
    if straightFlush(pokerHand) and (14 in rankList):
        return True
    else:
        pass
    
    return False

def convertToListDictionary(pokerHandList):
    #turn the pokerHandList into a list where each element is a dictionary with keys 'suit' and 'rank'
        
    pokerHandListDict = []
    
    for i in range(len(pokerHandList)):
        pokerHandListDict.append({'suit':pokerHandList[i][1], 'rank':pokerHandList[i][0]})
    
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
    
    return pokerHandListDict

def getHighCard(pokerHandListDict):
    #returns the numeric rank of the high card in the hand
    
    highCard = 0
    for i in range(len(pokerHandListDict)):
        if int(pokerHandListDict[i]['rank']) > highCard:
            highCard = int(pokerHandListDict[i]['rank'])
           
    return highCard        

def compareHighCards(player1PokerHandListDict,player2PokerHandListDict):
    #returns the winner corresponding to the player with the high card or a tie
    
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

def compareHighCardUsed(player1PokerHandListDict,player2PokerHandListDict,handRank):
    # Called if the players hands have the same rank, this method considers the rank of the hand
    # and decides the winner based on the high cards in the hand.
    
    if handRank == 10: #case royal flush
        #always a tie
        winner = -1
        
    elif handRank == 9: #case royal straight
        #high card wins
        winner = compareHighCards(player1PokerHandListDict,player2PokerHandListDict)
        
    elif handRank == 8: #case four of a kind
        numOfEachRank1 = getNumOfEachRank(player1PokerHandListDict)
        numOfEachRank2 = getNumOfEachRank(player2PokerHandListDict)
        index1 = numOfEachRank1.index(4)
        index2 = numOfEachRank2.index(4)
        if index1 > index2:
            winner = 1
        elif index2 > index1:
            winner = 2
        else:
            winner = -1
            
    elif handRank == 7: #case full house
        #high card wins
        winner = compareHighCards(player1PokerHandListDict,player2PokerHandListDict)
        
    elif handRank == 6: #case flush
        #high card wins
        winner = compareHighCards(player1PokerHandListDict,player2PokerHandListDict)
        
    elif handRank == 5: #case straight
        #high card wins
        winner = compareHighCards(player1PokerHandListDict,player2PokerHandListDict)
        
    elif handRank == 4: #case three of a kind
        numOfEachRank1 = getNumOfEachRank(player1PokerHandListDict)
        numOfEachRank2 = getNumOfEachRank(player2PokerHandListDict)
        #find where there are 3 of a kind
        index1 = numOfEachRank1.index(3)
        index2 = numOfEachRank2.index(3)
        if index1 > index2:
            winner = 1
        elif index2 > index1:
            winner = 2
        else:
            winner = -1
            
    elif handRank == 3: #twoPairs case
        numOfEachRank1 = getNumOfEachRank(player1PokerHandListDict)
        numOfEachRank2 = getNumOfEachRank(player2PokerHandListDict)
        numOfEachRank1 = 0
        numOfEachRank2 = 0
        maxPairIndices1 = []
        maxPairIndices2 = []
        for i in range(len(numOfEachRank1)):
            if numOfEachRank1[i]==2:
                maxPairIndices1.append(i)
            if numOfEachRank2[i]==2:
                maxPairIndices2.append(i)
        
        for i in range(len(maxPairIndices1)-1,-1,-1):
            if  maxPairIndices1[i] > maxPairIndices2[i]:
                winner = 1
                break
            if  maxPairIndices2[i] > maxPairIndices1[i]:
                winner = 2
                break
            
            #if we've checked the pairs are the same
            if i == 0 and maxPairIndices1[i]==maxPairIndices2[i]:
                #in this case the max card will be the 1 unused card
                maxNonUsedCardIndex1 = numOfEachRank1.index(1)
                maxNonUsedCardIndex2 = numOfEachRank2.index(1)
                
                if maxNonUsedCardIndex1 > maxNonUsedCardIndex2:
                    winner = 1
                elif maxNonUsedCardIndex2 > maxNonUsedCardIndex1:
                    winner = 2
                else:
                    winner = -1
            
    elif handRank == 2: #onePair case
        numOfEachRank1 = getNumOfEachRank(player1PokerHandListDict)
        numOfEachRank2 = getNumOfEachRank(player2PokerHandListDict)
        index1 = numOfEachRank1.index(2)
        index2 = numOfEachRank2.index(2)
        
        if index1 > index2:
            winner = 1
        elif index2 > index1:
            winner = 2
        else: #check cards not in the one pair
            index1OfHighCardNotUsed = 0
            index2OfHighCardNotUsed = 0
            for i in range(len(numOfEachRank1)):
                if i != index1:
                    if numOfEachRank1[i] > 0:
                        index1OfHighCardNotUsed = i
                    if numOfEachRank2[i] > 0:
                        index2OfHighCardNotUsed = i
            if index1OfHighCardNotUsed > index2OfHighCardNotUsed:
                winner = 1
            elif index2OfHighCardNotUsed > index1OfHighCardNotUsed:
                winner = 2
            else:
                winner = -1
            
    elif handRank == 1: #case high card
        #high card wins
        winner = compareHighCards(player1PokerHandListDict,player2PokerHandListDict)
 
    else:
        sys.exit('Error: invalid hand rank.')
        
    return winner

def rankHand(pokerHand):
    '''High Card => rank = 1
        One Pair => rank = 2
        Two Pairs => rank = 3
        Three of a Kind => rank = 4
        Straight => rank = 5
        Flush => rank = 6
        Full House => rank = 7
        Four of a Kind => rank = 8
        Straight Flush => rank = 9
        Royal Flush => rank = 10'''
    
    #initialize rank
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
    #returns the winner of a game of poker between 2 hands
    
    player1HandRank = rankHand(player1PokerHandListDict)
    player2HandRank = rankHand(player2PokerHandListDict)
    
    if player1HandRank == player2HandRank:
        winner = compareHighCardUsed(player1PokerHandListDict,player2PokerHandListDict, player1HandRank)
        #winner = compareHighCards(player1PokerHandListDict,player2PokerHandListDict)
    elif player1HandRank > player2HandRank:
        winner = 1
    else:
        winner = 2

    return winner

#main part of code
pokerFile = open('poker.txt', encoding = 'utf-8')

#initialize variables
numPlayer1Wins = 0
numPlayer2Wins = 0
ties = 0
games = 0

for line in pokerFile:
    games +=1
    print('This is poker game number {}.'.format(games))
    aPokerHand = (line.rstrip()).split(' ')
    
    player1PokerHandList = aPokerHand[0:5]
    player2PokerHandList = aPokerHand[5:10]
  
    player1PokerHandListDict = convertToListDictionary(player1PokerHandList)
    player2PokerHandListDict = convertToListDictionary(player2PokerHandList)
    print('Player1\'s hand:')
    print(player1PokerHandListDict)
    print('Player2\'s hand:')
    print(player2PokerHandListDict)
    
    winner = playPoker(player1PokerHandListDict, player2PokerHandListDict)

    if winner == 1:
        numPlayer1Wins += 1
        print('P1 wins')
    elif winner == 2:
        numPlayer2Wins += 1
        print('P2 wins')
    elif winner == -1:
        ties += 1
        print('It\s a tie')
    else:
        print('Nobody won or tied? There\s a bug in the program!')
        
print('Player1 won {0} hands, and Player2 won {1} hands. And there were {2} ties.'.format(numPlayer1Wins,numPlayer2Wins,ties))

