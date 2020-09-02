#Write a program that asks the user to enter the width and length of a room. Once
#the values have been read, your program should compute and display the area of the
#room. The length and the width will be entered as floating point numbers. Include
#units in your prompt and output message; either feet or meters, depending on which
#unit you are more comfortable working with.
#Area of the Room

# Enter width and length in meters
width = input("Enter the width of the room (meters):")
length = input ("Enter the length of the room (meters):")

#Compute Area
Area = float(width)*float(length)
print("The Area of the room is " + str(Area) + " meters.")