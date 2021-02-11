import numpy as np
from numpy import random

board = np.empty((3,4))
board = [["1A","1B","1C","1D"],
          ["2A","2B","2C","2D"],
          ["3A","3B","3C","3D"]]
          
matrix = np.empty((3,4))
matrix = [[" "," "," "," "],
          [" "," "," "," "],
          [" "," "," "," "]]
          
roulette =  ['1A','2B','3C','1D','2A','3B','1C','2D','3A','1B','2C','3D']
positions = ['00','11','22','03','10','21','02','13','20','01','12','23']
occupied =  ['-','-','-','-','-','-','-','-','-','-','-','-']

score=100

def main():
    printGame()   
    spin()
    while True:
        print("Keep playing? [Y/N]:", end=' ')
        kp = input().lower()
        print('')
        
        if(kp == 'y'): spin()
        else:
            if(kp == 'n'): break
            else:
                print('Not a valid input. Try Again.') 
                continue
    print('Thank you for playing! \nYour final score is:', score)


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

def spin():
    
    #recibir la casilla ocupada en formato de posición en lista
    rand=random.randint(11)

    #print('Random position:  ', rand)
    print('* * * * * * * *')
    print('*  SLOT:', roulette[rand], '  *')
    print('* * * * * * * *')


    #pasar el valor de posición en lista a posición en matriz
    board_position= [int(char) for char in positions[rand]]
    i=board_position[0]
    j=board_position[1]
    
    #print('Position in board:', board_position)
    print('')
    
    #tachar el valor en la matriz y en la ruleta
    matrix[i][j]='*'
    occupied[rand]='*'
    
    printGame()
    
main()