def wrong():
    print("try again!")
def start():
    print('welcome to the fun cookie hunting adventure!')
    print('''⠀⠀⠀⠀⠀⠀⠀⢰⠒⠒⠒⠒⠒⠒⢲⡖⣶⣶⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⡀⣯⠉⠉⠉⣖⣲⣶⡆⠀⠀⠈⠉⠉⠉⠉⠉⠉⢱⠀⠀⠀⠀
⢀⣀⣸⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣇⣀⡀
⢸⣿⣀⣀⡀⠀⠿⠿⠀⠀⠀⣸⣙⣿⣿⠀⢸⣿⠀⠀⠀⠀⠀⠀⢰⡇
⢸⡿⠾⠿⠟⠀⠀⠀⣤⡄⠀⠸⠿⠿⠟⠀⠸⠿⠀⠀⠀⣠⣤⠀⢸⡇
⢸⡃⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠀⢸⡇
⢸⣖⠀⠀⠀⠀⠀⠀⠙⠋⠀⢴⣶⣶⣶⠀⠀⠀⣶⣶⠀⠀⠀⠀⢸⡇
⢸⣿⣶⠀⠀⠀⣶⣶⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⠉⠉⠀⠀⠀⣷⣾⡇
⠈⠉⢹⣿⣿⣀⣀⣠⠀⠀⠀⠀⠀⠀⠸⣿⡇⠀⣀⣀⣀⣿⣿⡏⠉⠁
⠀⠀⠀⠀⢿⠿⠿⢿⣀⣀⣀⣀⣠⣤⣤⣤⣤⣤⣿⠿⠿⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠿⠿⣿⣿⣿⣿⠿⠇⠀⠀⠀⠀⠀⠀⠀''')
    print('you had just arrived at your grandma\'s house and could smell the lovely homemade cookie aroma wafting through the house!\neveryone knows your grandma bakes the greatest cookies in the world! you really want to try them,\nbut your evil old grandma won\'t allow you!!\n\nthe cookies should be ready to be taken out of the oven in about 20 minutes,\nnow let\'s figure out how to get our hands on these delicious-smelling cookies!')
    foyer()

def foyer():
    print("\nyou are in the foyer room")
    move = input("\nwhere would you like to go? say one of these choices:\n\tliving room\n\tgrandma's bedroom\n\tbackyard\n")
    if move.lower() == "living room":
        biglivingroom()
    elif move.lower() == "grandma's bedroom":
        grandmasbedroom()
    elif move.lower() == "backyard":
        backyard()
    else:
        wrong()
        foyer()
        #TODO: what should happen if they type something else?
        pass

def backyard():
    print('''   
    __
o-''|\_____/)
 \_/|_)     )
    \  __  /
    (_/ (_/ ''')
    print('you are now at the backyard. it\'s a beautiful sunny day\nthe family dog is hanging out there\n\ndo you want to have some fun with him?')
    play = input("what would you like to do?:\n\tback to foyer\n\tpet the dog\n")
    if play.lower() == "back to foyer":
        foyer()
    if play.lower() == "pet the dog":
        print('''     
     |\_/|                  
     | @ @   Woof! 
     |   <>              _  
     |  _/\------____ ((| |))
     |               `--' |   
 ____|_       ___|   |___.' 
/_/_____/____/_______|''')
        play = input("we made the family's dog day, where do you want to go now?\n\tfoyer\n")
        if play.lower() == "foyer":
            foyer()
        else:
            wrong()
            backyard()
    else:
        wrong()
        backyard()
        pass

def livingroom():
    print("you're in the living room right now\nyou can see your drowsy granny over there, as usual, watching her favorite cooking TV show.\ni wonder what i can possibly do to distract her exhausted mind!\n")
    move = input("\nwhere would you like to go? say one of these choices:\n\tfoyer\n\tkitchen\n")
    if move.lower() == "foyer":
        foyer()
    elif move.lower() == "kitchen":
        kitchen()
    else:
        #TODO: what should happen if they type something else?
        wrong()
        livingroom()
        pass

def kitchen():
    print('''       
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________| 
           ''')
    print("this is grandma's property, she wont let you in...")
    goback = input('go back to living room\n')
    if goback == "go back to living room":
        livingroom()
    else:
        wrong()
        kitchen()


def grandmasbedroom():
    print('''  ()___
()//__/)_________________()
||(___)//#/_/#/_/#/_/#()/||
||----|#| |#|_|#|_|#|_|| ||  
||____|_|#|_|#|_|#|_|#||/||
||    |#|_|#|_|#|_|#|_||''')
    print("you are inside your grandma's bedroom, smells like old people and vitamin pills...\nyou notice a warm blue blanket neatly folded on her bed.\nyou decide to take it with you.")
    global have_blanket
    have_blanket = True
    move = input("\nwhere would you like to go? say one of these choices:\n\tfoyer\n")
    if move.lower() == "foyer":
        foyer_blanket()
    else:
        #TODO: what should happen if they type something else?
        wrong()
        grandmasbedroom()
        pass

def foyer_blanket():
    print("\nyou are in the foyer room")
    move = input("\nwhere would you like to go? say one of these choices:\n\tliving room\n\tgrandma's bedroom\n\tbackyard\n")
    if move.lower() == "living room":
        biglivingroom()
    elif move.lower() == "grandma's bedroom":
        grandmasbedroom_blanket()
    elif move.lower() == "backyard":
        backyard_blanket()
    else:
        wrong()
        foyer()
        #TODO: what should happen if they type something else?
        pass

def kitchen_blanket():
    print('''                                   .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :''')
    print("CONGRATULATIONS! You may finally enjoy your granny's outstanding, delicious, crunchy yet smooth cookies.!!!!\n\nthank you so much for playing ヘ(^o^ヘ)")

def after_sleep(): 
    aftersleep = input("\n\tfoyer\n\tkitchen\n")
    if aftersleep == "kitchen":
        kitchen_blanket()
    if aftersleep == "foyer":
        foyer_blanket()
    else:
        wrong()
        after_sleep()


def livingroom_blanket():
    blanket_yesorno = input("your grandma looks all cozy and sleepy, do you want to give her the warm puffy blanket to make her sleep!?!\n")
    if blanket_yesorno == "yes":
        print("mission complete! your grandma is asleep! go steal all the cookies you want before she wakes up!")
    after_sleep()

def biglivingroom():
    if have_blanket == False:
        livingroom()
    else:
        livingroom_blanket()
########
#main
#######
#TODO: Add some global variables
have_blanket = False 
start()

#"On my honor, I pledge that I have neither given nor received unauthorized information on this assignment. I did this work only for this assignment. If I have plagiarized, I will receive a zero for this project."