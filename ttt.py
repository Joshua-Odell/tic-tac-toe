import random


mydic={1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6: " ", 7:" ", 8:" ", 9:" "}
temp=[1, 2, 3, 4, 5, 6, 7, 8, 9]
pieces={' ':0, 'X':1, 'O':2}

playing_choice=1
c=0
z=1
t=0
b=1

def occupied_o():
    c=random.choice(temp)
    if mydic[c]=='O':
        occupied_o()
    else:
        mydic[c]='O'

def playing():
    global mydic
    global temp
    print("Would you like to play again?")
    print("Press 1  to Play Again")
    print("Press 2  to Quit")
    playing_choice=int(input(">"))
    while playing_choice!=1 and playing_choice!=2:
        print("Please choose 1 or 2")
        playing_choice=int(input(">"))
    if playing_choice==1:
        mydic={1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6: " ", 7:" ", 8:" ", 9:" "}
        temp=[1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(mydic)
        print(temp)
    elif playing_choice==2:
        exit()



def occupied_x():
    c=random.choice(temp)
    if mydic[c]=='X':
        occupied_x()
    else:
        mydic[c]='X'

def choice():
    global y
    print("Would you rather start as X or O?")
    pc=input(">").upper()
    if pc=="X":
        print("Good Luck as X!")
        y=1
    elif pc=="O":
        print("Good Luck as O!")
        y=0
    else:
        y=2
        while y==2:
            print("I said X or O!")
            choice()

def display(board):
    print(mydic[7]+"|"+mydic[8]+"|"+mydic[9])
    print("-+-+-")
    print(mydic[4]+"|"+mydic[5]+"|"+mydic[6])
    print("-+-+-")
    print(mydic[1]+"|"+mydic[2]+"|"+mydic[3])

def evaluate():
    checkspaces(1,2,3)
    checkspaces(4,5,6)
    checkspaces(7,8,9)
    checkspaces(1,4,7)
    checkspaces(2,5,8)
    checkspaces(3,6,9)
    checkspaces(1,5,9)
    checkspaces(3,5,7)

def old_evaluate():
    global q
    global g
    if mydic[1]==mydic[2] and mydic[2]==mydic[3]:
        if mydic[3]=="X":
            q=1
            g=True
        if mydic[3]=="O":
            q=2
            g=True
        else:
            q=0
    elif mydic[4]==mydic[5] and mydic[5]==mydic[6]:
        if mydic[6]=="X":
            q=1
            g=True
        if mydic[6]=="O":
            q=2
            g=True
        else:
            q=0
    elif mydic[7]==mydic[8] and mydic[8]==mydic[9]:
        if mydic[9]=="X":
            q=1
            g=True
        if mydic[9]=="O":
            q=2
            g=True
        else:
            q=0
    elif mydic[1]==mydic[4] and mydic[4]==mydic[7]:
        if mydic[7]=="X":
            q=1
            g=True
        if mydic[7]=="O":
            q=2
            g=True
        else:
            q=0
    elif mydic[2]==mydic[5] and mydic[5]==mydic[8]:
        if mydic[8]=="X":
            q=1
            g=True
        if mydic[8]=="O":
            q=2
            g=True
        else:
            q=0
    elif mydic[3]==mydic[6] and mydic[6]==mydic[9]:
        if mydic[9]=="X":
            q=1
            g=True
        if mydic[9]=="O":
            q=2
            g=True
        else:
            q=0
    elif mydic[1]==mydic[5] and mydic[5]==mydic[9]:
        if mydic[9]=="X":
            q=1
            g=True
        if mydic[9]=="O":
            q=2
            g=True
        else:
            q=0
    elif mydic[3]==mydic[5] and mydic[5]==mydic[7]:
        if mydic[7]=="X":
            q=1
            g=True
        if mydic[7]=="O":
            q=2
            g=True
        else:
            q=0

def victory():
    evaluate()
    if q==1:
        print("Good Job Team X")
    if q==2:
        print("Good Job Team O")

def checkspaces(a,b,c):
    global q
    global g
    if not g and mydic[a]==mydic[b]==mydic[c]:
        q = pieces[mydic[c]]
        g = q != 0

def occupied(p):
    c=random.choice(temp)
    if mydic[c]==p:
        occupied(p)
    else:
        mydic[c]=p

def evaluate():
    checkspaces(1,2,3)
    checkspaces(4,5,6)
    checkspaces(7,8,9)
    checkspaces(1,4,7)
    checkspaces(2,5,8)
    checkspaces(3,6,9)
    checkspaces(1,5,9)
    checkspaces(3,5,7)

def computer_turn():

    c4pu = 'X' if y==0 else 'O'
    if   mydic[2]==mydic[3]!=' ' and mydic[1]==' ': mydic[1]=cpu
    elif mydic[5]==mydic[9]!=' ' and mydic[1]==' ': mydic[1]=cpu
    elif mydic[7]==mydic[4]!=' ' and mydic[1]==' ': mydic[1]=cpu
    elif mydic[1]==mydic[3]!=' ' and mydic[2]==' ': mydic[2]=cpu
    elif mydic[8]==mydic[5]!=' ' and mydic[2]==' ': mydic[2]=cpu
    elif mydic[1]==mydic[2]!=' ' and mydic[3]==' ': mydic[3]=cpu
    elif mydic[7]==mydic[5]!=' ' and mydic[3]==' ': mydic[3]=cpu
    elif mydic[9]==mydic[6]!=' ' and mydic[3]==' ': mydic[3]=cpu
    elif mydic[5]==mydic[6]!=' ' and mydic[4]==' ': mydic[4]=cpu
    elif mydic[1]==mydic[7]!=' ' and mydic[4]==' ': mydic[4]=cpu
    elif mydic[4]==mydic[6]!=' ' and mydic[5]==' ': mydic[5]=cpu
    elif mydic[1]==mydic[9]!=' ' and mydic[5]==' ': mydic[5]=cpu
    elif mydic[7]==mydic[3]!=' ' and mydic[5]==' ': mydic[5]=cpu
    elif mydic[8]==mydic[2]!=' ' and mydic[5]==' ': mydic[5]=cpu
    elif mydic[9]==mydic[3]!=' ' and mydic[6]==' ': mydic[6]=cpu
    elif mydic[4]==mydic[5]!=' ' and mydic[6]==' ': mydic[6]=cpu
    elif mydic[8]==mydic[9]!=' ' and mydic[7]==' ': mydic[7]=cpu
    elif mydic[3]==mydic[5]!=' ' and mydic[7]==' ': mydic[7]=cpu
    elif mydic[4]==mydic[1]!=' ' and mydic[7]==' ': mydic[7]=cpu
    elif mydic[5]==mydic[2]!=' ' and mydic[8]==' ': mydic[8]=cpu
    elif mydic[7]==mydic[9]!=' ' and mydic[8]==' ': mydic[8]=cpu
    elif mydic[1]==mydic[5]!=' ' and mydic[9]==' ': mydic[9]=cpu
    elif mydic[7]==mydic[8]!=' ' and mydic[9]==' ': mydic[9]=cpu
    elif mydic[6]==mydic[3]!=' ' and mydic[9]==' ': mydic[9]=cpu
    else:
        occupied(cpu)

def old_computer_turn():
    if y==1:
        if mydic[1]==mydic[2] and mydic[1]!=" " and  mydic[3]==' ':
            mydic[3]='O'
        elif mydic[2]==mydic[3] and mydic[2]!=" " and  mydic[1]==' ':
            mydic[1]='O'
        elif mydic[1]==mydic[3] and mydic[1]!=" " and  mydic[2]==' ':
            mydic[2]='O'
        elif mydic[4]==mydic[5] and mydic[4]!=" " and  mydic[6]==' ':
            mydic[6]='O'
        elif mydic[5]==mydic[6] and mydic[5]!=" " and  mydic[4]==' ':
            mydic[4]='O'
        elif mydic[4]==mydic[6] and mydic[4]!=" " and  mydic[5]==' ':
            mydic[5]='O'
        elif mydic[7]==mydic[8] and mydic[7]!=" " and  mydic[9]==' ':
            mydic[9]='O'
        elif mydic[8]==mydic[9] and mydic[8]!=" " and  mydic[7]==' ':
            mydic[7]='O'
        elif mydic[7]==mydic[9] and mydic[7]!=" " and  mydic[8]==' ':
            mydic[8]='O'
        elif mydic[1]==mydic[5] and mydic[1]!=" " and  mydic[9]==' ':
            mydic[9]='O'
        elif mydic[5]==mydic[9] and mydic[5]!=" " and  mydic[1]==' ':
            mydic[1]='O'
        elif mydic[1]==mydic[9] and mydic[1]!=" " and  mydic[5]==' ':
            mydic[5]='O'
        elif mydic[7]==mydic[5] and mydic[7]!=" " and  mydic[3]==' ':
            mydic[3]='O'
        elif mydic[7]==mydic[3] and mydic[7]!=" " and  mydic[5]==' ':
            mydic[5]='O'
        elif mydic[3]==mydic[5] and mydic[3]!=" " and  mydic[7]==' ':
            mydic[7]='O'
        elif mydic[7]==mydic[4] and mydic[7]!=" " and  mydic[1]==' ':
            mydic[1]='O'
        elif mydic[4]==mydic[1] and mydic[4]!=" " and  mydic[7]==' ':
            mydic[7]='O'
        elif mydic[1]==mydic[7] and mydic[1]!=" " and  mydic[4]==' ':
            mydic[4]='O'
        elif mydic[8]==mydic[5] and mydic[8]!=" " and  mydic[2]==' ':
            mydic[2]='O'
        elif mydic[5]==mydic[2] and mydic[5]!=" " and  mydic[8]==' ':
            mydic[8]='O'
        elif mydic[8]==mydic[2] and mydic[8]!=" " and  mydic[5]==' ':
            mydic[5]='O'
        elif mydic[9]==mydic[6] and mydic[9]!=" " and  mydic[3]==' ':
            mydic[3]='O'
        elif mydic[9]==mydic[3] and mydic[9]!=" " and  mydic[6]==' ':
            mydic[6]='O'
        elif mydic[6]==mydic[3] and mydic[6]!=" " and  mydic[9]==' ':
            mydic[9]='O'
        else:
            occupied_o()
    if y==0:
        if mydic[1]==mydic[2] and mydic[1]!=" " and  mydic[3]==' ':
            mydic[3]='X'
        elif mydic[2]==mydic[3] and mydic[2]!=" " and  mydic[1]==' ':
            mydic[1]='X'
        elif mydic[1]==mydic[3] and mydic[1]!=" " and  mydic[2]==' ':
            mydic[2]='X'
        elif mydic[4]==mydic[5] and mydic[4]!=" " and  mydic[6]==' ':
            mydic[6]='X'
        elif mydic[5]==mydic[6] and mydic[5]!=" " and  mydic[4]==' ':
            mydic[4]='X'
        elif mydic[4]==mydic[6] and mydic[4]!=" " and  mydic[5]==' ':
            mydic[5]='X'
        elif mydic[7]==mydic[8] and mydic[7]!=" " and  mydic[9]==' ':
            mydic[9]='X'
        elif mydic[8]==mydic[9] and mydic[8]!=" " and  mydic[7]==' ':
            mydic[7]='X'
        elif mydic[7]==mydic[9] and mydic[7]!=" " and  mydic[8]==' ':
            mydic[8]='X'
        elif mydic[1]==mydic[5] and mydic[1]!=" " and  mydic[9]==' ':
            mydic[9]='X'
        elif mydic[5]==mydic[9] and mydic[5]!=" " and  mydic[1]==' ':
            mydic[1]='X'
        elif mydic[1]==mydic[9] and mydic[1]!=" " and  mydic[5]==' ':
            mydic[5]='X'
        elif mydic[7]==mydic[5] and mydic[7]!=" " and  mydic[3]==' ':
            mydic[3]='X'
        elif mydic[7]==mydic[3] and mydic[7]!=" " and  mydic[5]==' ':
            mydic[5]='X'
        elif mydic[3]==mydic[5] and mydic[3]!=" " and  mydic[7]==' ':
            mydic[7]='X'
        elif mydic[7]==mydic[4] and mydic[7]!=" " and  mydic[1]==' ':
            mydic[1]='X'
        elif mydic[4]==mydic[1] and mydic[4]!=" " and  mydic[7]==' ':
            mydic[7]='X'
        elif mydic[1]==mydic[7] and mydic[1]!=" " and  mydic[4]==' ':
            mydic[4]='X'
        elif mydic[8]==mydic[5] and mydic[8]!=" " and  mydic[2]==' ':
            mydic[2]='X'
        elif mydic[5]==mydic[2] and mydic[5]!=" " and  mydic[8]==' ':
            mydic[8]='X'
        elif mydic[8]==mydic[2] and mydic[8]!=" " and  mydic[5]==' ':
            mydic[5]='X'
        elif mydic[9]==mydic[6] and mydic[9]!=" " and  mydic[3]==' ':
            mydic[3]='X'
        elif mydic[9]==mydic[3] and mydic[9]!=" " and  mydic[6]==' ':
            mydic[6]='X'
        elif mydic[6]==mydic[3] and mydic[6]!=" " and  mydic[9]==' ':
            mydic[9]='X'
        else:
            occupied_x()

def x_space():
    global a
    a=int(input(">"))
    if not isinstance(a,int): # I need  a  type check  for input here
        print("You need  to  pick a  number")
        x_space()
    if a>9 or  a<1:
        print("That space does not  exist")
        x_space()
    if mydic[a]=='X' or mydic[a]=='O':
        print("That space is already taken")
        x_space()
    if mydic[a]==' ':
        mydic[a]='X'
def y_space():
    global a
    a=int(input(">"))
    if mydic[a]=='X' or mydic[a]=='O':
        print("That space is already taken")
        y_space()
    if mydic[a]==' ':
        mydic[a]='O'

while playing_choice==1:
    display(mydic)
    choice()
    print("Please enter your choice with a number from the Number Pad representing the board")
    g=False
    while t<9 and g==False: #there is an empty space
        global y
        if y == 1:
            x_space()
            t+=1
            temp.pop(a-b)
            z+=1
            b+=1
            display(mydic)
            victory()
            if t==9:
                break
            computer_turn()
            t+=1
            print("-------")
            display(mydic)
            victory()

        elif y == 0:
            y_space()
            t+=1
            temp.pop(a-b)
            z+=1
            b+=1
            display(mydic)
            victory()
            if t==9:
                break
            computer_turn()
            t+=1
            print("------")
            display(mydic)
            victory()

        else:
            print('ERROR')



    if  t==9 and g==False:
        print("ITS A DRAW!")
    print("GG")
    playing()
