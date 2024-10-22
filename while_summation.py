#while summation code following directions from Readme
user_num = int(input(""))
x = 0
times_looped = 0
total = 0

while x <= user_num and times_looped < user_num:
    total += x
    x += 1
    
print(total)
