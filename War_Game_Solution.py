import random

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'Q', 'P', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']
# Alphabet is for the IDs of the soldiers.

number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# Number list is for the trenches.

trench_list = {}  # We define a dictionary for recording the trenches and the colonels and captains inside them.
for i in range(10):  # We use for loop to add trench(key)-squad list(value) pair to the dictionary.
    trench_list[str(i)] = []
# for ex=> trench_list = {'1':[captain-1], '2':[], '3':['captain-2', 'captain-3'], '4': [],}


class Private:  # We define a parent class for private soldiers.
    Class_name = 'Private'

    def __init__(self, tag, commander):  # We define instance attributes of tag, commander, shield and ammo.
        self.tag = tag
        self.commander = commander
        self.shield = random.randint(25, 40)  # We define shield as random.
        self.ammunition = 50  # We define ammo attribute as 50.

    def attack(self, order):  # We define a method of attack based on the number of bullets order by the captain.
        fire = min(self.ammunition, order)
        # If the ammo of the private is smaller than the order, private can use the ammo left.
        self.ammunition -= fire  # We deduct the used ammo from the total ammo that each private has.
        if self.ammunition == 0:  # If the private runs out of ammo, the soldier is considered as out of game.
            self.shield = 0
        return fire  # We return fire as the output of this method.


class Captain(Private):  # We define a captain class as a subclass of Private class.
    Class_name = 'Captain'

    def __init__(self, tag, commander):
        super().__init__(tag, commander)  # We inherit the instance attributes of Private class.
        self.shield = random.randint(40, 50)  # We define shield as random.
        self.squad = []  # We define a list for recording captain's squad (privates).
        self.trench = []  # We define a list for recording captain's movements in trenches.
        self.commander = commander.tag  # We define the tag for captain's commander (colonel).

    def report(self):  # We define a method of report to give reports to the colonel.
        self.total_shield = self.shield  # We define a variable for total shield and first add captain's shield.
        self.total_ammunition = self.ammunition  # We define a variable for total ammo and first add captain's ammo.
        for soldier in self.squad:  # We use for loop to call elements in the squad list of captain.
            self.total_shield += soldier.shield  # We add shield and ammo of elements of squad to total shield and ammo.
            self.total_ammunition += soldier.ammunition
        colonel.reports[self.tag] = [len(self.squad), self.total_shield, self.total_ammunition, self.trench]
        # We call the reports instance attribute of colonel defined as a dictionary and the info of the squad.
        # self.tag (key) gives the tag of the captain.

    def move(self, to, captain):  # We define a method to move the captain and his squad.
        trench_list[to].append(captain)  # We add the captain to his new place in the trench dict defined at the top.
        if len(self.trench) != 0:  # If he was already in a trench, we remove him from last trench in the trench list.
            trench_list[self.trench[-1]].remove(captain)
        if to not in self.trench:  # We add this trench also to the trench list of the captain.
            self.trench.append(to)

    def squad_attack(self):  # We define a method to attack as a squad.
        total_fire = 0  # At the beginning, we define total fire as 0.
        order = int(input("How much ammunition will you attack with?"))  # We get an input for the order of ammo.
        for i in self.squad:  # We reach to the each member of squad.
            fire = i.attack(order)  # We call the attack method of Private class to return fire for each private .
            total_fire += fire  # We add fire power of each private to total fire power.
            if i.ammunition == 0:  # If ammo of a private is 0, we remove him from the squad.
                self.squad.remove(i)
                print(f'The ammunition of private {i} has been exhausted and he was out of war.')
        self.ammunition -= min(self.ammunition, order)  # We also add the captain's fire power.
        total_fire += min(self.ammunition, order)
        return total_fire  # We return total fire as the output of this method.

    def damage(self, total_hit):  # We define a method to calculate the total damage to the enemy.
        for enemy_soldier in self.squad:  # We call each soldier in the enemy army squad (enemy.squad).
            enemy_soldier.shield -= min(enemy_soldier.shield, total_hit)
            # We decrease shield level of each soldier, for this we take min of soldier shield and total hit.
            total_hit -= min(enemy_soldier.shield, total_hit)
            # We decrease total hit by the min value used above.
            if enemy_soldier.shield == 0:  # If the shield of a soldier is 0, this soldier is dead.
                print(f"Enemy solider {enemy_soldier.tag} has been killed.")
                self.squad.remove(enemy_soldier)
        print(f"{self.tag} squad was damaged.")


