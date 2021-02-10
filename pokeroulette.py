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

def split(word):
    return [char for char in word]

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
    
    print ('VALUES:')
    print('   A   B   C   D')
    c=1
    for i in range(0,3):
        print (c, end=' ')
        c+=1
        for e in matrix[i]:
            print ('[', e, sep='', end='] ')
        print('')
    print('')
    
    print('ROULETTE:')
    print (*roulette, sep=' ')
    print('')
    print('POSITIONS IN MATRIX:')
    print (*positions, sep=' ')
    print('')


def main():
    
    rand=random.randint(11)

    print('Random position:  ', rand)
    print('Slot:             ', roulette[rand])
    print('Position in board:', split(positions[rand]))
    
    #recibir la casilla ocupada en formato de posición en lista
    
    #pasar el valor de posición en lista a posición en matriz
    
    #tachar el valor en la matriz y en la ruleta

initialPrint()   
main()
