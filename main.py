
# Program to verify and find kaprekar constant 6174

print("===============================================")
# Taking four digit num as an input
num=int(input("Enter a valid four digit number :"))

# finding the max and min value using the given input number by following ascending and descending pattern
ascend="".join(sorted(str(num)))
descend="".join(sorted(str(num), reverse=True))

# substracting the max and the min value
sum=int(descend)-int(ascend)

print("Substraction of :",descend,"-",ascend,"=",sum)

# at the most 7 steps are required to achieve kaprekar constant 6174
# performing this using for loop

for i in range (6):
    ascend="".join(sorted(str(sum)))
    descend="".join(sorted(str(sum), reverse=True))
    sum=int(descend)-int(ascend)
    print("Substraction of :",descend,"-",ascend,"=",sum)

print("===============================================")
# conclude statement
print("\nHence kaprekar's constant is ",sum)
print("===============================================")