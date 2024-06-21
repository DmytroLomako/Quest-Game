from colorama import *
question1 = input('вы гуляли по улице и пошел дождь спрячитесь под крышей или пойдете дальше ' + Fore.GREEN + '(yes (спрятаться), ' + Fore.BLUE + 'no (пойти дальше))')
while question1 not in ['yes', 'no']:
    question1 = input(Fore.WHITE + 'вы гуляли по улице и пошел дождь спрячитесь под крышей или пойдете дальше ' + Fore.GREEN + '(yes (спрятаться), ' + Fore.BLUE + 'no (пойти дальше))')
if question1 == 'yes':
    print(Fore.GREEN + 'вы не намокли и спрятались под крышей')
    question2 = input(Fore.WHITE + 'к вам подошел человек ' + Fore.GREEN + 'yes (поздороваться), ' + Fore.BLUE + 'no (проигрнорировать)')
    while question2 not in ['yes', 'no']:
        question2 = input(Fore.WHITE + 'к вам подошел человек ' + Fore.GREEN + 'yes (поздороваться), ' + Fore.BLUE + 'no (проигрнорировать)')
    if question2 == 'yes':
        print(Fore.GREEN + 'у вас появился новый друг и дождь закончился')
        question4 = input(Fore.WHITE + 'вы пошли в хорошем настроении домой с вашим новым другом и по дороге встретили реку хотите поплавать? ' + Fore.RED + 'yes, ' + Fore.GREEN + 'no')
        while question4 not in ['yes', 'no']:
            question4 = input(Fore.WHITE + 'вы пошли в хорошем настроении домой с вашим новым другом и по дороге встретили реку хотите поплавать? ' + Fore.RED + 'yes, ' + Fore.GREEN + 'no')
        if question4 == 'yes':
            print(Fore.RED + 'вы неумеете плавать. вы утонули в реке')
            print(Fore.RED + 'game over. you can`t swim ending')
        elif question4 == 'no':
            print(Fore.GREEN + 'вы с другом пришли домой и отлично провели день')
            print(Fore.GREEN + 'game over. best ending')
    elif question2 == 'no':
        print(Fore.BLUE + 'вы продолжили стоять в одиночевстве под крышей')
        question5 = (Fore.WHITE + 'дождь закончился. пойдете домой?' + Fore.GREEN + ' yes,' + Fore.RED + ' no')
        while question5 not in ['yes', 'no']:
            question5 = (Fore.WHITE + 'дождь закончился. пойдете домой?' + Fore.GREEN + ' yes,' + Fore.RED + ' no')
        if question5 == 'yes':
            print(Fore.GREEN + 'вы пришли домой в плохом настроении потому что стояли 3 часа под кышей в ожидании')
            print(Fore.BLUE + 'game over. normal ending')
        elif question5 == 'no':
            print(Fore.RED + 'вас сбила машина')
            print(Fore.RED + 'why you stayed here ending')
elif question1 == 'no':
    print(Fore.BLUE + 'вы намокли и простыли')
    question3 = input('на вас идет подозрительный человек yes (поздороваться), no (проигрнорировать)')
    while question3 not in ['yes', 'no']:
        question3 = input('на вас идет подозрительный человек yes (поздороваться), no (проигрнорировать)')
    if question3 == 'yes':
        print('вы поздоровались с этим человеком и он вас пырнул ножом')
        print('game over. don`t talk to strangers ending')
    elif question3 == 'no':
        print('вы продолжили идти и дождь закончился')
        question6 = ('вы видите горящий дом хотите туда пойти? yes, no')
        while question6 not in ['yes', 'no']:
            question6 = ('вы видите горящий дом хотите туда пойти? yes, no')
        if question6 == 'yes':
            print('вы сгорели заживо')
            print('game over. why? ending')
        elif question6 == 'no':
            print('вы пришли домой в плохом настроении потому что вы простыли')
            print('game over. normal ending')
        
