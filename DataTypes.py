####Lists####
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