class Colonel(Private):  # We inherit Colonel class from Private class.
    Class_name = 'Colonel'

    def __init__(self, tag, garrison, trench):  # We define instance attributes for Colonel class.
        self.garrison = garrison
        self.tag = tag
        self.shield = 1000  # We define his shield as 1000.
        self.trench = []  # We define a list to record colonel's moves in different trenches.
        self.captains = []  # We define a list to record colonel's captains.
        self.reports = {}  # We define a dictionary to record reports from the captains.
        self.trench.append(trench)  # We add the colonel's trench to his trench list.

    def move(self, to):  # We define a method to change the trench of the colonel.
        if self.trench[-1] == to:  # If colonel is already in that trench, we give a warning.
            print(f"You are already in trench {to}.")
        else:  # Otherwise, we add colonel to his trench list.
            self.trench.append(to)
            print(f"You are in trench {to} now.")

    def review_reports(self):  # We define a method to get reports from all captains.
        for i in self.captains:  # We call report method for each captain to add them to the dictionary of reports.
            i.report()
        print('\n' * 2, '*' * 10)
        for i in self.reports.keys():  # We call report of each captain from the dictionary of reports.
            # We have a list of reports as value for each key.
            print(f"""Captain = {i}
Squad size = {self.reports[i][0]}
Total shield = {self.reports[i][1]}
Total ammunition = {self.reports[i][2]}
Trench = {self.reports[i][3]}""")
            print("*" * 10)
        else:
            print("*" * 20, "\n" * 2)

    def new_squad(self, colonel):  # We define a method to create new squad. We use the colonel as a parameter.
        print("Make a new squad.")
        while True:
            print("Total shield = ", self.shield)
            if self.shield <= 50:  # We need 50 and 25 points of shield for captain and each private respectively.
                print("You don't have enough shield to set up new squad.")
                break
            size = int(input("Size of new squad is ..."))
            if self.shield <= 50 + size * 25:
                print("You don't have enough shield to set up new squad of this size.")
            else:
                self.shield -= 50 + size * 25  # If there is enough shield, we deduct it from colonel's total shield.
                tag = random.choice(alphabet) + random.choice(alphabet)  # We use random.choice to form tag for squads.
                tag_list = [tag + str(i) for i in range(size)]  # We form a tags list for each private in the squad.
                tag = Captain(tag, colonel)  # We assign tag for the captain and we create an object of captain.
                self.captains.append(tag)  # We add the captain to the captains list of colonel.
                tag.squad.append(tag)  # We add the tag of captain to his squad list.
                for i in tag_list:
                    i = Private(i, tag)  # We form objects of privates with their tags and captain as their commander.
                    tag.squad.append(i)  # We add the tags of privates to captain's squad list.
                break

    def situation(self):  # We define a method to print tags of squads if there's more than one squad in a trench.
        for i in trench_list.values():
            if len(i) > 1:
                for j in i:
                    print(j.tag)

    def choice_captain(self):  # We define a method to choose a captain to give an order.
        while True:
            print("Captain tags = ", end='')  # First, we print the tags of the captains.
            for i in self.captains:
                print(i.tag, end='---')
            print()
            who, to = input("Choose a captain and a trench to attack (please use space between them.").split()
            # We take input for the tag of the captain and trench to make a move.
            who = who.upper()
            for attack_captain in self.captains:  # We use a for loop to look into the captains list of colonel.
                if attack_captain.tag == who and to in number_list:  # We make sure that who and to are consistent.
                    attack_captain.move(to, attack_captain)  # Then, we call the move method of Captain class.
                    return attack_captain, to  # We return the tag of the captain and the order of trench as output.
            else:  # If the order is not consistent with the records, we give a warning.
                print("Please check your order.")

    def defense_captain(self, to, enemy_colonel):
        # We define a method to select the enemy colonel or captain during an attack.
        for enemy in trench_list[to]:  # We look into trench_list to check if the order matches with an enemy trench.
            if enemy == enemy_colonel:  # If we find enemy colonel in the trench, we attack on enemy colonel.
                print("Attack on enemy colonel.")
                return enemy  # Then, we return output as the enemy colonel.
            elif enemy.commander == enemy_colonel.tag:
                # Otherwise, we check if the captain's commander in the trench is the same as enemy colonel.
                print('Attack on enemy captain.')
                return enemy  # Then, we return output as the enemy captain.
        else:
            print("The trench is clear.")

    def damage(self, total_fire, enemy_colonel):  # We define a method to execute damage on enemy colonel.
        # enemy_colonel.shield -= total_fire
        val = getattr(enemy_colonel, 'shield')  # We define a variable that's equal to enemy colonel's shield.
        setattr(enemy_colonel, 'shield', val - total_fire)  # Then, we deduct the total fire from his shield.
        if getattr(enemy_colonel, 'shield') <= 0:  # If the shield of enemy colonel becomes 0, enemy is defeated.
            print(f"{getattr(enemy_colonel, 'garrison')} is defeated.")
            quit()  # The game is over.
        print(f"{getattr(enemy_colonel, 'garrison')} is damaged.")  # Otherwise, enemy colonel is damaged.


