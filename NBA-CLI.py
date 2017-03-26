from cmd2 import Cmd, make_option, options

import requests

from clint.textui import colored, puts

import datetime

class  NBAStats(Cmd):
    Cmd.prompt = "NBA Stats>"
    puts(colored.yellow("Welcome to the NBA CLI. If this is your first time, type help to get started."))
    puts(colored.yellow("Developed by FireTrix 2017"))


    @options([
        make_option("--choice", dest = "choice"),
        make_option("--gameid", dest = "gameid")
            ])
    def do_games(self,arg,opts = None):
        teams = []
        times = []
        games = []
        yday = False
        td = False
        tomorrow = False
        scorespre = []
        scoresafter = []
        scoresfinal = []
        scoretwos= []
        gamecode = []
        players1 = []
        players2 = []
        reb1 = []
        reb2 = []
        assis1 = []
        assis2= []
        steal1= []
        steal2= []
        turn1= []
        turn2= []
        pts1= []
        pts2= []
        f = 0
        
        if opts.choice == "yesterday":
            today = datetime.date.today()
            date = int(today.strftime('%Y%m%d'))-1
            url = "http://stats.nesn.com/nba/scoreboard.asp?day=" + str(date) + "&meta=true"
            r = requests.get(url)
            yday = True
            text = (requests.get("http://stats.nesn.com/nba/scoreboard.asp?day="+str(date))).text
            quotesremoved = text.replace("\"","^")
            for c in range(0, len(quotesremoved)):
                if(quotesremoved[c:c+9] == "gamecode="):
                    gamecode.append(quotesremoved[c+9:c+19])
        if opts.choice =="today":
            r = requests.get("http://stats.nesn.com/nba/scoreboard.asp?")
            td = True
            text = (requests.get("http://stats.nesn.com/nba/scoreboard.asp?")).text
            quotesremoved = text.replace("\"","^")
            for c in range(0, len(quotesremoved)):
                if(quotesremoved[c:c+9] == "gamecode="):
                    gamecode.append(quotesremoved[c+9:c+19])
        if opts.choice == "tomorrow":
            today = datetime.date.today()
            date = int(today.strftime('%Y%m%d'))+1
            url = "http://stats.nesn.com/nba/scoreboard.asp?day=" + str(date) + "&meta=true"
            r = requests.get(url)
            tomorrow = True

        response = r.text
        quotesremoved = response.replace("/""","^")
        #print(quotesremoved)
        for c in range (0,len(quotesremoved)):
            if quotesremoved[c:c+10] == 'teamhome">':
                for j in range(1,30):
                    if quotesremoved[c+j:c+j+1] == "<":
                        teams.append(quotesremoved[c+10:c+10+j])

        for c in range (0,len(teams)):
            teams[c] = teams[c][0:len(teams[c])-len("<^a>&nbsp;")]

            if teams[c] == "Phoenix":
                teams[c] = "Phoenix Suns"
            if teams[c] == "Brooklyn":
                teams[c] = "Brooklyn Nets"
            if teams[c] == "Toronto":
                teams[c] = "Toronto Raptors"
            if teams[c] == "Miami":
                teams[c] = "Miami Heat"
            if teams[c] == "LA Clippers":
                teams[c] = "Los Angeles Clippers"
            if teams[c] == "Dallas":
                teams[c] = "Dallas Mavericks"
            if teams[c] == "Memphis":
                teams[c] = "Memphis Grizzlies"
            if teams[c] == "San Antonio":
                teams[c] = "San Antonio Spurs"
            if teams[c] == "New York":
                teams[c] = "New York Knicks"
            if teams[c] == "Portland":
                teams[c] = "Portland Trailblazers"
            if teams[c] == "Washington":
                teams[c] = "Washington Wizards"
            if teams[c] == "Cleveland":
                teams[c] = "Cleveland Cavaliers"
            if teams[c] == "Charolotte":
                teams[c] = "Charlotte Hornets"
            if teams[c] == "Detroit":
                teams[c] = "Detroit Pistons"
            if teams[c] == "Orlando":
                teams[c] = "Orlando Magic"
            if teams[c] == "Denver":
                teams[c] = "Denver Nuggets"
            if teams[c] == "Indiana":
                teams[c] = "Indiana Pacers"
            if teams[c] == "Boston":
                teams[c] = "Boston Celtics"
            if teams[c] == "Philadelphia":
                teams[c] = "Philadelphia 76ers"
            if teams[c] == "Chicago":
                teams[c] = "Chicago Bulls"
            if teams[c] == "Atlanta":
                teams[c] = "Atlanta Hawks"
            if teams[c] == "Milwaukee":
                teams[c] = "Milwaukee Bucks"
            if teams[c] == "New Orleans":
                teams[c] = "New Orleans Pelicans"
            if teams[c] == "Houston":
                teams[c] = "Houston Rockets"
            if teams[c] == "Minnesota":
                teams[c] = "Minnesota Timberwolves"
            if teams[c] == "Los Angeles":
                teams[c] = "Los Angeles Lakers"
            if teams[c] == "Sacramento":
                teams[c] = "Sacramento Kings"
            if teams[c] == "Golden State":
                teams[c] = "Golden State Warriors"
            if teams[c] == "Utah ":
                teams[c] == "Utah Jazz"

        for c in range (0,len(teams)):
            if teams[c].find("<^a>") != -1:
                teams[c] = " "
                
        for c in range (0,len(teams)):
            if teams[c] == " ":
                teams.append(teams[c])
                teams.remove(teams[c])
                
        for c in range(0,len(teams)):
            if c % 2 != 0:
                if len(teams[c]) > 2:
                    games.append((teams[c-1] + " vs. " + teams[c]))
                if len(teams[c]) < 2:
                    break
        totcounter = 0
        finalcounter = 0
        
        for c in range(0,len(quotesremoved)):
            if quotesremoved[c:c+47] == '<td class="shsTotD" style="width: 10%">Tot<^td>':
                totcounter = totcounter + 1
            if quotesremoved[c:c+14] == "Final Boxscore":
                finalcounter = finalcounter + 1
            if quotesremoved[c:c+5] == "PM ET":
                times.append(quotesremoved[c-6:c])
            if quotesremoved[c:c+20] == '<td class="shsTotD">':
                for j in range(0,50):
                    if quotesremoved[c+j:c+j+1] == "<":
                        scorespre.append(quotesremoved[c+20:c+j])
                    
        for c in range(0,len(times)):
            if ">" in times[c]:
                times[c] = times[c][1:len(times[c])]

        for c in range (0,len(scorespre)):
            if (len(scorespre[c]) < 4 and scorespre[c] != '' and scorespre[c]!= "OT"):
                scoresafter.append(scorespre[c])
                
        for c in range (0,len(scoresafter)):
            if (int(scoresafter[c]) > 50):
                scoresfinal.append(scoresafter[c])
      
        teamcounter = 0

        for c in range (0,len(scoresfinal)):
            if c % 2 != 0:
                scoretwos.append(scoresfinal[c-1] + " - " + scoresfinal[c])
        idcounter = 0
        for c in range (0,len(games)):
            if finalcounter > 0:
                puts(colored.yellow(games[c] + " has finished. The final score is " + scoretwos[c] +". Game id is " + str(idcounter)))
                finalcounter = finalcounter - 1
                totcounter = totcounter - 1
                teamcounter = teamcounter + 1
                idcounter = idcounter + 1
        for c in range (teamcounter,len(games)):
            if totcounter > 0 and finalcounter == 0:
                puts(colored.green(games[c] + " is currently being played. The score currently is " + scoretwos[c] + "."))
                totcounter = totcounter -1
                teamcounter = teamcounter + 1
        for c in range (0,len(times)):
            if len(games) > teamcounter:
                puts(colored.yellow(games[c] + " is going to start at "+ times[c]+"PM ET"))
        if (opts.choice == None and opts.gamieid != None):
            puts(colored.red("Please specify a choice for which day you want!"))
        if(opts.choice == "tomorrow" and opts.gameid != None):
            puts(colored.red("You cannot view boxscores for tomorrow!"))
        if(opts.gameid != None and opts.choice!= "tomorrow"):
            if len(str(opts.gameid)) == 1:
                text = (requests.get("http://stats.nesn.com/nba/boxscore.asp?gamecode="+gamecode[int(opts.gameid)])).text
                shortenedtext = text.replace("\"","^")
                shortenedtext = shortenedtext[shortenedtext.index("colspan=^15^>") + 13: len(shortenedtext)]
                shortenedtext1 = shortenedtext[0:shortenedtext.index("colspan=^15^>")]
                shortenedtext2 = shortenedtext[shortenedtext.index("colspan=^15^>") + 13: len(shortenedtext)]
            for c in range(0,len(shortenedtext1)):
                if(shortenedtext1[c:c+10] == "&amp;team="):
                    temp = ""
                    for i in range(c+13,c+ 32):
                        temp = temp + shortenedtext1[i]
                        if(shortenedtext1[i] == '<'):
                            break
                    
                    temp = temp.strip('<')
                    temp = temp.strip('>')
                    players1.append(temp)
                    f = f + 1
                    count = 0
                    while(count < 14):
                        if(shortenedtext1[c:c+8] == "^shsTotD"):
                            count = count + 1
                            if(count == 8):
                                temp = ""
                                for a in range(c+10, c + 15):
                                    if(shortenedtext1[a] == '<'):
                                        break
                                    temp = temp + shortenedtext1[a]
                                reb1.append(temp)
                            if(count == 9):
                                temp = ""
                                for a in range(c+10, c + 15):
                                    if(shortenedtext1[a] == '<'):
                                        break
                                    temp = temp + shortenedtext1[a]
                                assis1.append(temp)
                            if(count == 11):
                                temp = ""
                                for a in range(c+10, c + 15):
                                    if(shortenedtext1[a] == '<'):
                                        break
                                    temp = temp + shortenedtext1[a]
                                steal1.append(temp)
                            if(count == 12):
                                temp = ""
                                for a in range(c+23, c + 40):
                                    if(shortenedtext1[a] == '<'):
                                        break
                                    temp = temp + shortenedtext1[a]
                                turn1.append(temp)
                            if(count == 14):
                                temp = ""
                                for a in range(c+10, c + 15):
                                    if(shortenedtext1[a] == '<'):
                                        break
                                    temp = temp + shortenedtext1[a]
                                pts1.append(temp)
                        c = c + 1
                
                if(f == 9):
                    break
            f = 0
            for c in range(0,len(shortenedtext2)):
                if(shortenedtext2[c:c+10] == "&amp;team="):
                    temp = ""
                    for i in range(c+13,c+ 32):
                        temp = temp + shortenedtext2[i]
                        if(shortenedtext2[i] == '<'):
                            break
                    temp = temp.strip('<')
                    temp = temp.strip('>')
                    players2.append(temp)
                    f = f + 1
                    count = 0
                    while(count < 14):
                        if(shortenedtext2[c:c+8] == "^shsTotD"):
                            count = count + 1
                            if(count == 8):
                                temp = ""
                                for a in range(c+10, c + 15):
                                    if(shortenedtext2[a] == '<'):
                                        break
                                    temp = temp + shortenedtext2[a]
                                reb2.append(temp)
                            if(count == 9):
                                temp = ""
                                for a in range(c+10, c + 15):
                                    if(shortenedtext2[a] == '<'):
                                        break
                                    temp = temp + shortenedtext2[a]
                                assis2.append(temp)
                            if(count == 11):
                                temp = ""
                                for a in range(c+10, c + 15):
                                    if(shortenedtext2[a] == '<'):
                                        break
                                    temp = temp + shortenedtext2[a]
                                steal2.append(temp)
                            if(count == 12):
                                temp = ""
                                for a in range(c+23, c + 40):
                                    if(shortenedtext2[a] == '<'):
                                        break
                                    temp = temp + shortenedtext2[a]
                                turn2.append(temp)
                            if(count == 14):
                                temp = ""
                                for a in range(c+10, c + 15):
                                    if(shortenedtext2[a] == '<'):
                                        break
                                    temp = temp + shortenedtext2[a]
                                pts2.append(temp)
                        c = c + 1
                if(f == 9):
                    break
                
            meme = games[int(opts.gameid)].split("vs.")

            puts(colored.yellow(meme[0] + "boxscore:"))
            for c in range(0,len(players1)):
                puts(colored.green(players1[c] + " scored " + pts1[c] + " points, had " + assis1[c] + " assists, grabbed " + reb1[c] + " rebounds, snached up " + steal1[c] + " steals,and committed " + turn1[c] + " turnovers."))  
            puts(colored.yellow(meme[1] + " boxscore:"))
            for c in range(0,len(players2)):
                puts(colored.green(players2[c] + " scored " + pts2[c] + " points, had " + assis2[c] + " assists, grabbed " + reb2[c] + " rebounds, snached up " + steal2[c] + " steals,and committed " + turn2[c] + " turnovers."))  

    def do_help(self,arg,opts = None):
        puts(colored.yellow("To view scores, type in games --choice [option]. In place of [option], type in yesterday, tomorrow, or today. For example, an example of a command you could run would be: games --choice yesterday"))
        puts(colored.yellow("Doing this will show games that have been played/are currently on for that day. If the game has ended, a 'game id' will be available"))
        puts(colored.yellow("To view the boxscore of a certain game that has ended, type in games --choice [option] --gameid [id number]"))
        puts(colored.yellow("In [id number] above, type in the game id that you want, which will be provided for you! An example of this command would be: games --choice today --gameid 1"))
        puts(colored.yellow("We also have created the standings command. Simply type standings into the prompt, and it will return eastern and western conference rankings!"))
    def do_standings(self,arg,opts = None):
        url = "http://stats.nesn.com/nba/standings_conference.asp"
        r = requests.get(url)
        steams = []
        scores = []
        east = []
        west = []
        eastscores = []
        westscores = []
        eastscoresfinal = []
        westscoresfinal = []

        for c in range (0,len(r.text)):
            if r.text[c:c+14] == "</span></span>":
                for j in range(0,50):
                    if r.text[c+j:c+j+4] == "</a>":
                        steams.append(r.text[c+14:c+18+j])
        for c in range (0,len(steams)):
            steams[c] = steams[c][:steams[c].index("</a></td>\r\n<td cla")]

        for c in range (0,len(r.text)):
            if r.text[c:c+20] == '<td class="shsTotD">':
                scores.append(r.text[c+20:c+22])
           
        east = steams[0:len(steams)//2]
        west = steams[len(steams)//2:len(steams)]
        eastscores = scores[0:len(scores)//2-2]
        westscores = scores[len(scores)//2-2:len(scores)]

        estatcounter = 0
        for c in range(0,len(eastscores)):
            if estatcounter == 0:
                eastscoresfinal.append(eastscores[c]+" - " +eastscores[c+1])
                estatcounter = estatcounter + 1
            elif estatcounter == 3:
                estatcounter = 0
            else:
                estatcounter = estatcounter + 1

        wstatcounter = 0
        for c in range(0,len(westscores)):
            if wstatcounter == 0:
                westscoresfinal.append(westscores[c]+" - " +westscores[c+1])
                wstatcounter = wstatcounter + 1
            elif wstatcounter == 3:
                wstatcounter = 0
            else:
                wstatcounter = wstatcounter + 1

        puts(colored.yellow("Eastern Confrence Standings"))
        for c in range (0,len(east)):
            puts(colored.green(east[c] + " " + eastscoresfinal[c]))
        print(" ")
        print(" ")
        puts(colored.yellow("Western Conference Standings"))
        for c in range (0,len(west)):
            puts(colored.green(west[c] + " " + westscoresfinal[c]))
        
                
                
                
                
                
            
nba = NBAStats()
nba.cmdloop()
