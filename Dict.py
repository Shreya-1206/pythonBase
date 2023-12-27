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
