height=float(input( "enter the height in m" ))
weight=float(input("enter the weight in kg "))
bmi=weight/(height)**2
if (bmi<18.5):
 print("underweight")
elif(18.5-24.9):
   print("normal")
elif(25.0<bmi<29.9):
   print(" overweight")
elif(bmi>=30.0):
   print ("obese")
