# # # # count = 6
# # # # while (count > 0):
# # # #     print(count)
# # # #     count = count -  1
# # # # print ("hello ")


# # # a = input()
# # # a = int
# # # b = 10
# # # print("a is", a, "and b is ", b )
# # # print("The remainder is" , b-a)
# # # print (type(a))


# # tuple = input("Write your fruits shopping list : ")
# # print (tulli )

# # a=input('your age: ')
# # b = int(a)
# # if b >= 18 :
# #     print("yes")
# # else : print("no")

# # n1 = int(input("First Num 1 - "))
# # n2 = int(input("First Num 2 - "))
# # n3 = int(input("First Num 3 - "))
# # n4 = int(input("First Num 4 - "))
 
# # if (n1>n2 and n1>n3 and n1>n4):
# #    print("Greatest Number is Num 1")
# # elif (n2>n1 and n2>n3 and n2>n4):
# #    print("Greatest Number is Num 2")
# # elif (n3>n1 and n3>n2 and n3>n4):
# #    print("Greatest Number is Num 3")
# # elif (n4>n2 and n4>n3 and n4>n1):
# #    print("Greatest Number is Num 4")
# # else: print("All Num are equal")


# # s1 = int(input("what is your marks in PHYSICS - "))
# # s2 = int(input("what is your marks in CHEMISTRY - "))
# # s3 = int(input("what is your marks in MATHS - "))

# # total_percentage =(s1+s2+s3)/300
# # if total_percentage >= 0.4 and s1 >= 33 and s2>= 33 and s3 >= 33:
# #     print("You are Passed", total_percentage*100) 
# # else: print("Sorry Best of Luck Next Time", total_percentage*100)


# # p1 = "Make a lot of money"
# # p2 = "buy now"  
# # p3 = "subscribe this"  
# # p4 = "click this"

# # message = input("Enter your comment: ")

# # if((p1 in message) or (p2 in message )or (p3 in message) or (p4 in message)):
# #     print("This comment is a spam")

# # else:
# #     print("This comment is not a spam")

# # username = input("What is your username? - ")
# # if len(username) > 10:
# #     print("Your username length is more than 10 characters")
# # else: print("Your username is good to go 😁")


# # l1 = ["Harry", "Chupa", "Rustom"]
# # name = input("What is your name: ")
# # if name in l1 :
# #     print((name), "Welcome Back 👋😎")
# # else: print("Sorry Best of Luck Next Time 😁")

# # i = int(input("write your number: "))
# # while i<15:
# #    print(i)
# #    i += 1 

# # for i in range (201):
# #     if i%2 != 0 :
# #         continue
# #     print (i)

# # n1 = int(input("For which Number You want to see the table? "))
# # for i in range (1,11):
# #       print (n1, " x ", i , " = ", (i*n1)) 

# # n1 = int(input("number = "))
# # for i in range(2, n1):
# #    if (n1 % i) == 0:
# #     print("your number is not prime")
# #     break;
# # else: print("prime it is")


                         
# # n = int(input("write your number : "))
# # i = 1
# # sum = 0
# # while (i < n+1):
# #     sum += i
# #     i+= 1
# # print (sum)


# # # l = ["Harry", "chota", "Bada", 124, 6.28]
# # for i in range (0,9,2):
# #     print(i)


# # letter = ''' 
# #          Dear <|Name|>
# #          Yaou are Selected!
# #          <|Date|>'''
# # print(letter.replace("<|Name|>", "Harry").replace("<|Date|>","05 Sept 2015"))

# # a = {1,2,3,4,5,6,}

# # print(a)

# # name = "abhishek"
# # for i in name:
# #     print(i, end = ", ")


# # Day 17

# # for i in range(1,11):
# #     print(i*i)

# # for i in range (1,51):
# #      if i%2 == 0:
# #         print(i)


# # string = "Programming is fun"
# # vowels = ["a","e","i","o","u"]
# # count = 0
# # for char in string:
# #     if char in vowels:
# #         count = count + 1
# # print(count)
    
# # for i in range (1,6):
# #     print("*" * i)

# # def sum(a,b):
# #     if a>b:
# #         print( a,"is greater than",b)
# #     else:print(b,"is greater than",a)
# #     print ("your sum is",a+b)


# # c = 2
# # d = 6
# # sum(c,d)

# # x1 = 22
# # x2 = 89
# # sum(x1,x2)

# # l1 = [1,2,3,4,5]
# # print(l1[5])
# # print(l1[1])

# # CrorePati Game
# # import random
# # l1 = ["What is my name?" , "What is my age? ", "What is my gender? ","Where do i live? "]
# # l2 = ["prakhar", "21", "male", "ghaziabad"]
# # prize = 1000

# # def Crorepati():
# #     global prize
# #     print(random.choice(l1))
# #     answer = input("Please type your answer: ")
# #     if answer in l2 :
# #         print(f"congratulations You have won{prize}")
# #         prize = prize + 1000
# #     else: print("Wrong answer, Try again next time") 

# # i = 0
# # while i < len(l1):
# #     Crorepati()
# #     i += 1 


# # def fibonacci(n):
# #         a = 0
# #         b = 1
# #         if n == 1:
# #                 print(0)
# #         else:
# #            print(a)
# #            print(b)
        
# #         for i in range (2,n):
# #                c = a + b
# #                a = b
# #                b = c
# #                print(c)
# # n = int(input("Type the range ofFibonaci Series:"))        
# # fibonacci(n)

# # Fibonacci wiht recursion

# # n = int(input("what is your rannge:"))

# # def fibonacci(n):
# #         if n == 0:
# #             return 0
# #         elif n == 1:
# #             return 1
# #         else : return(fibonacci(n-1) + fibonacci(n-2))
# # for i in range (n):
# #     print(fibonacci(i))

# # Set

# # a = {0,1,2,3,4}
# # b = {1,2,}
# # print(b.issubset(a)) 

# # Dictionary
# dict = {"harry":31 , "Prakhar":21}
# print(dict["harry"])
# print(dict.get("harry"))
# # multiple item access
# for i in dict.keys():
#     print(dict[i])