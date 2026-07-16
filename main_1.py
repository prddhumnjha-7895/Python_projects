import random
sub = [
    "Sarukh Khan",
    "Virat Kohli"
    "Monkey"
    "PM Modi ji"
    "A Group of Monkey"
    "Auto Rickshaw Driver from Delhi"
    "A Mumbai Cat"
]
act=[
    "launches",
    "cancels",
    "dance with",
    "eats",
    "declars wars on",
    "celebrates"
    ]
pl_things=[
    "Agra Fort",
    "in Mumbai Local Train",
    "a plot of samosa",
    "inside parliament",
    "during IPL match",
    "india gate"
]
while True:
    subject=random.choice(sub)
    action = random.choice(act)
    pt = random.choice(pl_things)

    headline = (f"BRAKING NEWS: {subject} {action} {pt} ")
    print("\n" + headline)
    user = input("\ndo you want more news: (yes/no)").strip().lower()
    if user =="no":
        break
print("Thanks to use")


