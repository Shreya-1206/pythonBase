class firstClass:
    x =5;

p1 =firstClass();
print(p1.x);

## ___init__ function
class Person:
  def __init__(self, name,age, hobby):
     self.name = name;
     self.age =age;
     self.hobby =hobby
    
  def greetings(self):
     print("Hello from " + self.name);

p1 = Person("Pihu", 24, "sona");
p2 = Person("Soni" ,41, "chick chick karna");
print(p1.name);
print(p2.age);
p1.greetings();
p1.age = 11;
print(p1.age);
print(p2.hobby);
del p1.age;


##### Inheritance
class Product:
   def __init__(self, pdName, pdNo):
      self.pdName = pdName;
      self.pdNo = pdNo;
    
   def GetDetails (self):
      print("Product Name - " + self.pdName);
      print("Product Id - " + format(self.pdNo) );

class Cost(Product): 
    def __init__(self, pdName, pdNo, category,cost):
       super().__init__(pdName, pdNo)

       self.category = category;
       self.cost = cost;

    def CostUpdate(self):
     print("Product Name - " + self.pdName);
     print("Product Id - " + format(self.pdNo) );
     print("Product Category - " + self.category)
     print("Product Cost - " + format(self.cost));


product2 = Cost("Body Wash", 1002, "Body", 450);    
product1 = Cost("Razor", 1001, "Essentials", 200);
print(product1.pdName);
print(product1.pdNo);
product1.GetDetails();
product2.CostUpdate();
product1.CostUpdate();

## Iterators
    