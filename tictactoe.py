from random import randrange

# Randomness for loop may come into play 
"""for i in range(10):
    print(randrange(10))"""

# Expectation from Cisco Networking Academy website. An example.

# Establishing tic-tac-toe board
print("+---+---+---+")
print("| 1 | 2 | 3 |\n+---+---+---+\n| 4 | 5 | 6 |\n+---+---+---+\n| 7 | 8 | 9 |")
print("+---+---+---+")

print("--------------------------")

# Trying to figure out how to choose a number
for i in range(1, 10):
    print(i, end=" ")

print()

# Choosing number for play field
choose = int(input("Which square will you choose: "))
print(f"How to put {choose} in grid?")

def square(num):
    for i in range(1, 10):
        print(i, end=",")

print()

print("+---+---+---+\n\
| 1 | 2 | 3 |\n\
+---+---+---+\n\
| 4 | 5 | 6 |\n\
+---+---+---+\n\
| 7 | 8 | 9 |\n\
+---+---+---+")

print("--------------------------")

# Establish basic concept of number before change
print("+---+\n| 1 |\n+---+")
print()
"""def choice(choose):
    print("+---+\n| 1 |\n+---+")"""

print("Choose your location: ")

# If worked out, can create a 'matrix' or '2-D board' of elements
# board = [[EMPTY for i in range(8)] for j in range(8)]

# Can even create '3-D cube' of elements
temps = [[0.0 for h in range(24)] for d in range(31)]
# print(temps)
# All zeroes here
rooms = [[[False for r in range(4)] for f in range(4)] for t in range(3)]
# print(rooms)
rooms[1][1][2] = True
# print(rooms)

board1 = [[i + 1 for i in range(3)] for j in range(3)]
print(board1)
board2 = [[i + 1 for i in range(9)] for j in range(1)]
print(board2)
board3 = [[i + 1 for i in range(1)] for j in range(9)]
print(board3)

empty = []
# board4 = [[empty[i][j] += 1 for i in range(3)] for j in range(3)]
# Error

# Failure: IndexError
"""for i in range(3):
    empty[i] += 1
    for j in range(3):
        empty[j] += 1

"""

for i in range(7):
    if i % 2 == 0:
        print("+---+---+---+")
    else:
        print("| 1 | 2 | 3 |")

print()

for i in range(7):
    if i % 2 != 0:
        print("| 1 | 2 | 3 |")
    else:
        print("+---+---+---+")

print()

print("Choose your next spot: ")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
choice1 = int(input())
def choose(selection):
    for i in list1:
        if choice1 == i:
            return "O"

print(choose(choice1))

print("-----------------------------------------------")

print("Final attempt.")

samp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Creating the list", samp_list)
samp_list[0] = "X"
print("Replacing an element in the list", samp_list)
print()

samp_list[0] = input("Choose a letter: ")
print(samp_list)
print()

print("+---+---+---+")
print(f"| {samp_list[0]} | {samp_list[1]} | {samp_list[2]} |\n+---+---+---+")
print(f"| {samp_list[3]} | {samp_list[4]} | {samp_list[5]} |\n+---+---+---+")
print(f"| {samp_list[6]} | {samp_list[7]} | {samp_list[8]} |\n+---+---+---+")

for i in range(7):
    if i % 2 != 0:
        print("| 1 | 2 | 3 |")
    else:
        print("+---+---+---+")
