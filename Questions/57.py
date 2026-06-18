"""
Write a porgram that prompts the user to specify the length of a list and then request numbers to populate that list.
Display the final list as the output.
"""

list_length = int(input("Enter length = "))  # Get the length of the list from the user
result = []  # Create an empty list

for i in range(0, list_length):
    num = int(input(f"Enter value at position {i} = "))

    result.append(num)  # Add the number to the list

print(result)  # Display the final list


# lets try with while loop


list_length = int(input("Enter length = "))  # Get the length of the list from the user
result = []  # Create an empty list

i = 0  # Initialize the counter


while i < list_length:  # Continue looping until i reaches list_length
    num = int(input(f"Enter value at position {i} = "))  # Get a number from the user

    result.append(num)  # Add the number to the list
    i += 1  # Increase the counter by 1


print(result)  # Display the final list
