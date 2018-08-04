#CODE NAME: akwaibomboymafia(Anwanakak Victor)
#This code was written by the "akwaibomboymafia" to round up my association with code lagos.Hopefully,the past 6ix weeks hasn't been a waste.
#THIS PROJECT WAS CARRIED OUT SUCCESSFULLY WITH THE USE OF THE FOLLOWING: function: print()and input(),while loop,conditionals: if,elif and else.
#Credit to Uncle Ben a.k.a(rexben) for doing nothing,and i am also sorry for using your name for every input() i use;what can i say it is a three letter word, as well as easy to call and recall. 
#As for  my Code lagos class mate turned family ikorodu(II) Igbogbo centre, Roll of Honor starting from, Ay (Iphone guy),Dotguy(Css king),Mr Ezekiel(Always asking about using python on visual basic) a.k.a Oga Eze, Mummy of the class( Dcn something sha so bad of me i don't know her name because she bought drinks on her birthday),Micheal,Mr kenny,Tunde(the web guru; this guy knows php,javascript now has learnt python what can i say he is just a boss)and the alien in our class Ola (Mr Disney)God bless you fam. I hope we all become great programmers.
#DISCRIPTION OF THE APP
#This is a World cup Russia 2018 result app for the just concluded Fifa world cup in Moscow. 
#The intention is for the user to input the password "world cup" to gain acess to the app; then uses the prescribed keyword allocated to each country in the app to get the results of the participating country to get their result 
#For my prediction for the winner of the 2018 Fifa world cup.I will go with *Croatia*; by the way my croatian name is *Victoric*.This was done on friday 13th of july 2018 so , if i am correct it will not be i cheated.

#Created a counter starting from 1
count=1
#password for the app
key="world cup"
print("Use the password:\"world cup\".Please in lower case without the quote("")")
#ask user to input password
password=input("Enter the password:")
#used while loop if key !=password
while(not(key==password)):
#excute this line of code
    password=input("""enter the key \"wrong password\": """)
   #if count==1:
        #break
        #count=count+1
    if key==password:
        print("Welcome to the World cup result app")
#collect input from user
name=input("What is your name: ")
#output
print(name,"it is nice to meet you") 

