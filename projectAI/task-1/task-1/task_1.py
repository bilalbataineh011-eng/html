#part1:Output
print("2*3=",2*3)
print("2**3=",2**3)
print("1 == 2=",1 == 2)
print("3 == 1 * 3=",3 == 1 * 3)
print("(3 == 1) * 3=", (3 == 1) * 3)
print("(3 == 3) * 4 + 3 == 1=", (3 == 3) * 4 + 3 == 1)
print("5.0 / 3=", 5.0 / 3)
print("5 % 3=", 5 % 3)
print("5 / 3=", 5 / 3)
print("float (123)=", float (123))
#print("int ('123.23')=", int ('123.23')) #error
print("bool (0)=", bool (0))
print("not (False or True)=", not (False or True))
print("float (7) // 4=", float (7) // 4)
print("3 < 5 and 5 < 10=", 3 < 5 and 5 < 10)
print("'py' + 'thon'=", 'py' + 'thon')
print("'py'*3 + 'thon'=", 'py'*3 + 'thon')
print("0 == False=", 0 == False)
print("False or ( -5 % 2 == 1)=", False or ( -5 % 2 == 1))
print("type (not 1)=", type (not 1))
print("float(int (5.3))=", float(int (5.3)))
print("type ([])=", type ([]))
print("bool (-5)=", bool (-5))
print("2 ** 2 ** 0=", 2 ** 2 ** 0)
print("(2 ** 2) ** 0=", (2 ** 2) ** 0)
#part2.1 :Loop statements
x=int(input("Enter start number:"))
y=int(input("Enter end number:"))
counter=0
for i in range(x,y+1):
    if i%2==0:
        counter+=1
print("Number of even numbers between", x, "and", y, "is:", counter)
#part2.2 :Loop statements
n=int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    m=(2**i)-1
    sum+=m
print("Sum of the series is:", sum)
#part3.1 :string
words = "Sami,7ameed, hani , reda , 3ala, a#i, Wael, saleem, Yara, @ara"
word_list = words.split(",")
for word in word_list:
    word = word.strip()
    if word[0].isalpha():
        print(word[0].upper()+word[1:])

#part3.2 :string
str = "Sami went with his friend to city. They ride a bus from city. sami is carrying a bag."

new_list=str.split(".")
print("the count of the sentences is:", len(new_list)-1)
new_list=str.split(" ")
print("the count of the words is:", len(new_list))
new_list=str.split(".")
for sentence in new_list:
    sentence = sentence.strip()
    if sentence=="":
        continue
    print(sentence.title())
    
