import random

# create new captain and his privates
alphabet = ['B', 'C', 'D', 'F', 'G', 'H', 'Q',
            'R', 'Y', 'U', 'I', 'O', 'P', 'J',
            'K', 'L', 'Z', 'X', 'V', 'N', 'M']

# to create dictionary for trench.  keys= trench no , values =  list of tags
trench_dic = {}
for i in range(10):
    trench_dic[str(i)] = []

# to save all object create a dic.  keys= trench no , values =  list of captains(privates in his squad list) and colonels
objects_dic = {}
for i in range(10):
    objects_dic[str(i)] = []


class Private:
    CLASS_NAME = 'Private'

    def __init__(self, tag, commander_name, trench):
        self.tag = tag
        self.commander_name = commander_name
        self.trench = trench
        self.shield = 25     # if shield 0 it is  out of battle
        # ammunition random between 20 to 30  # if amunation 0 it is not out of battle
        self.ammunition = random.randint(20, 30)

    def attack(self, order):  # order is ammunition values
        fire = min(self.ammunition, order)
        self.ammunition -= fire
        return fire


class Captain(Private):  # captain class, subclass of private
    CLASS_NAME = 'Captain'

    def __init__(self, tag, commander_name, trench):
        super().__init__(tag, commander_name, trench)
        self.shield = 50     # if shield 0 he and his all is  out of battle
        # ammunition random between 40 to 60  # if amunation 0 it is not out of battle
        self.ammunition = random.randint(40, 60)
        self.trench = trench
        self.squad = []  # object list of his privates
        self.trench_list = []  # list of his trenches
        self.trench_list.append(trench)

    def report(self):  # report to colonel
        self.total_shield = self.shield  # total shield in his squad
        self.total_ammunition = self.ammunition  # total ammunition in his squad
        for soldier in self.squad:
            self.total_shield += soldier.shield
            self.total_ammunition += soldier.ammunition

    def move(self, to, captain):  # move to captain and his privates
        if self.trench_list[-1] == to:
            print(f'You are already in trench {to}.')
        else:
            print(f'You are moving {captain.trench} to trench {to}.')
            trench_dic[captain.trench].remove(captain.tag)
            objects_dic[captain.trench].remove(captain)
            captain.trench_list.append(to)
            captain.trench = to
            trench_dic[captain.trench].append(captain.tag)
            objects_dic[captain.trench].append(captain)
            print(f'You are in trench {captain.trench} now.')

    # when user choose attact-4 , then call clash function , if attact captain and his privates
    def squad_attack(self):
        total_fire = 0
        order = int(input('\nEnter ammunition values to attack the enemy : '))
        for i in self.squad:  # call attack method for each privates in squad list
            fire = i.attack(order)
            total_fire += fire
            if i.shield == 0:  # remove the private if his shield equal to zero
                self.squad.remove(i)
                print(
                    f'The ammunition of private {i} has been exhausted and he was out of war.')
        return total_fire

    def damage_squad(self, total_hit):  # damage the enemy as much as your total_hit
        for enemy_soldier in self.squad:  # call enemy.squad for each privates
            enemy_soldier.shield -= min(enemy_soldier.shield, total_hit)
            total_hit -= min(enemy_soldier.shield, total_hit)
            if enemy_soldier.shield == 0:
                print(f'Enemy soldier {enemy_soldier.tag} has been killed')
                self.squad.remove(enemy_soldier)
        print(f"{self.tag} squad was damaged.")


