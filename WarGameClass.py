import random
alphabet = ['A','B','C','D','E','F','G','H','Q','W',
          'R','T','Y','U','I','O','P','S','F','J',
          'K','L','Z','X','V','N','M']

number_list = ['0','1','2','3','4','5','6','7','8','9']


trench_list = {}
for i in range(10):                   ###### trenches are created as a dictionary
    trench_list[str(i)] = []

# trench_list = {'1':[captain-1],'2':[ ],'3':[captain-2,captain-3],'4':['captan amerika'],}

class Private:                        ###### private class is parent class
    Class_name = 'Private'
    def __init__(self, tag, commander):
        self.tag = tag
        self.commander = commander
        self.shield = random.randint(25, 40)
        self.ammunition = 50

    def attack(self, order):           #### number of shells for attack from commander with order
        fire = min(self.ammunition, order)
        self.ammunition -= fire
        if self.ammunition == 0:
            self.shield = 0
        return fire

class Captain(Private):               ##### captain class,subclass of private
    Class_name = 'Capatain'
    def __init__(self, tag, commander):
        super().__init__(tag, commander)
        self.shield = random.randint(40, 50)
        self.squad = []
        self.trench = []
        self.commander = commander.tag

    def report(self):                  #### reports to the commander
        self.total_shield = self.shield
        self.total_ammunition = self.ammunition
        for soldier in self.squad:
            self.total_shield += soldier.shield
            self.total_ammunition += soldier.ammunition
        colonel.reports[self.tag] = [len(self.squad), self.total_shield, self.total_ammunition, self.trench]

    def move(self, to, captain):
        trench_list[to].append(captain)       ##### captain adds a new place to the trench dictionary
        if len(self.trench) != 0:             #####and deletes it from the previous place
            trench_list[self.trench[-1]].remove(captain)
        if to not in self.trench:
            self.trench.append(to)            ##### if it is a new trench added to its trench list
    def squad_attack(self):
        total_fire = 0
        order = int(input('How much ammunition will you attack with?')) # order=10
        for i in self.squad:      #### The attack method is executed for each individual in the squad list
            fire = i.attack(order)
            total_fire += fire
            if i.ammunition == 0:     #### deleting the reset manga list
                self.squad.remove(i)
                print(f'The ammunition of private {i} has been exhausted and he was out of war.')
        self.ammunition -= min(self.ammunition,order)  #### captain throws a bullet
        total_fire += min(self.ammunition,order)
        return total_fire


    def damage(self, total_hit):      ##### Damage to enemies as total_hit
        for enemy_soldier in self.squad:    #### will be called enemy.squad and for each soldier
            enemy_soldier.shield -= min(enemy_soldier.shield, total_hit)
            total_hit -= min(enemy_soldier.shield, total_hit)
            if enemy_soldier.shield == 0:
                print(f'Enemy soldier {enemy_soldier.tag} has been killed')
                self.squad.remove(enemy_soldier)
        print(f"{self.tag} squad was damaged.")


class Colonel(Private):      ######class of colonel,subclass of private
    Class_name = 'Colonel'

    def __init__(self, tag, garrison, trench):   ####we did not use super since it will not be a commander
        self.garrison = garrison
        self.tag = tag
        self.shield = 1000
        self.trench = []
        self.captains = []
        self.reports = {}
        self.trench.append(trench)

    def move(self, to):       ###### change colonel trench method
        if self.trench[-1] == to:
            print(f'You are alreday in trench {to}.')
        else:
            self.trench.append(to)
            print(f'You are in trench {to} now.')

    def review_reports(self):     ##### view all reports from captains
        for i in self.captains:
            i.report()            #### Running report method for each captain in captains list
        print('\n'*2,'*'*10)
        for i in self.reports.keys():    #### raports was a dictionary
            print(f'''Captain = {i}
Squad size = {self.reports[i][0]}       
Total shield = {self.reports[i][1]}
Total ammunition = {self.reports[i][2]}
Trench = {self.reports[i][3]}''')
            print('*'*10)
        else:
            print('*'*20,'\n'*2)
    # reports = {'captain-1'=[5,200,300,[1,3,7]],
    #             'captain-2' = [6,300,250,[2]]}
