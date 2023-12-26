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

#/Modification Of Strings ///
x ="hello, world!";
print(x.upper());
print(x.lower());


x ="  hello, world!";
print(x.strip());


x ="  hello, world!";
print(x.strip().replace('h','j'))

y = "Jingal Bells, Jingal Bells, Jingal All The Way";
print(y.split(","));

##StringConcatenation

x = "Shreya";
y = "Ray";
z = x + " " + y
print(z)

##string Format
text = "His name is John Snow and He is King in the north. He doesnt even look old even in his {}s";
age = 30;
print(text.format(age));

q =3;
cost = 1000;
productNo = 34;
text = "Product Number : {} \nHas been ordered In the Quantity of {}, per bottle cost is {} ";
print(text.format(productNo, q, cost));


##Escape character
text1 = "You sure about the release of the \"Game Of Thrones season\" 8 ";
text = "You sure about the release of the \rGame Of Thrones season\r 8 ";
print(text1);
print(text);

texT = "You sure about the release of the \fGame Of Thrones season\f 8 ";
print(texT);

text2 = "You sure about the release of the \bGame Of Thrones season\b 8 ";
print(text2);

text3 = "You sure about the release of the \000Game Of Thrones season\000 8 ";
print(text3);

text4 = "You sure about the release of the \tGame Of Thrones season\t 8 ";
print(text4);


y=9;
x = "hello, world!"
print(x.capitalize());
print(x.casefold());
print(x.count("l"));
#########print(x.center(1));
print(x.encode());
print(x.endswith("hello"));
print(x.expandtabs());
print(x.find("o"));
print(x.find("w"));
z= "hello, world!"
print(z.format(y));
##print(x.format_map());
print(x.index("d"));
print(x.isalnum());
print(x.isalpha());


###DATA TYPES###
##Numeric types -int , float ,complex

x =1;
y = 7.8;
z = 1j;
print(type(x));
print(type(y));
print(type(z));

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

##nummeric Type conversion
x =1;
y = 3.9;
z =5j;

a =float(x);
b = int(y);
c = complex(z);
print(a);
print(b);
print(c);
print(type(a));
print(type(b));
print(type(c));

##Random numbers any one number from 1 to 20 
import random
print(random.randrange(1, 20));

##casting
x =int(1);
y=float(9);
z =float(0);
print(x);
print(y);
print(z);









