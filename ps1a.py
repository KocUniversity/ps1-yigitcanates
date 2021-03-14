n, B = list(map(int, input().strip().split()))
T = 0

# your code here
Should_be_bigger_than_B = 0


for a in range(1, 10000):
  T = a
  for i in range(1, (n+1)):  
    if i%2 == 0:
      Should_be_bigger_than_B += ((2**i)+1)**(n-i)*T
    else:
      Should_be_bigger_than_B += ((3**i)+1)**(n-i)*T

  if Should_be_bigger_than_B > B: 
    break  
  else:
    Should_be_bigger_than_B = 0

if Should_be_bigger_than_B <= B:
  T = -1

# please do not modify the input and print statements
# and make sure that your code does not have any other print statements

print(T)
