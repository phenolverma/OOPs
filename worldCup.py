'''
WAP to create a world cup team :
1. Print All the players in indian team
2. Print all the players in Australian team
3. Find Total no of players in India as well as AUS
4. Print total no of players playing worldcup
'''
class team(object):
    def __init__(self,*players):
        self.players=players
    def __str__(self):
        allPlayers=''
        for player in self.players:
            allPlayers=allPlayers+' '+player
        return allPlayers
    def __len__(self):
        allPlayers=0
        for x in self.players:
            allPlayers+=1
        return allPlayers
    def __add__(self, other):
        allPlayers=''
        for player in self.players:
            allPlayers=allPlayers+' '+player
        for player in other.players:
            allPlayers=allPlayers+' '+player
        return allPlayers

india=team('Dhoni','Kohli','Sharma')
australia=team('Lee','Smith','ABCK','Mcgrath')

print 'Players of india are : {} '.format(india)
print 'PLayers of AUS are :{}'.format(australia)
print 'Total Players in India are {}'.format(len(india))
print 'Total Players in Australia are {}'.format(len(australia))
print 'Players in India and Australia are {}'.format(india+australia)
