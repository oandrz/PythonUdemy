file = open("my_file.txt")
contents = file.read() # will get the content of the file as a string
print(contents)
file.close() # tell the system to close down the file

'''
other format: it always close down file once we finish using them
'''



'''
    to write, if file doesn't exist when read file then it will automatically created
'''

# will replace every content
with open("my_file.txt", mode='w') as file:
    file.write("New Text")

# will add from previous content
with open("my_file.txt", mode='a') as file:
    file.write("\nNew Text_2")