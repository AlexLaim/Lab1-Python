import random
import itertools
import datetime

teamList = [
        'Команда 1','Команда 2','Команда 3','Команда 4',
        'Команда 5','Команда 6','Команда 7','Команда 8',
        'Команда 9','Команда 10','Команда 11','Команда 12',
        'Команда 13','Команда 14','Команда 15','Команда 16',
    ]

groups = []
end = 15

for i in range(4):
    groups.append([])
    for j in range(4):
        team = random.randint(0,end)
        groups[i].append(teamList[team])
        teamList.pop(team)
        end -=1
            
    
date_game_start = datetime.datetime(2023, 9, 14, 22, 45)

i = 0
for group in groups:
    print("Группа : " + str(group) + "\n")
    games = itertools.permutations(group, 2)
    for game in games:
        if i!=0:
            date_game_next = datetime.timedelta(days=14)
            date_game = date_game_start+date_game_next
            date_game_start = date_game
        i = 1
        print("Дата игры: " + date_game_start.strftime("%d/%m/%Y, %H:%M")+ "\n" + str(game[0]) + " против " + str(game[1]) + "\n")