class Colonel(Private):  # colonel class is subclass of private class
    CLASS_NAME = 'Colonel'

    def __init__(self, tag, trench):  # we didn't use super() for colonel
        self.tag = tag
        # shield random between 950 to 1050
        self.shield = random.randint(950, 1050)
        self.trench = trench
        self.trench_list = []  # trench list of trenches where colonel has stayed so far
        self.captains = []  # list of objects captan and his squad(privates)
        self.captainsNameList = list()
        self.trench_list.append(trench)

    def move(self, to, colonel):  # change colonel trench
        if self.trench_list[-1] == to:
            print(f'You are already in trench {to}.')
        else:
            trench_dic[self.trench].remove(self.tag)
            objects_dic[self.trench].remove(colonel)
            self.trench_list.append(to)
            self.trench = to
            trench_dic[self.trench].append(self.tag)
            objects_dic[self.trench].append(colonel)
            print(f'You are in trench {self.trench} now.')

    def review_reports(self):  # report all details of captain and his privates
        nthCaptainCount = 0
        allTotalShield = 0
        allTotalAmmunition = 0
        allTotalSoldiers = 0
        if len(self.captains) == 0:
            print("You haven't got any captain and squad. Please create new squad.")
        for i in self.captains:
            nthCaptainCount += 1
            i.report()  # call report method for each every captain in list of captains
            allTotalSoldiers += len(i.squad)
            allTotalShield += i.total_shield
            allTotalAmmunition += i.total_ammunition
            print(f'''\nReports for {nthCaptainCount}. Captain = {i.tag}''')
            for j in i.squad:
                print(f'''
        +++++++++++++++++++++++++++++++++++++++++++++++++
        Rank of soldier = {j.CLASS_NAME}
        Name of soldier = {j.tag}
        Shield of soldier = {j.shield}
        Ammunition of soldier = {j.ammunition}''')
            print(f'''
            ****************************************************
              Count of soldiers in squad = {len(i.squad)}
              Total shield of squad = {i.total_shield}
              Total ammunition of squad= {i.total_ammunition}
              All Trenches List of squad= {i.trench_list}''')
            print('*'*70, "\n")
            if nthCaptainCount == len(self.captains):
                print(f"""ALL TOTAL OF GARRISON
                    Total captains of all squads = {nthCaptainCount}
                    Soldiers count of all squads = {allTotalSoldiers}
                    Total Shields of all squads = {allTotalShield}
                    Total Ammunition of all squads = {allTotalAmmunition}
                  """)
        else:
            print('*'*90)

    # order to create new squad and captain and his 5 privates as much as your shield greater than 300
    def new_squad(self, colonel):
        print('\nCreating new squad...')
        countOfPrivates = 5
        while True:
            print('Your current total shield = ', self.shield)
            if self.shield <= 300:
                print("You don't have enough shield to create new squad !!!")
                break
            else:
                self.shield -= 50 + countOfPrivates * 25
                while True:  # check squad name same or not
                    # EAST or WEST+ a random letter for captain-squat name
                    tag = self.tag + "-" + random.choice(alphabet)
                    if tag in self.captainsNameList:
                        print("same name is created.for searching to new name")
                        continue
                    else:
                        break
                tag_list = [tag + str(i) for i in range(countOfPrivates)]
                keysListe = list()
                for i in trench_dic.keys():
                    keysListe.append(i)
                newTrench = random.choice(keysListe)
                trench_dic[newTrench].append(tag)

                tag = Captain(tag, colonel, newTrench)
                objects_dic[newTrench].append(tag)
                self.captains.append(tag)
                self.captainsNameList.append(tag.tag)
                tag.squad.append(tag)
                for i in tag_list:
                    i = Private(i, tag, newTrench)
                    tag.squad.append(i)
                print('You created new squad with a captain {} and his {} privates ...'.format(
                    tag.tag, countOfPrivates))
                print('Now your total shield = ', self.shield)
                break

    def situation(self):
        if any(len(elem) > 1 for elem in trench_dic.values()):
            for i in trench_dic.values():  # to inform if there are two squads in same trench
                if len(i) > 1:
                    for j in i:
                        if len(j) > 3:
                            print(j)
        else:
            print("There are no two squad in same trench")

    def choice_captain(self):  # select captain and which trench he is attacking
        keysListe = list()
        for i in trench_dic.keys():
            keysListe.append(i)
        while True:
            print('Captain tags = ', end='')
            for i in self.captains:
                print(i.tag, end='    ')
            while True:
                try:
                    who, to = input(
                        '\nChoose a captain and a trench to attack(use space between this two choices) : ').split()
                    break
                except ValueError:
                    print("No valid integer! Please try again ...")
            who = who.upper()
            for attack_captain in self.captains:  # if selected captain in list of captains
                if attack_captain.tag == who and to in keysListe:
                    # captain move method çağrılır
                    attack_captain.move(to, attack_captain)
                    return attack_captain, to  # return attack_captain as an object
            else:
                print('check your order')

    # firstly if enemy is colonel in the trench, attack him. if not, attack enemy captain.if not return 'The trench is clear'
    def defense_captain(self, to, enemy_colonel):
        for keyInTrencDic in trench_dic[to]:
            if keyInTrencDic == enemy_colonel.tag:  # enemy colonel
                print('Attack on enemy colonel')
                return enemy_colonel
            elif keyInTrencDic in enemy_colonel.captainsNameList:  # enemy captain
                print('Attack on enemy captain')
                for objOfEnemyCaptain in enemy_colonel.captains:
                    if objOfEnemyCaptain.tag == keyInTrencDic:
                        return objOfEnemyCaptain
        else:
            return 'The trench is clear'

    # if you attack enemy colonel, subtract the values of total_fire from his shield values
    def damage_colonel(self, total_fire, enemy_colonel):
        val = getattr(enemy_colonel, 'shield')
        setattr(enemy_colonel, 'shield', val - total_fire)
        if getattr(enemy_colonel, 'shield') <= 0:
            print(f"YOU WIN {getattr(enemy_colonel,'tag')} WAS KILLED !!!")
            quit()
        print(f"{getattr(enemy_colonel,'tag')} was damaged.")


