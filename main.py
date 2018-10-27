b=0
for i in range(1,600851475143):
  if(600851475143 % i == 0):
    for j in range(1,600851475143):
      if(i%j==0):
        b = b + 1
      if(b==0):
        prime_fact = i
print(i)



