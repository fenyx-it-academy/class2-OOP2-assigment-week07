# class2-OOP2-assigment-week07
Code a battle game with using OOP in Python3
In this game, two military units-Garrisons(West - East) fight each other.
The both enemy garrisons  will consist of a colonel (class Colonel), captains (class Captain) and privates (class Private).
- The Battle Game arguments; Two Garrisons, Squads, Shield(Defense Force), Ammunition(Attack Force) and Trench warfares
- The aim of the battle is to kill the colonel of the Enemy Garrison.


## The Rules of Game
1 - Privates are the most active soldiers in this battle game.
- Instance Attributes of class Private; 
  tag(name of privates), 
  captain name, 
  shield (There are 25 values and the soldier whose defensive force is zero-0, is out of the battle game),
  ammunition (ammunition values-bullets are randomly between 20 to 30. Also if ammunition 0 it is not out of battle)
  trench
- Instance method of class Private;
  Attack; Attacks the enemy with as much as a number of bullets which are specified by the captain.
          The number of this bullets is subtracted from the ammunition of the private at the same value.
          Also, the same values is subtracted from the shield values of enemy private.


2 - Captain is commander of his own squad.
- Instance Attributes of class Captain;
  tag(name of captain), 
  colonel name, 
  the count of privates in his squad,
  shield (There are 50 values and if the captain defensive force is become zero-0, the captain and his squad will be out of the battle game),
  ammunition (ammunition values-bullets are randomly between 40 to 60. Also if ammunition 0 it is not out of battle.just attack empty value)
  trench,
  squad(list of privates object in his squad),
  trench list(list of trenches where captain has stayed so far)
- Instance method of class Captain;
  report; Reporting  the some situation to his Colonel
  move; to attack enemy move your trench to where you want to attack
  squad attack; attack enemy with your ordered ammunition value
  damage squad; damage the enemy as much as your total ammunition




3 - Colonel is the commander of his own garrison.
- Instance Attributes of class Colonel;
  tag(name of garrison),
  name list of his captains,
  trench,
  trench list(list of trenches where colonel has stayed so far),
  shield (defensive force value randomly between 950 to 1050. if the Colonel defensive force is become zero-0, the Colonel and his garrison will lose the battle game),
  captains object list,
  name of captains list
- Instance method of class Colonel;
  new squad; Colonel can create a new squad which has a captain and          privates  as much as your shield greater than 300. The number of privates are 5.Also, 50 values for one captain and 25 values for one private is subtracted from his shield values.)
  choice_captain;select captain and which trench he is attacking
  move;move your trench to where you want to escape or hide out or whatever your battle strategy is to do
  review reports; report all details of captain and his privates
  situation;to inform if there are two squads in same trench
  damage_colonel;if you attack enemy colonel, subtract the values of total_fire from his shield values 
  defense_captain; firstly if enemy is colonel in the trench, attack him. if not, attack enemy captain.if not return 'The trench is clear'

## The Details of Game

- There are totally  10 trenches for taking your position or attacking the enemy.Colonels take his position at the beginning of game. Also he can change his trench warfare. Captains and his privates take their trench when they are created. Also they can move their trench to where they want to attack.

- Colonel gives attack order to captain and tells captain where trench to attack. Colonel can change his trench and examine his squads to get reports.

- A colonel who has the game turn, can changes his position, can attack the enemy garrison, can create a new squad or review the reports. The last one of these moves does not spend your playing turn. 

## The Details of Python3 Codes
- Code this battle game with Object-Oriented Programming (OOP) in Python 3
- Python Classes,Object Instances, Defining and Working with Methods, OOP Inheritance topics can be reviewed.
- class, subclass, overriding, getattr,issubclass, isinstance, setattr etc.
you can use these concepts or methods in your code whichever you need.
- You can import any module you want.
- You can code the battle game one of the two ways.  You vs Computer (play against the computer)
or 2 Players Game(Player1 against Player2). 

