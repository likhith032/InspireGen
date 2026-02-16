import random

happy_quotes = [
    "Keep smiling, your energy is powerful!",
    "Success loves happy minds.",
    "Happiness attracts opportunities."
]

sad_quotes = [
    "Tough times don’t last, tough people do.",
    "Every dark night has a bright morning.",
    "You are stronger than you think."
]

lazy_quotes = [
    "Start now. Not tomorrow.",
    "Small steps daily = Big results.",
    "Discipline creates freedom."
]
stressed_quotes = [
    "Take a deep breath. You’ve got this.",
    "One step at a time.",
    "Progress, not perfection."
]

mood = input("Enter your mood (happy/sad/lazy/stressed): ").lower()

if mood == "happy":
    print(random.choice(happy_quotes))
elif mood == "sad":
    print(random.choice(sad_quotes))
elif mood == "lazy":
    print(random.choice(lazy_quotes))
elif mood == "stressed":
    print(random.choice(stressed_quotes))
else:
    print("Invalid mood. Stay positive!")
