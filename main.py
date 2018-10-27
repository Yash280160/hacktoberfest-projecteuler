sum = 0
b= 0
for i in range(20000001):
    for j in range(20000001):
      if(i%j==0):
        b = b+ 1
    if(b==0):
      sum = sum + i
print("The sum of numbers:"sum)