if(8>90): 
    print("yes")
else:
    print("no")

age= int(input("Enter your age"))
if(age>90):
   print("no")
else:
    print("yes")

if(age>=18):
    print("yes")
elif(age==1):
    print("you are a kid")
else:
    print("no")

print("end of program")

#match case
a=int(input("enter no"))
a=4
match a:
    case 1:
        print("case1")
    case 2:
         print("case2")
    case _:
        print("default")

#for loop
for i in range(5):
   print(i+1)

a=[1,3,4,5,6,7]
for item in a:
    print(item)

#while loop

# j=4
# while(j<10):
#     print(j)
#     j=j+1
# print("program khatam")


# while(True):
#     print("whle loop not terminating")


