<<<<<<< HEAD
print ("Newton's Second Law of Motion")
print ("---------------------------------------")

print ("Select the missing value: ")
print ("1. Mass(m)")
print ("2. Acceleration(a) ")
print ("3. Force (F)")
missing_value_choice = input ("Enter the option number for the mssing value: ")

if missing_value_choice == "1":
    a = float(input ("Ennter the acceleration (a):"))
    F = float(input ("Enter the force (F): "))
    m = F / a
    print (f"Mass (m)= {m} Kg")
    
elif missing_value_choice == "2":
    m = float(input ("Enter the mass (m):"))
    F = float(input ("Enter the force (F):"))
    a = F / m
    print (f"Acceleration (a)= {a} meter per sec square")
elif missing_value_choice == "3":
    m = float(input("Enter the mass (m):"))
    a = float(input("Ennter the acceleration (a): "))
    F = a * m
    print (f"Force (F)= {F} N")
else:
    print("Invalid option selected fir the missing option")
    

    

    
    
    



=======
print("Newton's Second Law of Motion")
print("---------------------------------------------------")

# Deteermine the missing value 
print("Select the missing value:")
print("1. Mass(m)")
print("2. Acceleration(a)")
print("3. Force(F)")
missing_value_choice = input("Enter the option number for the missing valuse: ")

# Prompt the user to enter the other two values
if missing_value_choice == "1":
    a = float(input("Enter acceleration (a): "))
    F = float(input("Enter force (F): "))
    m = F / a
    print(f"Mass (m) = {m}")

elif missing_value_choice == "2":
    m = float(input("Enter mass (m): "))
    F = float(input("Enter force (F): "))
    a = F / m 
    print(f"Acceleration (a) = {a}")

elif missing_value_choice == "3":
    m = float(input("Enter mass (m): "))
    a = float(input("Enter acceleration (a): "))
    F = m * a
    print(f"Force (F) = {F}")  

else:
    print("Invalid option selected for the missing value.") 
>>>>>>> 865f28daace0cc2c0ce8afe0b9b5bab512c25663
