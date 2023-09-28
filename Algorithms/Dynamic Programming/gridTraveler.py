#You are a traveler on a 2D grid. You begin in the top left corner and your goal is to travel to the bottom-right corner, You may only move down or right
#In how many ways can you travel to the goal on a grid with dimensions m*n ?


def gridTraveler(m,n):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    return gridTraveler(m-1,n) + gridTraveler(m,n-1)

print(gridTraveler(1,1))
print(gridTraveler(2,3))
print(gridTraveler(3,2))
print(gridTraveler(3,3))
print(gridTraveler(18,18))
