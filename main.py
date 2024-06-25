from colorama import *
question1 = input('Вы гуляли по улице, и вдруг пошел дождь. Cпрячитесь под крышей или пойдете дальше? ' + Fore.GREEN + '(yes (спрятаться), ' + Fore.BLUE + 'no (пойти дальше))')
while question1 not in ['yes', 'no']:
    question1 = input(Fore.WHITE + 'Вы гуляли по улице, и пошел дождь. Cпрячитесь под крышей или пойдете дальше? ' + Fore.GREEN + '(yes (спрятаться), ' + Fore.BLUE + 'no (пойти дальше))')
if question1 == 'yes':
    print(Fore.GREEN + 'Вы не намокли и спрятались под крышей')
    question2 = input(Fore.WHITE + 'К вам подошел человек ' + Fore.GREEN + 'yes (поздороваться), ' + Fore.BLUE + 'no (проигрнорировать)')
    while question2 not in ['yes', 'no']:
        question2 = input(Fore.WHITE + 'К вам подошел человек ' + Fore.GREEN + 'yes (поздороваться), ' + Fore.BLUE + 'no (проигрнорировать)')
    if question2 == 'yes':
        print(Fore.GREEN + 'У вас появился новый друг и дождь закончился')
        question4 = input(Fore.WHITE + 'Вы пошли в хорошем настроении домой с вашим новым другом, и по дороге встретили реку хотите поплавать? ' + Fore.RED + 'yes, ' + Fore.GREEN + 'no')
        while question4 not in ['yes', 'no']:
            question4 = input(Fore.WHITE + 'Вы пошли в хорошем настроении домой с вашим новым другом, и по дороге встретили реку хотите поплавать? ' + Fore.RED + 'yes, ' + Fore.GREEN + 'no')
        if question4 == 'yes':
            print(Fore.RED + 'Вы неумеете плавать. Вы утонули в реке')
            print(Fore.RED + 'game over')
        elif question4 == 'no':
            print(Fore.GREEN + 'Вы с другом пришли ночью домой и включив телевизор вы узнали что начался зомби апокалипсис')
            question9 = input('Побежите на улицу, или останетесь дома? yes (побежать на улицу), no (остаться дома)')
            while question9 not in ['yes', 'no']:
                question9 = input('Побежите на улицу, или останетесь дома? yes (побежать на улицу), no (остаться дома)')
            if question9 == 'yes':
                print('Вы выбежали на улицу и ваш друг увидел оружейный магазин')
                question11 = input('Будете брать оружие, или вы пацифист? yes (взять оружие), no (я пацифист)')
                while question11 not in ['yes', 'no']:
                    question11 = input('Будете брать оружие, или вы пацифист yes (взять оружие), no (я пацифист)')
                if question11 == 'yes':
                    print('Вы, с вашым другом, убили всех зомби которые пыталися зайти в магазин')
                    print('На следующий день, вас спасли военные')
                    print('You won')
                elif question11 == 'no':
                    print('Вы были заражены от зомби, но ваш друг убил его и остался жив')
                    print('game over')
            elif question9 == 'no':
                print('К вам в дом ворвался зомби. Он убил вашего друга')
                question10 = input('Побежите на улицу, или останетесь дома? yes (побежать на улицу), no (остаться дома)')
                while question10 not in ['yes', 'no']:
                    question10 = input('Побежите на улицу, или останетесь дома? yes (побежать на улицу), no (остаться дома)')
                if question10 == 'yes':
                    print('Вы дожили до утра. Вы узнали что зомби сгорают под солнечным светом')
                    question12 = input('Пойдете за помощью в полицейский участок, или останетесь на улице? yes (пойти в полицейский участок), no (остаться на улице)')
                    while question12 not in ['yes', 'no']:
                        question12 = input('Пойдете за помощью в полицейский участок, или останетесь на улице? yes (пойти в полицейский участок), no (остаться на улице)')
                    if question12 == 'yes':
                        print('К сожалению вы опоздали и там все уже были заражены. Вы были убиты')
                        print('game over')
                    elif question12 == 'no':
                        print('Вы остались на улице и вас увидел вертолет, пролетавший над вами')
                        print('Вы были спасены')
                        print('You won')
                elif question10 == 'no':
                    print('Вы были заражены от вашего друга')
                    print('game over')                    
    elif question2 == 'no':
        print(Fore.BLUE + 'Вы продолжили стоять, в одиночевстве под крышей')
        question5 = input(Fore.WHITE + 'Дождь закончился. Пойдете домой?' + Fore.GREEN + ' yes,' + Fore.RED + ' no')
        while question5 not in ['yes', 'no']:
            question5 = input(Fore.WHITE + 'Дождь закончился. Пойдете домой?' + Fore.GREEN + ' yes,' + Fore.RED + ' no')
        if question5 == 'yes':
            print(Fore.BLUE + 'Вы пришли домой в плохом настроении, потому что стояли 3 часа под кышей в ожидании')
            print('To be continued')
        elif question5 == 'no':
            print(Fore.RED + 'Вас сбила машина')
            print(Fore.RED + 'game over')
elif question1 == 'no':
    print(Fore.BLUE + 'Вы намокли и простыли')
    question3 = input('На вас идет подозрительный человек yes (поздороваться), no (проигрнорировать)')
    while question3 not in ['yes', 'no']:
        question3 = input('На вас идет подозрительный человек yes (поздороваться), no (проигрнорировать)')
    if question3 == 'yes':
        print('Вы поздоровались с этим человеком. Вас пырнули ножом')
        question7 = input('Вы истекаете кровью. Будете вызывать скорую? yes, no')
        while question7 not in ['yes', 'no']:
            question7 = input('Вы истекаете кровью. Будете вызывать скорую? yes, no')
        if question7 == 'yes':
            print('К вам приехала скорая и отвезла вас в больницу.')
            question8 = input('В больнице вы узнали что начался зомби апокалипсис. Хотите сбежать из больницы? yes, no')
            while question8 not in ['yes', 'no']:
                question8 = input('В больнице вы узнали что начался зомби апокалипсис. Хотите сбежать из больницы? yes, no')
            if question8 == 'yes':
                print('Как вы хотите сбежать через окно или через главный вход? window, main entrance')
                while question8 not in ['window', 'main entrance']:
                    question8 = ('Как вы хотите сбежать через окно или через главный вход? window, main entrance')
                if question8 == 'window':
                    print('Вы выпрыгнули с 9 этажа. Вы разбились')
                    print('game over')
                elif question8 == 'main entrance':
                    print('Вы смогли убежать через главный вход')
                    print('To be continued')
            elif question8 == 'no':
                print('К вам в полату зашёл зомби. Вы были заражены')
                print('game over')
        elif question7 == 'no':
            print('Вам никто не помог.')
            print('game over')
    elif question3 == 'no':
        print('Вы продолжили идти. Дождь закончился')
        question6 = input('Вы видите горящий дом. Хотите туда пойти? yes, no')
        while question6 not in ['yes', 'no']:
            question6 = input('Вы видите горящий дом. Хотите туда пойти? yes, no')
        if question6 == 'yes':
            print('Вы сгорели заживо')
            print('game over')
        elif question6 == 'no':
            print('Вы пришли домой в плохом настроении, потому что вы простыли')
            print('To be continued')
            
        
