from random import shuffle
from time import sleep

# В этой имплементации в классе хранится и имя и звук животного, так словарь нам нужен только
# при создании инстанций класса, а распечатать звуки можно когда угодно без него


class Animal:
    def __init__(self, name, sound):
        self.Name = name
        self.Sound = sound

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
for i in sounds.items():
    animals.append(Animal(i[0], i[1]))


print("Lets now learn what sounds animals make!")
sleep(1)
print("--------------------")
sleep(1)

for i in animals:
    print(f'{i.Name} makes sound "{i.Sound}"')
    sleep(0.5)

print("--------------------")
print("Now you will take a test. You will have 3 attempts, if you make more than 3 mistakes, you fail")
print("--------------------")

attempts = 3
shuffle(animals)

for i in animals:
    while attempts > 0:
        ans = input(f"What sound does {i.Name} make?  ").lower()
        if ans == i.Sound:
            print("That's right!")
            break
        else:
            attempts -= 1
            print(f'No, {i.Name} does not make sound "{ans}", you have {attempts} attempt(s) left. Try again!')

if attempts <= 0:
    print("--------------------")
    print("You have ran out of attempts! Try again later!")
else:
    print("--------------------")
    print("Congratulations! You passed the test.")
