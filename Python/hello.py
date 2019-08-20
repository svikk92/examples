print("Hello world!")
mystr = "Hello"
print(mystr[1])
print(mystr[-1])

print("hello \nworld")

print("hello \tworld")

print(type(mystr))

print(len(mystr))

mystr = 100

print(type(mystr))

xyz = "The {} {} {}"

print(xyz.format("brown", "fox", "quick"))

xyz = "The {0} {0} {0}"

print(xyz.format("brown", "fox", "quick"))

xyz = "The {2} {0} {1}"

print(xyz.format("brown", "fox", "quick"))

xyz = "The {q} {b} {f}"

print(xyz.format(b="brown", f="fox", q="quick"))

name = 'vikas'

title = 'sharma'

#print(f "Hello {name} {title}")  new to python 3.6

result = 100/777

print("Result is {r:1.5f}".format(r=result))

print("Result is {}".format(result))

