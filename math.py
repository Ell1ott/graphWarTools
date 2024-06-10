currentDir = 1  

def newDir(loc, dir):
    global currentDir
    l = f'(x-{loc}+abs(x-{loc}))({dir-currentDir})'
    '(x-1+abs(x-1))'
    currentDir = dir
    return l
    
pixelToUnit = 25/387

prevX = 0
PrevY = 0

def findSteepness(prevX, prevY, x, y):
    return (y-prevY)/(x-prevX)


def onClick(x, y):
    global prevX, prevY
    steepness = findSteepness(prevX, prevY, x, y)
    prevX = x
    prevY = y
    formel += "+" + newDir(x*pixelToUnit, steepness)
    
# formel = f'(x+abs(x))({currentDir})'

# formel += "+" + newDir(1, 0)

# for i in range(10):
#     formel += '+' + newDir(i + 5, 1)
#     formel += '+' + newDir(i + 0.5 + 5, -1)


print(formel)
    
    

