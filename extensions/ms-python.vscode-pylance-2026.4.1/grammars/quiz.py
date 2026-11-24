score = 0

# question 1
epilogi1 = input("1. What exercise in calisthenics mostly exercises the back?: ")
if epilogi1 == "pull ups" or epilogi1 == "pull-ups":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

# question 2
epilogi2 = input("2. What is the best exercise for chest?: ")
if epilogi2 == "chest press" or epilogi2 == "push ups":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

# question 3
epilogi3 = int(input("3. How many days a week should you train for peak results?: "))
if epilogi3 >= 5:
    print("Ideal!")
    score = score + 1
else:
    print("Wrong! Muscles will burn!")

# question 4
epilogi4 = int(input("4. And lastly how many months will it take in your opinion to see results?: "))
if epilogi4 >= 4:
    print("Correct!")
    score = score + 1
else:
    print("Wrong! Under four months you wont see any results")

print("The quiz is over! Thanks for participating!")
print(score)