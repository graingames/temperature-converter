def toFarenheit():
    c = float(input("Enter the temprature in Celsius: "))
    f = c*(9/5)+32
    input(f)

def toCelsius():
    f = float(input("Enter the temprature in Farenheit: "))
    c = (f-32)*(5/9)
    input(c)

conversion = input("Do you want to convert to Farenheit or Celsius?(F/C) ")

if conversion =="c" or conversion == "C":
    toCelsius()
elif conversion == "f" or conversion == "F":
    toFarenheit()
else:
    input("INVALID RESPONSE")