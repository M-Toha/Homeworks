## Practice

'''1. 
    1. Write a program that generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
    2. To each file append a random number between 1 and 100.
    3. Create a summary file (summary.txt) that contains name of the file and number in that file:

        A.txt: 67

        B.txt: 12

        ...
        
        Z.txt: 98

'''
import random as r
for i in range (ord('A'), ord('Z')+1):
    with open(f'{chr(i)}.txt', 'w') as file:
        file.write(str(r.randint(1, 100)))
with open('summary.txt', 'w') as summary:
    for i in range (ord('A'), ord('Z')+1):
        with open (f'{chr(i)}.txt', 'r') as file:
            summary.write(f'{chr(i)}.txt: {file.read()}\n')

'''
2. 
    1. Create file with some content. As example you can take this one
    ```
        Тому що ніколи тебе не вирвеш,
        ніколи не забереш,
        тому що вся твоя свобода
        складається з меж,
        тому що в тебе немає
        жодного вантажу,
        тому що ти ніколи не слухаєш,
        оскільки знаєш і так,
        що я скажу,
    ```
    2. Create second file and copy content of the first file to the second file in upper case.
'''
with open('poem.txt', 'w', encoding='utf-8') as poem:
    poem.write('Тому що ніколи тебе не вирвеш,\n\
ніколи не забереш,\n\
тому що вся твоя свобода\n\
складається з меж,\n\
тому що в тебе немає\n\
жодного вантажу,\n\
тому що ти ніколи не слухаєш,\n\
оскільки знаєш і так,\n\
що я скажу,')
with open('poem_copy.txt', 'w', encoding='utf-8') as copy, open('poem.txt', 'r', encoding='utf-8') as poem:
    copy.write(poem.read().upper())

'''
3. Write a program that will simulate user score in a game. 
    Create a list with 5 player's names. 
    After that simulate 100 games for each player. 
    As a result of the game create a list with player's name and his score (0-1000 range). 
    And save it to a CSV file. File should looks like this:
    ```
    Player name, Score
    Josh, 56
    Luke, 784
    Kate, 90
    Mark, 125
    Mary, 877
    Josh, 345
    ...
    ```
'''
import csv
player_list = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']
Score_list = []
for i in range (0, 100):
    for player_name in player_list:
        Score_list.append([player_name, r.randint(0, 1000)])
with open('Players_score.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Player name', 'Score'])
    writer.writerows(Score_list)

'''
4. Write a script that reads the data from previous CSV file and creates a new file called 
high_scores.csv where each row contains the player name and their highest score. 
Final score should sorted by descending of highest score

The output CSV file should look like this:

    
    Player name, Highest score
    Kate, 907
    Mary, 897
    Luke, 784
    Mark, 725
    Josh, 345'''


with open('Players_score.csv', mode='r') as file:
    reader = csv.reader(file)
    Scorelist = {i:[] for i in player_list}
    for row in reader:
        if row[0] in player_list:
            Scorelist[row[0]].append(row[1])
    Highscorelist = [[i, max(Scorelist[i])] for i in player_list]

with open('Players_highscore.csv', mode='w', newline='') as file1:
    writer = csv.writer(file1)
    writer.writerow(['Player name', 'Highest score'])
    writer.writerows(sorted(Highscorelist, key = lambda x: x[1], reverse = True))