def clash(colonel, enemy_colonel):  # We define a function to simulate clash between two squads.
    colonel.situation()  # First, we look at the situation whether two enemy squads are in the same trench.
    if len(colonel.captains) == 0:  # If colonel does not have any captain, we get out of the function.
        print("You don't have any captain to give order.")
        return
    else:  # If colonel have any captain, we call the choice_captain and defense_captain methods.
        attack_captain, to = colonel.choice_captain()
        # We set attack_captain and to parameters as the parameters of the choice_captain method.
        enemy = colonel.defense_captain(to, enemy_colonel) # We set enemy as the parameters of defense_captain method.
        if enemy:  # If there is enemy in the ordered trench, we call the squad attack method of captain.
            total_fire = attack_captain.squad_attack()
            if enemy.tag == enemy_colonel.tag:
                # If there is enemy colonel in the trench, we call the damage method of colonel.
                enemy_colonel.damage(total_fire, enemy_colonel)
            else:  # Otherwise, we call the damage method of captain.
                enemy.damage(total_fire)
                if enemy.shield == 0:
                    # If the shield of enemy captain becomes 0, we remove him from captains list and trench.
                    enemy_colonel.captains.remove(enemy)
                    trench_list[enemy.trench[-1]].remove(enemy)


west = Colonel('West', 'Garrison West', 0)  # First, we create two objects from colonel class.
trench_list['0'].append(west)  # We, assign colonels to different trenches.
east = Colonel('East', 'Garrison East', 9)
trench_list['9'].append(east)
turn = random.randint(0, 1)  # We start the game randomly.
while True:
    if turn % 2:
        colonel, enemy_colonel = west, east
    else:
        colonel, enemy_colonel = east, west

    print(colonel.tag.upper())  # We write the tag of the colonel.
    print(colonel.__dict__)  # We use this to write all attributes of the colonel.
    hamle = input("""Please enter:
1- to see reports
2- to change the trench
3- to make a new squad
4- to attack
************************************""")  # We define a menu for the game.
    if hamle == '1':
        colonel.review_reports()
    elif hamle == '2':
        turn += 1
        to = input('To where you want to move?: ')
        print("Your trench is ", getattr(colonel, 'trench'))
        colonel.move(to)
    elif hamle == '3':
        turn += 1
        colonel.new_squad(colonel)
    elif hamle == '4':
        turn += 1
        clash(colonel, enemy_colonel)
    else:
        print(trench_list)
        print('\n' * 5)
