hrwage=int(input("Enter the hourly wage of an employee :"))
trhrs=int(input("Enter the total regular hours of an employee :"))
tohrs=int(input("Enter the total overtime hours of an employee :"))
#Calculate the overtime pay of the employee
opay=tohrs*1.5*hrwage
print("The overtime pay of an employee is",opay)
#Calculate total weekly pay of the employee
weekpay=hrwage*(trhrs+opay)
print("The regular weekly pay of an employee is",weekpay)
