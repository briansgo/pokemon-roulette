import random

board = [["1A","1B","1C","1D"],
          ["2A","2B","2C","2D"],
          ["3A","3B","3C","3D"]]
          
matrix = [[" "," "," "," "],
          [" "," "," "," "],
          [" "," "," "," "]]
          
roulette =  ['1A','2B','3C','1D','2A','3B','1C','2D','3A','1B','2C','3D']
positions = ['00','11','22','03','10','21','02','13','20','01','12','23']
occupied =  ['-','-','-','-','-','-','-','-','-','-','-','-']

score=100
question = "Spin? [Y/N]:"

def main():
    printGame()
    while True:
        print(question, end=' ')
        play = input().lower()
        print('')
        
        if(play == 'y'):
            betting()
        else:
            if(play == 'n'): 
                break
            else:
                print('Not a valid input. Please try Again. \n')
                continue
    print('Thank you for playing! \n\nYour final score is:', score, end='!')
    input()


def initialPrint():
    
    print ('BOARD:')
    for i in range(0,3):
        for e in board[i]:
            print (' [', e, sep='', end=']')
        print('')
    print('')
    
    print('ORDER:')
    print('    A    B    C    D ')
    print('1 [ 1] [10] [ 7] [ 4]')
    print('2 [ 5] [ 2] [11] [ 8]')
    print('3 [ 9] [ 6] [ 3] [12]')
    print('')
    
    printGame()
   
    print('POSITIONS IN MATRIX:')
    print (*positions, sep=' ')
    print('') #used for debugging

def printGame():
    
    print('ROULETTE:')
    print (*roulette, sep=' ')
    print(' ', end='')
    print (*occupied, sep='  ')
    print('')
    
    print ('BOARD:')
    print('   A   B   C   D')
    c=1
    for i in range(0,3):
        print (c, end=' ')
        c+=1
        for e in matrix[i]:
            print ('[', e, sep='', end='] ')
        print('')
    print('')
    
    print('Your score:', score, '\n')

def betting():
    print('Please write your bet:', end=' ')
    bet = input().lower()
    
    spin()
    
def spin():
    #recibir la casilla ocupada en formato de índice 
    rand=getRandom(0, len(roulette)-1)

    fill(rand)
    
    printGame()

def fill(rand):
    
    free_position = search_free_position(rand)
    pos=getPositions(free_position)
    
    slot=getSlot(free_position)

    print_slot(slot)

     #pasar el valor de posición en lista a posición en matriz
    board_position= [int(char) for char in pos]
    i=board_position[0]
    j=board_position[1]
    
    #print('Position in board:', board_position)
    #print('')
    
    #tachar el valor en la matriz y en la ruleta
    matrix[i][j]='*'
    occupied[free_position]='*'
    
def print_slot(s):
    #print('Random position:  ', rand)
    print("\nSpinning...\n")
    print('* * * * * * * *')
    print('*  SLOT:', s, '  *')
    print('* * * * * * * *')
    
def search_free_position(rand):
    if (is_it_busy(rand)):
        return bounce(rand)
    else:
        return rand
    
def is_it_busy(rand):
    if (occupied[rand] == '*'):
        return True

def bounce(rand):
    if (getRandom(0,1) == 0): #rebota a la izq
        return bounce_left(rand)
    else:
        return bounce_right(rand) #rebota a la derecha
    
def bounce_left(rand):
    print("Oops! Busy slot, bouncing left!")
    if (rand == 0):
        r = len(roulette)-1
    else:
        r = rand-1
        
    if (is_it_busy(r)):
        bounce_left(r)
    else:
        return r
        
def bounce_right(rand):
    print("Oops! Busy slot, bouncing right!")
    if (rand == len(roulette)-1):
        r = 0
    else:
        r = rand+1
        
    if (is_it_busy(r)):
        bounce_right(r)
    else:
        return r

def getRandom(x,y):
    return random.randint(x,y)

def getSlot(rand):
    return roulette[rand]

def getPositions(rand):
    return positions[rand]

main()