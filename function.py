def myFun():
    print("Hello welcome to first function from python !!");

myFun();

def myFun(name):
  print(name+" " + "Ray");
myFun("Shreya");
myFun("Soni");


### no of arguments
def add(a,b):
   z =a +b;
   print("Addition -", z);

def  sub(a,b):
   z =a -b;
   print("Substraction -", z);

def  multi(a,b):
   z =a *b;
   print("Multiplication -", z);

def  div(a,b):
   z =a /b;
   print("Division -", z);

def  mod(a,b):
   z =a %b;
   print("Modulus-", z);
   
sub(100,50);
div(500,5);
multi(8,8);
mod(11,2)
add(20,59);

## mulitple arguments can be recived by the function when its called

def fun(*add):
   i = 0;
   
   for x in add:
      i += x;
      print("Addition with muiltiple Arguments-", i);     

fun(89, 54, 10, 100);

def printName(*name):
   print("Names - " +name[2]);

printName("Jon", "Maddy", "Sofia");

## keyWord arguments
def child(child1, child2, child3): 
   print("Print the name of youngest child - "+child3)
   print("Print the name of middle child - " + child2)
   print("Print the name of eldest child - " + child1)

child(child1="Soni", child2="Piyush", child3= "Shreya"); 

## Arbitary Keyword arguments
def fruits(**name):
   print("My favourite Fruit is -" + name["fruit1"])
   print("My favourite fruit Juice is -" + name["fruit2"]+" "+ "Juice")

fruits(fruit1 ="Kiwi", fruit2 ="Watermelon", fruit3 = "Banana");

## default parameter

def travel(country = "Indonesia"):
   print("My wish for travelling to this country is first - " + country);

travel();
travel("Europe");



## passing Array to function 
def arr(food):
   for x in food:
      print(x);

food= ["Gol Gappa", "Dahi Vada"];
arr(food);

## return statement
def funSum(n):
   return 100 * n;

print(funSum(8))


### Recursion
def recurr(k):
   if(k >0):
    result =k + recurr(k -1);
    return result
   else:
      result =0;
      return result;

print(recurr(6))
      
## Anonymous function 

x = lambda a : a + 15
print(x(5));

## lambda can take any number of arguments
x = lambda a , b : a * b;
print(x(9,4));

x = lambda a, b, c : a + b + c;
print(x(400,20,10));

## lambda inside function
def mFun(n):
   return lambda a : a * n;

myDoubler = mFun(2);

print(myDoubler(10));

######## Arrays
dogsBreed = ["French Mastiff", "Bull Mastiff", "Labordor", "stizu" ,"Dobarman", "Boxer", "Husky", "German Shepherd", "Indie", "Golden Retriver"];
x = dogsBreed[7];
print(x);
dogsBreed[0] = "chivwaa";
print(dogsBreed);

print(len(dogsBreed));
for x in dogsBreed:
   print(x);