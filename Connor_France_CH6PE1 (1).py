#Declare list/variables
days=["Sunday","Monday","Tuesday", "Wednesday","Thursday","Friday","Saturday"]
sales=[]
totalSales=0
#write program to require input of sales per given dday
for x in range(7):
    print("Enter the sales for", days[x], ": ")
    sales= float(input())
    while sales < 0:
        print ("You must enter a number greater than or equal to 0:")
        sales= float(input())
#convert into totalSales
    totalSales += sales
#show total sales for the week
print("Total sales for the week: $%.2f" % totalSales) 
