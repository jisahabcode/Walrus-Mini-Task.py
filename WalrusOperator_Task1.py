
#Walrus Operator Advance Topic 
while (number:=int(input("Enter A Number OR '0' For Exit: "))) !=0:
       numbers=[number]
       results=[y for x in numbers if (y:=x*x)>0]
       print(f"Your Number is: {number}\nResult is: {results}")