with open("Test.txt", mode='w+') as f:
    f.write("I created this file")

my_file = open("Test.txt")

content = my_file.read()

print(content.upper())

print(content)