# captain=50
# private=25

    def new_squad(self, colonel):       ##### create a new squad
        print('Make a new squad.')
        while True:
            print('Total sheild = ', self.shield)
            if self.shield <= 50:
                print("You don't have shield to set up new squad")
                break
            size = int(input('Size of new squad is ...'))
            if self.shield <= 50 + size * 25:
                print("You don't have shield to set up new squad of this size")
            else:
                self.shield -= 50 + size * 25
                tag = random.choice(alphabet) + random.choice(alphabet)  # XN
                tag_list = [tag + str(i) for i in range(size)]   #### creating tags for the new squad to be created
                # XN0,XN1,XN2
                tag = Captain(tag, colonel)    #### cA new captain from captain class
                self.captains.append(tag)
                tag.squad.append(tag)         #### tag captain was the name. own name added to squad list
                for i in tag_list:
                    i = Private(i, tag)       ### Private class privates occurred
                    tag.squad.append(i)
                break


    def situation(self):
        for i in trench_list.values():       #### if there are more than one squad in a trench
            if len(i)>1:
                for j in i:
                    print(j.tag)


    def choice_captain(self):
        while True:
            print('Captain tags = ', end='')
            for i in self.captains:
                print(i.tag, end='---')
            print()
            who,to = input('Choice a captain and a trench to attack(use space)').split()
            # XN 3
            #who=XN to=3
            who = who.upper()
            for attack_captain in self.captains:    ### If the selected captain is in the captains list
                if attack_captain.tag == who and to in number_list:
                    attack_captain.move(to, attack_captain)  #### captain move method is called
                    return attack_captain, to
            else:
                print('check your order')

    def defense_captain(self, to, enemy_colonel):   ###enemy selection
        for enemy in trench_list[to]:
            if enemy == enemy_colonel:            ### enemy colonel
                print('Attack on enemy colonel')
                return enemy
            elif enemy.commander == enemy_colonel.tag:  ### enemy captain
                print('Attack on enemy captain')
                return enemy
        else:
            print('The trench is clear')

    def damage(self, total_fire, enemy_colonel):   ###attack on enemy colonel
        # enemy_colonel.shield -= total_fire
        val = getattr(enemy_colonel, 'shield')
        setattr(enemy_colonel, 'shield', val-total_fire)
        if getattr(enemy_colonel, 'shield') <= 0:
            print(f"{getattr(enemy_colonel,'garrison')} was defeated.")
            quit()
        print(f"{getattr(enemy_colonel,'tag')} was damaged.")

def clash(colonel, enemy_colonel):     #### clash function
    colonel.situation()
    if len(colonel.captains) == 0:   ### Is there a squad squad that will colonize the raft
        print("You don't have any captain to give order")
        return
    else:
        attack_captain, to = colonel.choice_captain() ###colonel method choice method attack captain and return the value
        enemy = colonel.defense_captain(to, enemy_colonel)   ### defense captain method for enemy
        if enemy:                            #### If a value was returned for enemy
            total_fire = attack_captain.squad_attack()   ### captain class's squad attack method for total_fire
            if enemy.tag == enemy_colonel.tag:
                enemy_colonel.damage(total_fire, enemy_colonel) ###if it is enemy colonel
            else:
                enemy.damage(total_fire)   ###if it is enemy captain
                if enemy.shield == 0:
                    enemy_colonel.captains.remove(enemy) ### Removes captain from the list when shield is reset
                    trench_list[enemy.trench[-1]].remove(enemy)

west = Colonel('West','Garrison West', 0)
trench_list['0'].append(west)
east = Colonel('East', 'Garrison East', 9)
trench_list['9'].append(east)
turn = random.randint(0,1)
while True:
    if turn%2:
        colonel, enemy_colonel = west, east
    else:
        colonel, enemy_colonel = east, west

    print(colonel.tag.upper())
    print(colonel.__dict__)
    hamle = input('''
1 to see the reports,
2 to change the trench,
3 to make a new squad,
4 to attack
**********************''')
    if hamle == '1':
        colonel.review_reports()
    elif hamle == '2':
        turn +=1
        to = input('to where')
        print('your trench is ', getattr(colonel, 'trench'))
        colonel.move(to)
    elif hamle == '3':
        turn += 1
        colonel.new_squad(colonel)
    elif hamle == '4':
        turn += 1
        clash(colonel, enemy_colonel)
    else:
        print(trench_list)
    print('\n'*5)
