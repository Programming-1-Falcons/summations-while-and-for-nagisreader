#for Summation code here
user_num = int(input("Enter a number: "))
x = 0
times_looped = 0
total = 0

while x <= user_num and times_looped < user_num:
    total += x
    x += 1
    
print(total)
