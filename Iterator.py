t = ("apple", "banana", "cherry")
myit = iter(t)
print(next(myit))
print(next(myit))
print(next(myit))

s ="Banana";
myit = iter(s);
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

## For iterable for loop can be used 


####################### Python scope ##############################

## Local Scope 
def function():
    x = 90;
    print(x + 10);
function();

## Inner Function
def function():
    x =300;
    def innerFuntion():
       print(x);
    innerFuntion()

function();       


## global Variable 
x =90;
def fun():
    print (x);

fun();
print(x);

## naming Variables
x =999;

def local():
    x =20;
    print(x);
 
local()
print(x);

## gobal Keyword
def gobal():
    global x 
    x =9000;
    print(x);

gobal();
print(x);

   #### use gobal keyword to make a change in inside  afucntion

x = 756;
def func():
    global r
    r =90;
   

func()
print(x);

########## Modules ######################
import myModules as mx

mx.greeting("Jon Mockery");

p1 = mx.person["name"];
print(p1);
