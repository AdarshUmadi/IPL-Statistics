import csv

def showTeams() :
    print('===Select a team===')
    print('1. Sunrisers Hyderabad')
    print('2. Rising Pune Supergiant')
    print('3. Kolkata Knight Riders')
    print('4. Chennai Super Kings')
    print('5. Rajasthan Royals')
    print('6. Royal Challengers Bangalore')
    print('7. Mumbai Indians')
    print('8. Kings XI Punjab')
    print('9. Deccan Chargers')
    print('10. Kochi Tuskers Kerala')
    teamNum = int(input('Enter Team Name : '))

    if teamNum==1:
        team = 'Sunrisers Hyderabad'
    elif teamNum==2:
        team = 'Rising Pune Supergiant'
    elif teamNum == 3:
        team = 'Kolkata Knight Riders'
    elif teamNum ==4:
        team = 'Chennai Super Kings'
    elif teamNum ==5:
        team = 'Rajasthan Royals'
    elif teamNum ==6:
        team = 'Royal Challengers Bangalore'
    elif teamNum ==7:
        team = 'Mumbai Indians'
    elif teamNum ==8:
        team = 'Kings XI Punjab'
    elif teamNum ==9:
        team = 'Deccan Chargers'
    elif teamNum ==10:
        team = 'Kochi Tuskers Kerala'

    return team

def tossWin(team) :
    with open('matches.csv') as matchcsv:
        dRead = csv.DictReader(matchcsv)
        print (dRead)
        totalToss = 0
        wonToss = 0
        for rows in dRead :
            if rows['TEAM1'] == team or rows['TEAM2'] == team :
               totalToss +=1
            if rows['TOSS_WINNER'] == team :
                wonToss +=1
    return totalToss,wonToss

def yearWise_WonPlayed(team) :
    with open('matches.csv') as matchcsv:
        dRead = csv.DictReader(matchcsv)
        stat = {}
        year = set([rec['SEASON'] for rec in dRead])
        print(year)

        for sec in year:
            total = 0
            won = 0
            matchcsv.seek(0)
            for rows in dRead:
                if (rows['TEAM1'] == team or rows['TEAM2'] == team) and rows['SEASON'] == sec:
                    total +=1
                    if rows['WINNER'] == team:
                        won +=1

            stat[sec]={'Total':total, 'Won':won}
        return stat

def locationWise(team) :
    with open('matches.csv') as matchcsv:
        dRead = csv.DictReader(matchcsv)
        stat = {}
        loc = set([rec['CITY'] for rec in dRead])

        for city in loc:
            total = 0
            won = 0
            matchcsv.seek(0)
            for rows in dRead:
                if (rows['TEAM1'] == team or rows['TEAM2'] == team) and rows['CITY'] == city:
                    total +=1
                    if rows['WINNER'] == team:
                        won +=1

            stat[city]={'total':total, 'won':won}
        return stat