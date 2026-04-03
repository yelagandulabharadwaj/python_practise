'''
The "Ship of Theseus" is a classic philosophical thought experiment about identity over time.

It asks: if every part of a ship is gradually replaced, one piece at a time, is it still the same ship in the end?

This kata turns that idea into a simple validation problem.

A ship is represented by a matrix of states.

Each row shows the ship at a different moment in time.

The ship is considered to remain the same only if, between every two consecutive rows, exactly one part of the ship has changed.

Rules
All rows must have the same length.
Rows must be compared position by position.
Between one row and the next, exactly one element (ship part) must be different.
If any transition changes zero elements or more than one element, the process is invalid.
Return true if the whole process is valid, otherwise return false.

If the matrix has 0 or 1 row, return true.

Example
shipOfTheseus([
  ["a", "b", "c"],
  ["x", "b", "c"],
  ["x", "y", "c"],
  ["x", "y", "z"]
]);
Step-by-step
["a", "b", "c"] -> ["x", "b", "c"] -> 1 change
["x", "b", "c"] -> ["x", "y", "c"] -> 1 change
["x", "y", "c"] -> ["x", "y", "z"] -> 1 change
Result:

true


'''

def diff(x,y):
    c=0
    
    for i in range(0,len(x)):
        print(x[i],y[i])
        if x[i]!=y[i]:
            c+=1
    print(c)
    return c

def ship_of_theseus(ship):
    if ship==[]:
        return True
    elif len(ship)==1:
        return True
    else:
        for i in range(0,len(ship)-1):
            print(ship[i],ship[i+1])
            if len(ship[i])!=len(ship[i+1]):
                return False
            c1=diff(ship[i],ship[i+1])
            if c1>1 or c1<=0:
                return False
        return True

print(ship_of_theseus([["a", "b", "c"], ["x", "b", "c"], ["x", "y", "c"], ["x", "y", "z"]]))

print(ship_of_theseus([["a", "b", "c"], ["x", "y", "c"]]))