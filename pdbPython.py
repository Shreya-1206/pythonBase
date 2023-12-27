import pdb

def fractorial(n):
    ##pdb.set_trace()
    if(n == 0):
        return 1;
    else:
     return n*fractorial(n -1);

result = fractorial(5)
print(result);


for x in range(0,10):
   print(x);