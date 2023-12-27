####Lists####
import pdb


l =["Apple", "Banana", "Cherry"];
print(l);

## Allow dup
l =["Apple", "Banana", "Cherry", "Apple"];
print(l);
print(l[3]);
# length function
print(len(l));

# Can be any Data Type
l = ["Apple Store","True", "24 Street California", 234];
print(l);
print(type(l));
## create new list
lnew = list(("Apple","Cherry"));
print(lnew);

#Access items from list
l =["Apple", "Banana", "Cherry", "Apple"];
print(l[2])

#negative Indexing
l =["Apple", "Banana", "Cherry", "Apple"];
print(l[-1]);
print(l[-3]);

## Ranging indexes gives new array
l = ["Apple", "Banana", "Cherry", "Apple", "Grapes", "Guava", "Mango", "Orange", "Chikoo"];
print(l[3:]);
print(l[3:8])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon",
"mango"]
print(thislist[:4])

## Check Items using (IN) keyword
l = ["Apple", "Banana", "Cherry", "Apple", "Grapes", "Guava", "Mango", "Orange", "Chikoo"];
if("Orange" in l):
    print("We, have found the item !");

## Change Liste Items 
l = ["Apple", "Banana", "Cherry", "Apple", "Grapes", "Guava", "Mango", "Orange", "Chikoo"];
l[3] = "Blueberry";
print(l);

# Change the range of items
l = ["Apple", "Banana", "Cherry", "Apple", "Grapes", "Guava", "Mango", "Orange", "Chikoo"];
l[1:4] = ["Blueberry","Dragon Fruit", "Blackcurrent"];
print(l);

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

l = ["apple", "banana", "cherry", "guava"]
l[1:3] = ["watermelon"]
print(l);

l = ["apple", "banana", "cherry", "guava"]
l[1:4] = ["watermelon"]
print(l);

# inset at particular index
l = ["apple", "banana", "cherry", "guava"];
l.insert(2, "blueberry");
print(l);

#Append(item)
l = ["apple", "banana", "cherry", "guava"];
l.append("chikoo");
print(l);

## Extend list with another list
l = ["apple", "banana", "cherry", "guava"];
seasionalFruits = ["Mango", "Watermelon", "Lychee", "Grapefruit"];
l.extend(seasionalFruits);
print(l);

## Extend list with (sets, tuple , dict)
l = ["apple", "banana", "cherry", "guava"];
seasionalFruits = {"Mango", "Watermelon", "Lychee", "Grapefruit"};
l.extend(seasionalFruits);
print(l);


## Remove list items
l = ["apple", "banana", "cherry", "guava"];
l.remove("guava");
print(l);

# Remove item from specific index
l = ["apple", "banana", "cherry", "guava"];
l.pop(1);
print(l);

# dont specify the in index number
seasionalFruits = ["Mango", "Watermelon", "Lychee", "Grapefruit"];
seasionalFruits.pop();
print(seasionalFruits)

# del keyword removes from secific index
seasionalFruits = ["Mango", "Watermelon", "Lychee", "Grapefruit"];
del seasionalFruits[0];
print(seasionalFruits)

## Clear () empties the list
seasionalFruits = ["Mango", "Watermelon", "Lychee", "Grapefruit"];
seasionalFruits.clear()
print(seasionalFruits);
seasionalFruits.append("Guava");
seasionalFruits.append("Avocado");
print(seasionalFruits);

## SORT list 
l = ["Mango", "Watermelon", "Lychee", "Grapefruit", "Apple", "Banana", "Cherry"];
seasionalFruits = ["Guava", "Avocado"];
l.extend(seasionalFruits);
l.sort();
print(l);

lNum = [100,89,75,12, 900];
lNum.sort();
pdb.set_trace();
print(lNum);


## sort decending 
l = ["Mango", "Watermelon", "Lychee", "Grapefruit", "Apple", "Banana", "Cherry"];
seasionalFruits = ["Guava", "Avocado"];
l.extend(seasionalFruits);

l.sort(reverse= True);
print(l);

lNum = [100,89,75,12, 900];
lNum.sort(reverse= True);
print(lNum);

## Reverse without alphabet sorrtig
l = ["Mango", "Watermelon", "Lychee", "Grapefruit", "Apple", "Banana", "Cherry"];
l.reverse();
print(l);


## copy list
l = ["Mango", "Watermelon", "Lychee", "Grapefruit", "Apple", "Banana", "Cherry"];
myFav = l.copy();
print(myFav);

  #or
l = ["Mango", "Watermelon", "Lychee", "Grapefruit", "Apple", "Banana", "Cherry"];
myFav = list(l);
print(myFav);

## Join list
l = ["Mango", "Watermelon", "Lychee", "Grapefruit", "Apple", "Banana", "Cherry"];
seasionalFruits = ["Guava", "Avocado"];
lFav = l +seasionalFruits
print(lFav);

for x in l:
    seasionalFruits.append(x);
print(seasionalFruits);



