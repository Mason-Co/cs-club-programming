import random

def compareSet(num1, num2):
    while num1 != num2:
        print("thinking...")
        num2 = random.randint(num1 - 1, num1 + 1)
        print(".")
        print("..")
        print("...")
    return num2

def main():
    print("FiRST nUMBer: ")
    num1 = input()
    print("SeCand MuNber: ")
    num2 = input()
    comp1 = 0
    comp1 = compareSet(num1, comp1)
    comp2 = 0
    comp2 = compareSet(num2, comp2)
    product = comp1 + comp2
    print(product)

if __name__ == '__main__':
    main()