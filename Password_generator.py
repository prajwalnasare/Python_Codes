import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['@','#','$','*','!','&','(',')','+']

print("Password Generator")
nr_letters = int(input("How many letters do you want in your password?"))
nr_numbers = int(input("How many numbers do you want in your password?"))
nr_symbols = int(input("How many symbols do you want in your password?"))
# easy way
# password = ""

# for char in range(1,nr_letters + 1):
#     random_char = random.choice(letters)
#     password = password + random_char

# for num in range(1,nr_numbers + 1):
#     random_num = random.choice(numbers)
#     password = password + random_num
# for symb in range(1,nr_symbols + 1):
#     random_symb = random.choice(symbols)
#     password = password + random_symb

# print(password)

# hard way
password = []

for char in range(1,nr_letters + 1):
    random_char = random.choice(letters)
    password.append(random_char)
for num in range(1,nr_numbers + 1):
    random_num = random.choice(numbers)
    password.append(random_num)
for symb in range(1,nr_symbols + 1):
    random_symb = random.choice(symbols)
    password.append(random_symb)

print(password)
random.shuffle(password)
print(password)

new_password = ""
for char in password:
    new_password += char

print(f"Your password is :{new_password}")