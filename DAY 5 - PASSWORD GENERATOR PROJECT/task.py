letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
import random
print("Welcome to the Password Generator!!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
passwd = ""

for i in range(nr_letters):
    num=random.randint(0,len(letters)-1)
    passwd+= letters[num]

for j in range(nr_symbols):
    num = random.randint(0, len(symbols) - 1)
    passwd+=symbols[num]

for k in range(nr_numbers):
    num = random.randint(0, len(numbers) - 1)
    passwd+=numbers[num]

print(f"Suggested password: {passwd}")


# HARD VERSION(without sequence)

char_list=list(passwd)
random.shuffle(char_list)
print("Suggested password(shuffled version):","".join(char_list))













