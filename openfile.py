# Mytxt is a text file that i read from here

re = open("Mytxt", "r") # r is to read open a file and read

print(re.read())

wr = open('Mytxt', 'w') # w is to write into a file, it will not save the text
wr.write("I am adding a new text ")

app = open('Mytxt', 'a')
app.write(" Now, this is stored because it append the new text")

print(re.read())
