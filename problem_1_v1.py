from random import shuffle
from time import sleep


class Animal:
    def __init__(self, name):
        self.Name = name

    def __repr__(self):
        print(self.Name)


# Для добавления звуков просто пополняем этот словарь (который директор впринципе и так даёт)
sounds = {
    "lion": "roar",
    "cat": "meow",
    "dog": "bark",
    "wolf": "barkbark",
    "giraffe": "giraffesounds"
}


animals = []
for i in sounds:
    animals.append(Animal(i))


print("Lets now learn what sounds animals make!")
sleep(1)
print("--------------------")
sleep(1)

for i in animals:
    print(i.Name + " makes sound " + sounds[i.Name])
    sleep(0.5)

print("--------------------")
print("Now you will take a test. You will have 3 attempts, if you make more than 3 mistakes, you fail")
print("--------------------")

attempts = 3
animal_names = list(sounds.keys())
shuffle(animal_names)

for i in animal_names:
    while attempts > 0:
        ans = input(f"What sound does {i} make?  ").lower()
        if ans == sounds[i]:
            print("That's right!")
            break
        else:
            attempts -= 1
            print(f"No, {i} doesn't make sound {ans}, you have {attempts} left. Try again!")

if attempts <= 0:
    print("--------------------")
    print("You have ran out of attempts! Try again later!")
else:
    print("--------------------")
    print("Congratulations! You passed the test.")
