import random
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','X','Q','W','V','Y','Z']
number_list=['1','2','3','4','5','6','7','8','9','0']

trench_list={}
for i in range(10):#siperler bir sozluk olarak olusturulur.
    trench_list[str(i)]=[]
# trench_list = {'1':[captain-1],'2':[ ],'3':[captain-2,captain-3],'4':['captan amerika'],}

class Private:#private class => parent class
    Class_name='Private'
    def __init__(self,tag,commander):
        self.tag=tag
        self.commander=commander
        self.shield=random.randint(25,40)
        self.ammunition=50

    def attack(self,order):#order ile komutandan saldiri icin mermi sayisi
        fire=min(self.ammunition,order)
        self.ammunition-=fire
        if self.ammunition==0:
            self.shield=0
        return fire

class Captain(Private):#captain class <= private sub class
    Class_name='Captain'
    def __init__(self,tag,commander):
        super().__init__(tag,commander)
        self.shield=random.randint(40,50)
        self.squad=[]
        self.trench=[]
        self.commander=commander.tag

    def report(self):#komutana rapor veriyor
        self.total.shield=self.shield
        self.total_ammunition=self.ammunition
        for soldier in self.squad:
            self.total_shield+=soldier.shield
            self.total_ammunition+=soldier.ammunition
        colonel.reports[self.tag]=[len(self.squad),self.total_shield,self.total_ammunition,self.trench]

    def move(self,go_to,captain):
        trench_list[go_to].append(captain)#kaptani siper sozlugunde yeni bir yere ekliyor

        if len(self.trench)!=0:
            trench_list[self.trench[-1]].remove(captain)#ve onceki yerden siliyor
        if to not in self.trench:
             self.trench.append(go_to)#eger yeni bir siper ise kendi siper listesine ekliyor

    def squad_attack(self):
        total_fire=0
        order=int(input('How much ammunition will you attack with?'))#order=10
        for i in self.squad: #squad listesinde her bir er icin attack methodu calistiriliyor.
            fire=i.attack(order)
            total_fire+=fire
            if i.ammunition==0:#shieldi sifirlanan er boluk(squad) listesinden siliniyor.
                self.squad.remove(i)
                print("The ammunition of private {} has been exhausted and he was out of war.".format(i))
                self.ammunition-=min(self.ammunition,order)#kaptan mermi atiyor.
                total_fire+=min(self.ammunition,order)
                return total_fire

    def damage(self,total_hit): #total_hit kadar dusmana zarar verilecek.
        for enemy_soldier in self.squad: #enemy.squad olarak cagrilacak ve her bir er icin
            enemy_soldier.shield-=min(enemy_soldier.shield,total_hit)
            total_hit-=min(enemy_soldier.shield,total_hit)
            if enemy_soldier.shield==0:
                print("Enemy soldier {} has been killed.".format(enemy_soldier.tag))

                self.squad.remove(enemy_soldier)
        print("{} squad was damaged.".format(self.tag))


class Colonel(Private):  #colonel class <= private sub class
    Class_name='Colonel'
    def __init__(self,tag,garrison,trench): #commander olmayacagi iicn supe kullanmadik
           self.garrison=garrison
           self.tag=tag
           self.shield=1000
           self.trench=[]
           self.captains=[]
           self.reports={}
           self.trench.append(trench)

    def move(self,go_to): #colonel siper degsitir methodu
        if self.trench[-1]==go_to:
            print("You are already in trench {}".format(go_to))
        else:
            self.trench.append(go_to)
            print("You are in trench {} now".format(go_to))

    def review_reports(self): # kaptanlardan tum raporlari goruntule
        for i in self.captains:
            i.raport() #captains listesindeki her bir kaptan icin report method calistirliyor.
        print('\n'*2,'*'*10)
        for i in self.reports.keys():#reports bir sozluktu.
            print("""Captain={}
            Squad size={}
            Total shield={}
            Total ammunition={}
            Trench={}
            """.append(i,self.reports[i][0],self.reports[i][1],self.reports[i][2],self.reports[i][3]))
            print('*'*10)

        else:
            print('*'*20,'\n'*2)

