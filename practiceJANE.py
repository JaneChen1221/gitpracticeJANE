# Partner 1 Name: Jane Chen
# Partner 2 Name: Daisy Chen
############################
# Assignment Name: GitHub Practice - 2/25/20 - 10 points
import random

def getNRandom(n):
    numbers = []
    for i in range(n):
        number = random.randint(1, 10)
        numbers.append(number)
    return numbers
    pass

def multiplyRandom(numbers):
    product = 1
    for number in numbers:
        product = product * number
    return product
    pass

def main():
	print(multiplyRandom(getNRandom(10))

if __name__ == "__main__":
	main()
