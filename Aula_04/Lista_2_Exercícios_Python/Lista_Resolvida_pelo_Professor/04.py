import os
os.system('cls')

for i in range(1,101):
    if i % 2 == 0:
        print(i)

# ou

for i in range(2,101,2):
    print(i)

# ou

for i in range(1,101):
    if i % 2 != 0:
        continue
    print(i)