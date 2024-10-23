import random

def update(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    c = random.choice(letters)
    pos = random.randint(0, len(word) -1)
    newstring = word[0:pos] + c + word[pos + 1:]
    return newstring

def main():
    happy = "rando"
    birthday = "randommm"
    trenton = "randomm"
    finallineexclamation = "!"
    while happy != "Happy":
        happy = update(happy)
        happy = happy.title()
    print("Phase 1 complete...")
    while birthday != "birthday":
        birthday = update(birthday)
    print("Phase 2 complete...")
    while trenton != "Trenton":
        trenton = update(trenton)
        trenton = trenton.title()
    print("Phase 3 complete...")
    print(f"{happy} {birthday} {trenton}{finallineexclamation}")

if __name__ == '__main__':
    main()