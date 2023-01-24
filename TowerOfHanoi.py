# Tower of Hanoi Python Implementation

def move(f, t):
    '''
    f : From Position
    t : To Position
    '''
    print("Move disc from {0} to {1}!".format(f, t))


def moveVia(f, v, t):
    '''
    f : From Position
    v : Via Position
    t : To Position
    '''
    move(f, v)
    move(v, t)

print("\t\tTower Of Hanoi\t\t")

def Hanoi(n, f, h, t):
    ''' 
    n : Number of disks
    f : From Position
    h : Helper Position
    t : Target Position
    '''
    if n == 0:
        pass
    else:
        Hanoi(n-1, f, t, h)
        move(f, t)
        Hanoi(n-1, h, f ,t)
    
    
Hanoi(9,"1","2","3")