#defined my function rexben()
def rexben():
    #use print() to execute code
    print("To get the result of each countries enter the keyword  below")
    #created a list using countries as my variable name
    countries=["Argentina: \"arg\"","Australia: \"aus\"","Belguim: \"bel\"","Brazil: \"bra\" ","Colombia: \"col\"","Costa Rica: \"cos\"","Croatia: \"cro\"","England: \"eng\"","Eygpt: \"eyg\"","Denmark: \"den\"","France: \"fra\"","Germany: \"ger\"","Iceland: \"ice\"","Iran: \"ira\"","Japan: \"jap\"","Mexico:\"mex\"","Morroco:\"mor\"","Nigeria: \"nig\"","Panama: \"pan\"","Peru: \"per\"","Poland: \"pol\"","Portugal: \"por\"","Russia: \"rus\"","Senegal: \"sen\"","Serbia: \"ser\"","South korea: \"sou\"","Spain: \"spa\"","Suadi Arabia: \"sua\"","Sweden: \"swe\"","Switzerland: \"swi\"","Uruguay:\"uru\""]
    #used for loop to iterate the list
    for list in countries:
        print(list)
    country=input("Enter the keyword: ")
    if country=="arg":
        print("Group D; \"Group of Death\"")
        print("Argentina vs Iceland: FT 1:1")
        print("Argentina vs Croatia: FT 0:3")
        print("Argentina vs Nigeria: FT 2:1")
        print("Progressed to round of 16 with the help of referee \"OJORO MASTER\"")
        print("Round of 16; Argentina vs France: FT 3:4")
        print("Failed to progress from round of 16")
    elif country=="aus":
        print("Group C")
        print("Australia vs France: FT 2:1")
        print("Australia vs Denmark: FT 1:1")
        print("Australia vs Peru : FT 0:2 ")
        print("Failed to progress from group stage")
    elif country=="bel":
        print("Group G")
        print("Belguim vs Panama FT 3:0")
        print("Belguim vs Tunisia FT 5:2")
        print("Belguim vs England FT 1:0")
        print("Progressed to round of 16")
        print("Round of 16; Belguim vs Japan FT 3:2")
        print("Progressed to quater final")
        print("Quater final; Belguim vs Brazil FT 2:1")
        print("Progressed from quarter final")
        print("Semi final; Belguim vs France FT 0:1")
        print("Failed to progress from semifinal")
        print("Third place match; Belguim vs England FT 2:0")
        print("Exited with a bronze medal")
    elif country=="bra":
        print("Brazil vs Switzerland FT 1:1")
        print("Brazil vs Costa Rica FT 0:2")
        print("Brazil vs Serbia FT 2:0")
        print("Progressed from group stage")
        print("Brazil vs Mexico FT 2:0")
        print("Progressed to quater final")
        print("Quarter final: Brazil vs Belguim FT 1:2")
        print("Failed to progress from quarter final")
    elif country=="col":
        print("Group H")
        print("Colombia vs Japan FT 1:2")
        print("Colombia vs Poland FT 3:0")
        print("Colombia vs Senegal FT 1:0")
        print("Progressed to round of 16")
        print("Quarter final; Colombia vs Englan FT 1:1 Pen 3:4")
        print("Failed to progress to quarter final")
    elif country=="cos":
        print("Group E")
        print("Costa Rica vs Serbia FT 0:1")
        print("Costa Rica vs Brazil FT 0:2")
        print("Costa Rica vs Switzerland FT 2:2")
        print("Failed to progress from group stage")
    elif country=="cro":
        print("Group D")
        print("Croatia vs Nigeria FT 2:0")
        print("Croatia vs Argentina FT 3:0")
        print("Croatia vs Iceland FT 2:1")
        print("Progressed to round of 16")
        print("Round of 16: Croatia vs Denmark FT 1:1 Pen 3:2 ")
        print("Progressed to quater final")
        print("Quarter final; Croatia vs Russia FT 2:2 Pen 6:5")
        print("Progressed to semi final ")
        print("Semi final; Croatia vs England FT 1:1 AET 2:1")
        print("Progressed to the final")
        print("Final; Croatia vs France FT 2:4")
        print("Exited with a silver medal")
    elif country=="eng":
        print("Group G")
        print("England vs Tunisia FT 2:1")
        print("England vs Panama FT 6:1")
        print("England vs Belgium FT 0:1")
        print("Progressed to round of 16")
        print("Round of 16: England vs Colombia FT 1:1 4:3")
        print("Progressed to the quarter final ")
        print("Quarter final; England vs Sewden FT 2:0 ")
        print("Progressed to semi final")
        print("Semi final; England vs Croatia FT 1:1 AET 1:2")
        print("Failed to progress from semi final")
        print("Third place match; England vs Belguim FT 0:2.\nKane go and collect your \"Penalty boot award\"")
    elif country=="eyg":
        print("Group A")
        print("Eygpt vs Uruguay FT 0:1")
        print("Eygpt vs Russia FT 1:3")
        print("Eygpt vs Suadi Arabia FT 1:2")
        print("Failed to progress from group stage")
    elif country=="den":
        print("Group C")
        print("Denmark vs Peru FT 1:0")
        print("Denmark vs Australia FT 1:1")
        print("Denmark vs France FT 0:0")
        print("Progressed to round of 16")
        print("Round of 16; Denmark vs Croatia FT 1:1 Pen 2:3")
        print("Failed to progressed from Round of 16")
    elif country=="fra":
        print("Group C")
        print("France vs Australia FT 2:1")
        print("France vs Peru FT 1:0")
        print("France vs Denmark FT 0:0")
        print("Progressed to round of 16")
        print("Round of 16; France vs Argentina FT 4:3")
        print("Progressed to round of 16")
        print("Quarter final; France vs Uruguay FT 2:0")
        print("Progressed from quarter final")
        print("Semi final; France vs Belguim FT 1:0")
        print("Progressed to the final")
        print("Final; France vs Croatia FT 4:2")
        print("Champions of the World")
    elif country=="ger":
        print("Group F")
        print("Germany vs Mexico FT 0:1")
        print("Germany vs Sweden FT 2:1")
        print("Germany vs South Korea FT 0:2")
        print("Failed to progress from group stage")
    elif country=="ice":
        print("Group D; \"group of death \"")
        print("Iceland vs Argentina FT 1:1")
        print("Iceland vs Nigeria FT 0:2")
        print("Iceland vs Croatia FT 1:2")
        print("Failed to progressed from group stage")
    elif country=="ira":
        print("Group B")
        print("Iran vs Morroco FT 1:0")
        print("Iran vs Spain FT 0:1")
        print("Iran vs Portugal FT 1:1")
        print("Failed to progress from group stage")
    elif country=="jap":
        print("Group H")
        print("Japan vs Colombia FT 2:1")
        print("Japan vs Sengal FT 1:1")
        print("Japan vs Poland FT 0:1")
        print("Progressed to round of 16")
        print("Round of 16; Japan vs Belguim FT 2:3")
        print("Failed to progress from round of 16")
    elif country=="mex":
        print("Group F")
        print("Mexico vs Germany FT 1:0")
        print("Mexico vs South Korea FT 2:1")
        print("Mexico vs Sewden FT 0:3")
        print("Progressed to round of 16")
        print("Round of 16; Mexico vs Brazil FT 0:2")
        print("Failed to progress from round of 16")
    elif country=="mor":
        print("Group B")
        print("Morroco vs Iran FT 0:1")
        print("Morroco vs Portugal FT 0:1")
        print("Morroco vs Spain FT 2:2")
        print("Failed to progress from group stage")
    elif country=="nig":
        print("Group of D; \"group of death\"")
        print("Nigeria vs Croatia FT 0:2")
        print("Nigeria vs Iceland FT 2:0")
        print("Nigeria vs Argentina FT 1:2")
        print("Failed to progress group stage")
    elif country=="pan":
        print("Panama vs Belguim FT 0:3")
        print("Panama vs England FT 1:6")
        print("Panama vs Tunisia FT 1:2")
        print("Failed to progress from group stage")
    elif country=="por":
        print("Group B")
        print("Portugal vs Spain FT 3:3")
        print("Portugal vs Morroco FT 1:0")
        print("Portugal vs Iran FT 1:1")
        print("Progressed to round of 16")
        print("Round of 16; Portugal vs Uruguay FT 1:2")
        print("Failed to progress from round of 16")
    elif country=="rus":
        print("Group A")
        print("Russia vs Suadi Arabia FT 5:0")
        print("Russia vs Eygpt FT 3:1")
        print("Russia vs Uruguay FT 3:0")
        print("Progressed to the round of 16")
        print("Round of 16; Russia vs Spain 1:1 Pen 4:3")
        print("Progressed to quarter final")
        print("Quarter final; Russia vs Croatia FT 2:2 Pen 5:6")
        print("Failed to progress from round of 16 ")
    elif country=="sen":
        print("Senegal vs Poland FT 2:1")
        print("Senagal vs Japan FT 1:1")
        print("Senegal vs Colombia FT 0:1")
        print("Failed to progress from goup stage")
    elif country=="ser":
        print("Group E")
        print("Serbia vs Costa Rica FT 1:0")
        print("Serbia vs Switzerland FT 1:2")
        print("Serbia vs Brazil FT 0:2 ")
        print("Failed to progress from group stage")
    elif country=="sou":
        print("Group F")
        print("South Korea vs Sweden FT 0:1")
        print("South korea vs Mexico FT 1:2")
        print("South Korea vs Germany FT 2:0 ")
        print("Failed to progress from group stage")
    elif country=="spa":
        print("Spain vs Portugal FT 3:3")
        print("Spain vs Iran FT 1:0")
        print("Spain vs Morroco FT 2:2")
        print("Progressed to round of 16")
        print("Round of 16; Spain vs Russia FT 1:1 Pen 3:4 ")
        print("Failed to progress from round of 16")
    elif country=="sua":
        print("Group A")
        print("Suadi Arabia vs Russia FT 0:5")
        print("Suadi Arabia vs Uruguay FT 0:1")
        print("Suadi Arabia vs Eygpt FT 2:1")
        print("Failed to progress from group stage")
    elif country=="swe":
        print("Group F")
        print("Sweden vs Costa rica FT 1:0")
        print("Sweden vs Germany FT 1:2")
        print("Sweden vs Mexico FT 3:0")
        print("Progressed to round of 16")
        print("Round of 16; Sweden vs Switzerland FT 1:0")
        print("Progressed to quater final")
        print("Quater final; Sweden vs England FT 0:2")
        print("Failed to progress from quater final")
    elif country=="swi":
        print("Group E")
        print("Switzerland vs Brazil FT 1:1")
        print("Switzerland vs Serbia FT 2:1")
        print("Switzerland vs Costa Rica FT 2:2 ")
        print("Progress to round of 16")
        print("Switzerland vs Sweden FT 0:1")
        print("Failed to progress from round of 16")
    elif country=="uru":
        print("Uruguay vs Eygpt FT 1:0")
        print("Uruguay vs Suadi Arabia FT 1:0")
        print("Uruguay vs Russia FT 3:0")
        print("Progressed to round of 16")
        print("Round of 16; Uruguay vs Portugal FT 2:1")
        print("Progressed to quarter final")
        print("Quater final; Uruguay vs France FT 2:0")
        print("Failed to progress from quater final")
    else:
        print("Invalid input")
    while True:
        return rexben()
rexben()

