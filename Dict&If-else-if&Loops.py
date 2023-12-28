d = {
    "name" : "Jon",
    "Age" : 29,
    "Proffession" : "Software Developer"
};
print(d);
print(d["name"]);

## NO dups
d = {
    "name" : "Jon",
    "Age" : 29,
    "Proffession" : "Software Developer",
    "Age" : 29,
};
print(d);

print(len(d));

## Dict data types
d = {
    "name" : "Jon",
    "Age" : 29,
    "Proffession" : "Software Developer",
    "Hobbies" : ["Driving", "Reading", "Brewing Coffee"]
};
print(d);

## Accessing Items
d = {
    "name" : "Jon",
    "Age" : 29,
    "Proffession" : "Software Developer",
    "Hobbies" : ["Driving", "Reading", "Brewing Coffee"]
};
print(d["Hobbies"][1]);
x = d.get("Proffession");
print(x);

## Returning Keys
d = {
    "name" : "Jon",
    "Age" : 29,
    "Proffession" : "Software Developer",
    "Hobbies" : ["Driving", "Reading", "Brewing Coffee"]
};

print(d.keys());

d["Fav Colour"] = "Black";
print(d.keys());

### Get values of the keys
d = {
    "name" : "Jon",
    "Age" : 29,
    "Proffession" : "Software Developer",
    "Hobbies" : ["Driving", "Reading", "Brewing Coffee"]
};
print(d.values());


## Check id key exist
d = {
    "name" : "Jon",
    "Age" : 29,
    "Proffession" : "Software Developer",
    "Hobbies" : ["Driving", "Reading", "Brewing Coffee"]
};

if "Age" in d:
    print("Yes, the age is present over here in the information...!!! ");

## update the value 
d = {
    "name" : "Jon",
    "Age" : 29,
    "Proffession" : "Software Developer",
    "Hobbies" : ["Driving", "Reading", "Brewing Coffee"]
};

d.update({"Age" :30})
print(d["Age"]);


## Removing Items
d = {
    "name" : "Jon",
    "Age" : 29,
    "Proffession" : "Software Developer",
    "Hobbies" : ["Driving", "Reading", "Brewing Coffee"]
};
d.pop("Age");
print(d);


d = {
    "name" : "Jon",
    "Age" : 29,
    "Proffession" : "Software Developer",
    "Hobbies" : ["Driving", "Reading", "Brewing Coffee"]
};
d.popitem();
print(d)


d = {
    "name" : "Jon",
    "Age" : 29,
    "Proffession" : "Software Developer",
    "Hobbies" : ["Driving", "Reading", "Brewing Coffee"]
};
del d["Proffession"];
print(d)

## delete dict

d = {
    "name" : "Jon",
    "Age" : 29,
    "Proffession" : "Software Developer",
    "Hobbies" : ["Driving", "Reading", "Brewing Coffee"]
};
del d;

## clear dict
d = {
    "name" : "Jon",
    "Age" : 29,
    "Proffession" : "Software Developer",
    "Hobbies" : ["Driving", "Reading", "Brewing Coffee"]
};

d.clear();
d["Name"] = "Soni Ray";
print(d);

############## If esle if statements ##################
a = 33
b = 200
if b > a:
 print("b is greater than a");

##elif
a = 33
b = 33
if b > a:
 print("b is greater than a")
elif a == b:
 print("a and b are equal")

#else
 a = 200
b = 33
if b > a:
 print("b is greater than a")
elif a == b:
 print("a and b are equal")
else:
 print("a is greater than b")

## short hand if
if a > b: print("A is greater than B..");

##short hand else-if
a =300
b =303
print("A") if a>b else print("B");

## And op
a = 200
b = 33
c = 500
if a > b and c > a:
 print("Both conditions are True");


## Or op 
a =90;
b = 50;
c =20;
if a >b or c > a:
 print("Yes, any one statement is true...!!!")

#nested if
a = 90;
b =80;
if a > 80:
  if b > 70:
   print("Both statements are true");
  else:
   print("Not true...");

## pass 
a = 40;
v =90;
if a> v:
 pass  



################### While Loops #######################

i = 1  
while i < 6: ## condition
 print(i);
 i += 1 ## Increment

## while loop with break statement

i = 1;
while i<7:
 print(i)
 if i == 4:
  break;
 i += 1  

 ## Continue statement

i = 1;
while i < 7:
 i += 1;
 if i ==  3:
  continue;
  print(i);

## with Else statement we can run the block of code once when conndition is no longer true

i = 0;
while i < 7:
 print(i);
 i += 1;
else :
 print("Now the loop doesnt follow any loop condition , thats why else statement is printed....");

######################## For Loops ################################

l = ["Apple", "Banana", "Cherry"];
for x in l:
 print(x);

l = "Shanghai";
for x in l:
 print(x);

## Loop through with range()

for x in range(8):
 print(x);

for x in range(2,50,2):
 print(x);
 

## else in for loop statisfies the code has been and its completed.
for x in range(20,40):
 print(x);
else: 
 print("Else statement signifies that the for loop has been executed..") 

## break the loop and see what happens with else block
 for x in  range(50,60):
  if x == 54:
   break;
  print(x);
 else:
  print("executuion completed..!!")

  






