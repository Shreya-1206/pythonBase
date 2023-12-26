x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # 

print(x);
print(y);
print(z);

x =5;
y = str(9);
print(type(x));
print(type(y));

#Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

##Unpack a Collection
fruits =["apple", "banana", "cherry"];
x , y, z = fruits;
print(x)
print(y)
print(z)

#To combine both text and a variable, Python uses the + character

x ="Oranges";
print("12" + " " + x + " "+ "makes a dozen..");

###STRINGS###

#multilineStrings
x = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.""";
    ## """  """  or  '''  '''
print(x);


##get Position of charcter in a word

x ="Hello World!";
print(x[2]);
print(x[1]);
print(x[0]);

##loop through a string (for loop)
for x in "banana":
    print(x)
 
# Strings are just like array so we can get length 
x ="foot";
print(len(x));

y = "shreya";
print(len(y));

# check string using IN keyword
x = "shreya";
print("h" in x);

y = ["apple", "banana"];
print("apple" in y);

text = "Hey welcome to my python practice file";
print("python practice" in text);

text = "Hey welcome to my python practice file";
if("welcome" in text):
    print("Yes, we have found the word !!");

#check string using NOT In keyword
text = "Hey welcome to my python practice file";
if("shreya" not in text):
    print("No, word is not there" );
else :
   print("Yes, we have found the word !!");

x ="hello world!";
print("hello" not in  x);

#slice
x ="hello, world!";
print(x[:5]);#slice to the start
print(x[2:5]);##slice
print(x[2:]);##slice to the end
print(x[-5:-2])##negative indexing

