import random


dictionary={1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6: " ", 7:" ", 8:" ", 9:" "}
temp=[1, 2, 3, 4, 5, 6, 7, 8, 9]
pieces={' ':0, 'X':1, 'O':2}

playing_choice=1
c=0
z=1
t=0
b=1

def occupied_o():
    c=random.choice(temp)
    if dictionary[c]=='O':
        occupied_o()
    else:
        dictionary[c]='O'

def playing():
    global dictionary
    global temp
    print("Would you like to play again?")
    print("Press 1  to Play Again")
    print("Press 2  to Quit")
    playing_choice=int(input(">"))
    while playing_choice!=1 and playing_choice!=2:
        print("Please choose 1 or 2")
        playing_choice=int(input(">"))
    if playing_choice==1:
        dictionary={1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6: " ", 7:" ", 8:" ", 9:" "}
        temp=[1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(dictionary)
        print(temp)
    elif playing_choice==2:
        exit()



def occupied_x():
    c=random.choice(temp)
    if dictionary[c]=='X':
        occupied_x()
    else:
        dictionary[c]='X'

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
    print(dictionary[7]+"|"+dictionary[8]+"|"+dictionary[9])
    print("-+-+-")
    print(dictionary[4]+"|"+dictionary[5]+"|"+dictionary[6])
    print("-+-+-")
    print(dictionary[1]+"|"+dictionary[2]+"|"+dictionary[3])

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
    if dictionary[1]==dictionary[2] and dictionary[2]==dictionary[3]:
        if dictionary[3]=="X":
            q=1
            g=True
        if dictionary[3]=="O":
            q=2
            g=True
        else:
            q=0
    elif dictionary[4]==dictionary[5] and dictionary[5]==dictionary[6]:
        if dictionary[6]=="X":
            q=1
            g=True
        if dictionary[6]=="O":
            q=2
            g=True
        else:
            q=0
    elif dictionary[7]==dictionary[8] and dictionary[8]==dictionary[9]:
        if dictionary[9]=="X":
            q=1
            g=True
        if dictionary[9]=="O":
            q=2
            g=True
        else:
            q=0
    elif dictionary[1]==dictionary[4] and dictionary[4]==dictionary[7]:
        if dictionary[7]=="X":
            q=1
            g=True
        if dictionary[7]=="O":
            q=2
            g=True
        else:
            q=0
    elif dictionary[2]==dictionary[5] and dictionary[5]==dictionary[8]:
        if dictionary[8]=="X":
            q=1
            g=True
        if dictionary[8]=="O":
            q=2
            g=True
        else:
            q=0
    elif dictionary[3]==dictionary[6] and dictionary[6]==dictionary[9]:
        if dictionary[9]=="X":
            q=1
            g=True
        if dictionary[9]=="O":
            q=2
            g=True
        else:
            q=0
    elif dictionary[1]==dictionary[5] and dictionary[5]==dictionary[9]:
        if dictionary[9]=="X":
            q=1
            g=True
        if dictionary[9]=="O":
            q=2
            g=True
        else:
            q=0
    elif dictionary[3]==dictionary[5] and dictionary[5]==dictionary[7]:
        if dictionary[7]=="X":
            q=1
            g=True
        if dictionary[7]=="O":
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
    if not g and dictionary[a]==dictionary[b]==dictionary[c]:
        q = pieces[dictionary[c]]
        g = q != 0

def occupied(p):
    c=random.choice(temp)
    if dictionary[c]==p:
        occupied(p)
    else:
        dictionary[c]=p

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
    if   dictionary[2]==dictionary[3]!=' ' and dictionary[1]==' ': dictionary[1]=cpu
    elif dictionary[5]==dictionary[9]!=' ' and dictionary[1]==' ': dictionary[1]=cpu
    elif dictionary[7]==dictionary[4]!=' ' and dictionary[1]==' ': dictionary[1]=cpu
    elif dictionary[1]==dictionary[3]!=' ' and dictionary[2]==' ': dictionary[2]=cpu
    elif dictionary[8]==dictionary[5]!=' ' and dictionary[2]==' ': dictionary[2]=cpu
    elif dictionary[1]==dictionary[2]!=' ' and dictionary[3]==' ': dictionary[3]=cpu
    elif dictionary[7]==dictionary[5]!=' ' and dictionary[3]==' ': dictionary[3]=cpu
    elif dictionary[9]==dictionary[6]!=' ' and dictionary[3]==' ': dictionary[3]=cpu
    elif dictionary[5]==dictionary[6]!=' ' and dictionary[4]==' ': dictionary[4]=cpu
    elif dictionary[1]==dictionary[7]!=' ' and dictionary[4]==' ': dictionary[4]=cpu
    elif dictionary[4]==dictionary[6]!=' ' and dictionary[5]==' ': dictionary[5]=cpu
    elif dictionary[1]==dictionary[9]!=' ' and dictionary[5]==' ': dictionary[5]=cpu
    elif dictionary[7]==dictionary[3]!=' ' and dictionary[5]==' ': dictionary[5]=cpu
    elif dictionary[8]==dictionary[2]!=' ' and dictionary[5]==' ': dictionary[5]=cpu
    elif dictionary[9]==dictionary[3]!=' ' and dictionary[6]==' ': dictionary[6]=cpu
    elif dictionary[4]==dictionary[5]!=' ' and dictionary[6]==' ': dictionary[6]=cpu
    elif dictionary[8]==dictionary[9]!=' ' and dictionary[7]==' ': dictionary[7]=cpu
    elif dictionary[3]==dictionary[5]!=' ' and dictionary[7]==' ': dictionary[7]=cpu
    elif dictionary[4]==dictionary[1]!=' ' and dictionary[7]==' ': dictionary[7]=cpu
    elif dictionary[5]==dictionary[2]!=' ' and dictionary[8]==' ': dictionary[8]=cpu
    elif dictionary[7]==dictionary[9]!=' ' and dictionary[8]==' ': dictionary[8]=cpu
    elif dictionary[1]==dictionary[5]!=' ' and dictionary[9]==' ': dictionary[9]=cpu
    elif dictionary[7]==dictionary[8]!=' ' and dictionary[9]==' ': dictionary[9]=cpu
    elif dictionary[6]==dictionary[3]!=' ' and dictionary[9]==' ': dictionary[9]=cpu
    else:
        occupied(cpu)

def old_computer_turn():
    if y==1:
        if dictionary[1]==dictionary[2] and dictionary[1]!=" " and  dictionary[3]==' ':
            dictionary[3]='O'
        elif dictionary[2]==dictionary[3] and dictionary[2]!=" " and  dictionary[1]==' ':
            dictionary[1]='O'
        elif dictionary[1]==dictionary[3] and dictionary[1]!=" " and  dictionary[2]==' ':
            dictionary[2]='O'
        elif dictionary[4]==dictionary[5] and dictionary[4]!=" " and  dictionary[6]==' ':
            dictionary[6]='O'
        elif dictionary[5]==dictionary[6] and dictionary[5]!=" " and  dictionary[4]==' ':
            dictionary[4]='O'
        elif dictionary[4]==dictionary[6] and dictionary[4]!=" " and  dictionary[5]==' ':
            dictionary[5]='O'
        elif dictionary[7]==dictionary[8] and dictionary[7]!=" " and  dictionary[9]==' ':
            dictionary[9]='O'
        elif dictionary[8]==dictionary[9] and dictionary[8]!=" " and  dictionary[7]==' ':
            dictionary[7]='O'
        elif dictionary[7]==dictionary[9] and dictionary[7]!=" " and  dictionary[8]==' ':
            dictionary[8]='O'
        elif dictionary[1]==dictionary[5] and dictionary[1]!=" " and  dictionary[9]==' ':
            dictionary[9]='O'
        elif dictionary[5]==dictionary[9] and dictionary[5]!=" " and  dictionary[1]==' ':
            dictionary[1]='O'
        elif dictionary[1]==dictionary[9] and dictionary[1]!=" " and  dictionary[5]==' ':
            dictionary[5]='O'
        elif dictionary[7]==dictionary[5] and dictionary[7]!=" " and  dictionary[3]==' ':
            dictionary[3]='O'
        elif dictionary[7]==dictionary[3] and dictionary[7]!=" " and  dictionary[5]==' ':
            dictionary[5]='O'
        elif dictionary[3]==dictionary[5] and dictionary[3]!=" " and  dictionary[7]==' ':
            dictionary[7]='O'
        elif dictionary[7]==dictionary[4] and dictionary[7]!=" " and  dictionary[1]==' ':
            dictionary[1]='O'
        elif dictionary[4]==dictionary[1] and dictionary[4]!=" " and  dictionary[7]==' ':
            dictionary[7]='O'
        elif dictionary[1]==dictionary[7] and dictionary[1]!=" " and  dictionary[4]==' ':
            dictionary[4]='O'
        elif dictionary[8]==dictionary[5] and dictionary[8]!=" " and  dictionary[2]==' ':
            dictionary[2]='O'
        elif dictionary[5]==dictionary[2] and dictionary[5]!=" " and  dictionary[8]==' ':
            dictionary[8]='O'
        elif dictionary[8]==dictionary[2] and dictionary[8]!=" " and  dictionary[5]==' ':
            dictionary[5]='O'
        elif dictionary[9]==dictionary[6] and dictionary[9]!=" " and  dictionary[3]==' ':
            dictionary[3]='O'
        elif dictionary[9]==dictionary[3] and dictionary[9]!=" " and  dictionary[6]==' ':
            dictionary[6]='O'
        elif dictionary[6]==dictionary[3] and dictionary[6]!=" " and  dictionary[9]==' ':
            dictionary[9]='O'
        else:
            occupied_o()
    if y==0:
        if dictionary[1]==dictionary[2] and dictionary[1]!=" " and  dictionary[3]==' ':
            dictionary[3]='X'
        elif dictionary[2]==dictionary[3] and dictionary[2]!=" " and  dictionary[1]==' ':
            dictionary[1]='X'
        elif dictionary[1]==dictionary[3] and dictionary[1]!=" " and  dictionary[2]==' ':
            dictionary[2]='X'
        elif dictionary[4]==dictionary[5] and dictionary[4]!=" " and  dictionary[6]==' ':
            dictionary[6]='X'
        elif dictionary[5]==dictionary[6] and dictionary[5]!=" " and  dictionary[4]==' ':
            dictionary[4]='X'
        elif dictionary[4]==dictionary[6] and dictionary[4]!=" " and  dictionary[5]==' ':
            dictionary[5]='X'
        elif dictionary[7]==dictionary[8] and dictionary[7]!=" " and  dictionary[9]==' ':
            dictionary[9]='X'
        elif dictionary[8]==dictionary[9] and dictionary[8]!=" " and  dictionary[7]==' ':
            dictionary[7]='X'
        elif dictionary[7]==dictionary[9] and dictionary[7]!=" " and  dictionary[8]==' ':
            dictionary[8]='X'
        elif dictionary[1]==dictionary[5] and dictionary[1]!=" " and  dictionary[9]==' ':
            dictionary[9]='X'
        elif dictionary[5]==dictionary[9] and dictionary[5]!=" " and  dictionary[1]==' ':
            dictionary[1]='X'
        elif dictionary[1]==dictionary[9] and dictionary[1]!=" " and  dictionary[5]==' ':
            dictionary[5]='X'
        elif dictionary[7]==dictionary[5] and dictionary[7]!=" " and  dictionary[3]==' ':
            dictionary[3]='X'
        elif dictionary[7]==dictionary[3] and dictionary[7]!=" " and  dictionary[5]==' ':
            dictionary[5]='X'
        elif dictionary[3]==dictionary[5] and dictionary[3]!=" " and  dictionary[7]==' ':
            dictionary[7]='X'
        elif dictionary[7]==dictionary[4] and dictionary[7]!=" " and  dictionary[1]==' ':
            dictionary[1]='X'
        elif dictionary[4]==dictionary[1] and dictionary[4]!=" " and  dictionary[7]==' ':
            dictionary[7]='X'
        elif dictionary[1]==dictionary[7] and dictionary[1]!=" " and  dictionary[4]==' ':
            dictionary[4]='X'
        elif dictionary[8]==dictionary[5] and dictionary[8]!=" " and  dictionary[2]==' ':
            dictionary[2]='X'
        elif dictionary[5]==dictionary[2] and dictionary[5]!=" " and  dictionary[8]==' ':
            dictionary[8]='X'
        elif dictionary[8]==dictionary[2] and dictionary[8]!=" " and  dictionary[5]==' ':
            dictionary[5]='X'
        elif dictionary[9]==dictionary[6] and dictionary[9]!=" " and  dictionary[3]==' ':
            dictionary[3]='X'
        elif dictionary[9]==dictionary[3] and dictionary[9]!=" " and  dictionary[6]==' ':
            dictionary[6]='X'
        elif dictionary[6]==dictionary[3] and dictionary[6]!=" " and  dictionary[9]==' ':
            dictionary[9]='X'
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
    if dictionary[a]=='X' or dictionary[a]=='O':
        print("That space is already taken")
        x_space()
    if dictionary[a]==' ':
        dictionary[a]='X'
def y_space():
    global a
    a=int(input(">"))
    if dictionary[a]=='X' or dictionary[a]=='O':
        print("That space is already taken")
        y_space()
    if dictionary[a]==' ':
        dictionary[a]='O'

while playing_choice==1:
    display(dictionary)
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
            display(dictionary)
            victory()
            if t==9:
                break
            computer_turn()
            t+=1
            print("-------")
            display(dictionary)
            victory()

        elif y == 0:
            y_space()
            t+=1
            temp.pop(a-b)
            z+=1
            b+=1
            display(dictionary)
            victory()
            if t==9:
                break
            computer_turn()
            t+=1
            print("------")
            display(dictionary)
            victory()

        else:
            print('ERROR')



    if  t==9 and g==False:
        print("ITS A DRAW!")
    print("GG")
    playing()
