#Create a program that reads the length and width of a farmer’s field from the user in
#feet. Display the area of the field in acres.
#Hint: There are 43,560 square feet in an acre.



#Area of a Field
sqft_to_acre = 43560
Length = input("Enter the length of the field (feet): ")
Width = input("Enter the width of the field (feet): ")
Area = (float(Length)* float(Width))/sqft_to_acre
print("The Area of the Field is " + str(Area) + " acres")
