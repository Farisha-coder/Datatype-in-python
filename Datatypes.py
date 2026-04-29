# length of string
x=" I love Coding"
print(len(x))

#slicing 
print(x[0:14:2])

#indexing 
y="apple "
print(y[0])
print(y[3])


#concatenation
print(x)
#reverse a string 
#input a word 
text = str(input("Enter a string :"))
#Reverse String
#using step values as -1 to iterate in reverse
revText = text[:: -1]
text = revText
print("Reverse of Given String is:")
print(text)