# clash functions is out of all class
def clash(colonel, enemy_colonel):

    if len(colonel.captains) == 0:  # if attack colonel has any squad
        print("You don't have any captain to give order")
        return
    else:
        colonel.situation()
        attack_captain, to = colonel.choice_captain()
        enemy = colonel.defense_captain(to, enemy_colonel)
        if not enemy == 'The trench is clear':  # if trench is not clear
            total_fire = attack_captain.squad_attack()
            if enemy.tag == enemy_colonel.tag:  # if enemy is colonel
                enemy_colonel.damage_colonel(
                    total_fire, enemy_colonel)
                if enemy_colonel.shield == 0:
                    print(f"{colonel} WINS THE BATTLE !!!")
                    quit()
            else:
                enemy.damage_squad(total_fire)  # if enemy is captain
                if enemy.shield == 0:
                    # when shield is 0  remove captain all lists
                    enemy_colonel.captains.remove(enemy)
                    print(f"{enemy.tag} was removed to enemy captains list")
                    enemy_colonel.captainsNameList.remove(enemy.tag)
                    trench_dic[enemy.trench_list[-1]].remove(enemy.tag)
                    objects_dic[enemy.trench_list[-1]].remove(enemy)
                    print(objects_dic)
        else:
            return "Trench is clear so you cant attact anyone"


# Instantiating Objects WEST AND EAST GARRISONS
west = Colonel('WEST', '0')
trench_dic['0'].append(west.tag)
objects_dic["0"].append(west)
east = Colonel('EAST', '9')
trench_dic['9'].append(east.tag)
objects_dic["9"].append(east)

# for turn
turn = random.randint(0, 1)


while True:
    if turn % 2:
        colonel, enemy_colonel = west, east
    else:
        colonel, enemy_colonel = east, west
    print(100*"=")
    print("TURN ;", colonel.tag.upper())
    print("INFORMATION ABOUT THE GARRISON;", colonel.__dict__)
    turn_move = input('''
1 to review the reports,
2 to change your trench warfare,
3 to create a new squad at your garrison,
4 to attack the enemy,

Enter Your Choice : ''')

    if turn_move == '1':
        colonel.review_reports()
    elif turn_move == '2':
        turn += 1
        print('\nYour trench warfare is ', getattr(
            colonel, 'trench'))
        while True:
            try:
                to = int(input('To where : '))
                if to not in range(10):
                    raise ValueError()
                break
            except (ValueError, KeyError):
                print(
                    "Enter numbers in trench list which are between 0 to 9! Please try again ...")
        to = str(to)
        colonel.move(to, colonel)
    elif turn_move == '3':
        turn += 1
        colonel.new_squad(colonel)
    elif turn_move == '4':
        turn += 1
        clash(colonel, enemy_colonel)
    else:
        print("1, 2, 3 or 4 are valid number! Please try again ...")
    print('\n'*3)