# reports = {'captain-1'=[5,200,300,[1,3,7]],  'captain-2' = [6,300,250,[2]]}

#captain=50
#private=25

    def new_squad(self,colonel): #yeni bir boluk(squad) olusturur.
        print('Make a new squad.')
        while True:
            print('Total shield=',self.shield)
            if self.shield<=50:
                print("You don't have shield to set up new squad")
                break
            size=int(input('Size of new squad is ...'))
            if self.shield<=50+size*25:
                print("You don't have shield to set up new squad of this size")
            else:
                self.shield-=50+size*25
                tag=random.choice(alphabet)+random.choice(alphabet) #XN
                tag_list=[tag+str(i) for i in range(size)] #XN0,XN1,XN2
                tag=Captain(tag,colonel)#captain classindan yeni kaptan
                self.captains.append(tag)#tag kaptanin etiketi idi. squad listesine kendi etiketi eklendi.
                for i in tag_list:
                    i=Private(i,tag)#private class dan erler olustu.
                    tag.squad.append(i)
                break

    def situation(self):
        for i in trench_list.values():#bir siperde birden fazla squad varsa
            if len(i)>1:
                for j in i:
                    print(j.tag)

    def choice_captain(self):
        while True:
            print('Captain tags=',end='')
            for i in self.captains:
                print(i.tag,end='---')
                who,go_to=input('Choice acaptain and a trench to attack(use space)').split()
                #XN3
                #who=XN go_to=3
                who=who.upper()
                for attack_captain in self.captains: #secilen kaptan kaptan listesinde var ise
                    if attack_captain.tag==who and go_to in number_list:
                        attack_captain.move(go_to,attack_captain) #captain move method cagrilir
                        return attack_captain,go_to
                    else:
                        print('Check your order')

    def defence_captain(self,go_to,enemy_colonel): #enemy secimi
        for enemy in trench_list[go_to]:
            if enemy==enemy_colonel: #enemy colonel
                print('Attack in enemy colonel')
                return enemy
            elif enemy.commander==enemy_colonel.tag:# enemy captain
                print('Attack on enemy captain')
                return enemy

        else:
            print('The trench is clear')

    def damage(self,total_fire,enemy_colonel): #enemy colonele saldiri
        #enemy_colonel.shield-=total_fire
        val=getattr(enemy_colonel,'shield')
        setattr(enemy_colonel,'shield',val-total_fire)
        if getattr(enemy_colonel,'shield')<=0:
            print("{} was defeated".format(getattr(enemy_colonel,'garrison')))
            quit()
        print("{} was damaged".format(getattr(enemy_colonel,'tag')))

def clash(colonel,enemy_colonel): #clash fonksiyonu
    colonel.situation()
    if len(colonel.captains)==0: #saldiri yapacak colonelin squad birligi var mi
        print("You don't have any captain to give order")
        return
    else:
        attack_captain, go_to=colonel.choice_captain() #colonel method choice method attack captain ve go_to degeri dondurur.
        enemy=colonel.defense_captain(go_to,enemy_colonel) #enemy icin defence_captain methodu
        if enemy: #enemy icin bir deger return edikdiyse
            total_fire=attack_captain.squad_attack() #total_fire için captain classın squad_attack methodu
            if enemy.tag==enemy_colonel.tag:
                     enemy_colonel.damage(total_fire,enemy_colonel) #enemy colonel ise
            else:
                enemy.damage(total_fire)#enemy captain ise
                if enemy.shield==0:
                    enemy_colonel.captains.remove(enemy)#shield sifirlaninca captaini listeden sil
                    trench_list[enemy.trench[-1]].remove(enemy)


west = Colonel('West', 'Garrison West', 0)
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
        turn += 1
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
    print('\n' * 5)
