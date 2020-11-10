def sum(number):
   result=0
   for n in range(number):
       num=int(input("value"+str(n+1)+":"))
       result=result+num
   return result
number=int(input("enter numver:"))
print("the result is:",sum(number))




