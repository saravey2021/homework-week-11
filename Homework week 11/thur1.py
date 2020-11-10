def sumFromTo(startValue,endValue):
    sum = 0
    for i in range(startValue , endValue+1):
       if endValue > startValue:
         sum = sum + i
       else:
         sum = sum + 0
    return sum
startValue=int(input("Start Value:"))
endValue=int(input("End Value:"))
print("The sum of number between"+str(startValue)+"and"+str(endValue)+"is:"+str(sumFromTo(startValue,endValue)))