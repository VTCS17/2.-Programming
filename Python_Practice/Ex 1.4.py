#Area of a Field
sqft_to_acre = 43560
Length = input("Enter the length of the field (feet): ")
Width = input("Enter the width of the field (feet): ")
Area = (float(Length)* float(Width))/sqft_to_acre
print("The Area of the Field is " + str(Area) + " acres")
