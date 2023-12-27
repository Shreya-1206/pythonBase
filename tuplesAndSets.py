t =("Apple", "Banana", "Cherry");
print(t);
print(type(t));
print(len(t));

##Allow Dups
t =("Apple", "Banana", "Cherry", "Apple");
print(t);

# Create tuple with one item
t =("Apple",);
print(type(t));

# Data types
t =("Apple Store","True", "24 Street California", 234);
print(t);

# Acess items
t =("Apple Store","True", "24 Street California", 234);
print(t[2]);

# Range of indexes returns new array
t =("Apple", "Banana", "Cherry", "Guava", "Blackcurrent");
print(t[1:3]);
print(t[1:4]);
print(t[:4]);

##change tuple values
t =("Apple", "Banana", "Cherry", "Guava", "Blackcurrent");
l = list(t);
l[0]="Avocado";
t = tuple(l);
print(t);

## Append items
t = ("Apple", "Banana", "Cherry", "Guava", "Blackcurrent");
l =list(t);
l.append("Oranges");
t =tuple(l);
print(t);

# Add two tuples
t = ("Apple", "Banana", "Cherry", "Guava", "Blackcurrent");
t2 = ("Blueberries" , "Dragon Fruit");
t += t2;
print(t);

# remove items
t =("Apple", "Banana", "Cherry", "Guava", "Blackcurrent");
l = list(t);
l.remove("Banana");
l.remove("Apple");
t =tuple(l);
print(t);

t =("Apple", "Banana", "Cherry", "Guava", "Blackcurrent");
del t; ## printing the t now will give error

### Unpacking the tuples

t =("Apple", "Banana", "Dragon Fruit");
(red, yellow, pink) = t;
print(red); ## python extracts values throught creating variables
print(yellow);
print(pink);
    ### if the number of varibles less then the values 
t =(" Green Apple", "Banana", "Dragon Fruit", " Strawberries", "Cherry" );
(green, yellow, *pink)= t;
print(green);
print(yellow);
print(pink);

## loop through this tuple(for loop)
for x in t:
    print(x);


## join tuples
t =(" Green Apple", "Banana", "Dragon Fruit", " Strawberries", "Cherry" );
t2 = (200, 400);
t3 = t2 + t;
print(t3);

## multiple the content in tuple
t =(" Green Apple", "Banana", "Dragon Fruit", " Strawberries", "Cherry" );
t = t*2;
print(t)

####### Sets
##Dups

s ={"Apple", "Banana", "Dragon Fruit", "Apple"};
print(s); ##No dups
print(len(s));

# Accessing items in setd is not possible so use for loop

for x in s:
    print(x);

## Adding new items
s ={"Apple", "Banana", "Dragon Fruit"};
s.add("Orange");
print(s);

#Add sets

s ={"Apple", "Banana", "Dragon Fruit"};
set = {"Guava", "Pineapple"};
s.update(set);
print(s);

## remove items
s ={"Apple", "Banana", "Dragon Fruit"};
s.remove("Apple");
print(s);

##Join sets
s ={"Apple", "Banana", "Dragon Fruit"};
set = {"Guava", "Pineapple"};
s.union(set);
print(s);





