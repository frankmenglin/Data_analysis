import numpy as np
import random

#We attempt to get a conversion table between dan/kyu type rating (rank) vs. ELO rating

Strength_Ave=1500 #The average ELO strength of all players
Strength_Std=400 #The standard deviation of strength of all players
start_rank=-9 #Assume everyone starts at 10kyu
Max_Rank=10 #Maximum possible rank
Min_Rank=-17 #Minimum possible rank
Number_of_Players=20000 #Number of players
Number_of_Games=20000000 #Number of Games played in simulation

#ELO win rate formula
def win_probability(Strength_A,Strength_B):
    return 1.0/(1.0+10.0**((Strength_B-Strength_A)/400.0))

#Dan/Kyu rating change rule
#The key is current rank, then the list contains information from left to right,
#number of games, number of win to promote, number of lose to demote
RankRule={-17:[10,6,999],-16:[10,6,7],-15:[10,6,7],-14:[12,7,8],-13:[12,7,8],
          -12:[12,7,8],-11:[14,8,10],-10:[14,8,10],-9:[14,8,10],-8:[16,10,11],
        -7:[16,10,11],-6:[16,10,11],-5:[16,10,11],-4:[18,11,12],-3:[18,11,12],
        -2:[18,11,12],-1:[19,12,13],0:[19,12,13],1:[19,12,13],2:[19,12,13],
        3:[20,14,13],4:[20,14,13],5:[20,15,13],6:[20,15,13],7:[20,15,13],
        8:[20,15,13],9:[20,18,13],10:[20,999,13]}

#update of a player's record after winning a game
def win_update(A):
    if len(A[2])<20:
        A[2]=A[2]+["w"]
    else:
        A[2]=A[2][1:]+["w"]
    num_of_game=RankRule[A[1]][0] #number of games when consider promotion/demotion
    if  A[2][(20-num_of_game):].count("w")>=RankRule[A[1]][1] and A[1]<Max_Rank:
        A[2]=[]
        A[1]=A[1]+1
    return A

#update of a player's record after losing a game
def lose_update(A):
    if len(A[2])<20:
        A[2]=A[2]+["l"]
    else:
        A[2]=A[2][1:]+["l"]
    num_of_game = RankRule[A[1]][0]  # number of games when consider promotion/demotion
    if A[2][(20-num_of_game):].count("l")>=RankRule[A[1]][2] and A[1]>Min_Rank:
        A[2]=[]
        A[1]=A[1]-1
    return A

#Create a nested list that store each player's rating, rank, and win/loss record

#In each sublist, index 0 stores ELO rating, index 1 stores rank, index 2 is a list that stores win/loss record

#If you print it out it looks like [[1543.12,0,["w","l","w"]],[1743.23,2,["w","l","l"]],......]
Players_data=[]
for i in range(Number_of_Players):
    Players_data=Players_data+[[np.random.normal(loc=Strength_Ave,scale=Strength_Std),start_rank,[]]]



Player_index=range(Number_of_Players)
i=0
while i<Number_of_Games:
    #randomly pick two players
    Players_of_game=random.sample(Player_index,k=2)
    Player_A=Players_of_game[0]
    Player_B=Players_of_game[1]

    #if they have the same rank, a game is played between them
    if Players_data[Player_A][1]==Players_data[Player_B][1]:
        match_result=random.uniform(0, 1)#uniform random number on (0,1)

        #update the win/loss record and rank
        if match_result<=win_probability(Players_data[Player_A][0],Players_data[Player_B][0]):
            Players_data[Player_A]=win_update(Players_data[Player_A])
            Players_data[Player_B]=lose_update(Players_data[Player_B])
        else:
            Players_data[Player_A]=lose_update(Players_data[Player_A])
            Players_data[Player_B]=win_update(Players_data[Player_B])
        i+=1



#Store the ratings of players in each rank
rank_rating={}
for i in range(Min_Rank,Max_Rank+1):
    rank_rating[i]=[]
for player in Players_data:
    rank_rating[player[1]]=rank_rating[player[1]]+[player[0]]

#Store the average rating of players in each rank
rank_rating_average={}
for i in range(Min_Rank,Max_Rank+1):
    if len(rank_rating[i])>0:
        rank_rating_average[i]=sum(rank_rating[i])/len(rank_rating[i])
    else:
        rank_rating_average[i]="N/A"

conversionfile = open('rating_conversion.txt', 'w')
for x,y in rank_rating_average.items():
    if int(x)>0:
        print("%sd %s" %(x,y), file = conversionfile)
    else:
        print("%sk %s" %(str(1-int(x)),y), file = conversionfile)
conversionfile.close()