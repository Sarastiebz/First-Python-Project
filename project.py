# Python Demonstration Project
# Sara Stieber

# Reads winning Megabucks numbers from a file and then goes through 
# all possible combinations of numbers to look for number combinations 
# that have won more often.
# 
# Megabucks rules: 6 numbered balls are drawn from a group of balls 
# numbered 1-49. Megabuck ticket costs $1. Minimum of 3 balls matched to your numbers is a 
# winner of $2. The order that the winning balls are drawn does not matter.

# variables
winners = []    # a list of the winning numbers read in from the file
dollaBills = [] # a list containing the current best number combination with the number of wins appended to end of list
maxWins = 0     # the most wins found in the number combination

# function to compare generated balls to the winners list
def compareNumbers(balls):
    global maxWins
    global dollaBills
    wins = 0
    # retrieve each list of winning balls from the winners list
    for winnerBalls in winners:
        matches = 0
        # check if each generated ball is in the list of winnerballs, track the number of matches
        for ball in balls:
            if ball in winnerBalls:
                matches += 1
        # if the number of matches is 3 or greater it is a winner
        if matches >= 3:
            wins += 1
    
    # check if wins is greater than the maximum number of wins
    if wins > maxWins:
        maxWins = wins
        # add the number of wins to the end of the balls list for reporting at end of program
        balls.append(wins)
        dollaBills = list(balls)   


# read winning numbers from file - must be in same directory and named megabucks.csv
print("Reading numbers from file...")
with open("megabucks.csv") as megaFile:
    # use readlines to get a list containing the string of each line, each line is a winning numbers
    lines = megaFile.readlines()
    # loop through each of the lines and split them by a comma because it is a csv file
    for l in lines:
        line = l.split(',')[1:7]
        # line now contains only the numbers but now we convert them from string to integer for comparison later
        for num in range(0,len(line)):
            line[num] = int(line[num])
        winners.append(line)
print("Finished reading numbers from file...")

# iterate through all number combinations starting at 1,2,3,4,5,6
print("Beginning evaluations...")
for ball1 in range(1,45):

    for ball2 in range(ball1 + 1,46):

        for ball3 in range(ball2 + 1,47):

            for ball4 in range(ball3 + 1,48):

                for ball5 in range(ball4 + 1,49):

                    for ball6 in range(ball5 + 1,50):

                        # call the function that compares these numbers to winning numbers
                        compareNumbers([ball1,ball2,ball3,ball4,ball5,ball6])

                        
# print the most winning balls to the screen
print(f"The best balls are: {dollaBills[0]} {dollaBills[1]} {dollaBills[2]} {dollaBills[3]} {dollaBills[4]} {dollaBills[5]}")
print(f"The best balls were winners {dollaBills[6]} times")