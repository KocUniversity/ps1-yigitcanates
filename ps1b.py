n, B = list(map(int, input().strip().split()))
T = 0

# your code here
low = 0
high = 10000
T = (high+low)//2 

Should_be_bigger_than_B = 0 

Smallest_T_at_the_moment = 0

while True:
  
  for i in range(1, (n+1)):  
    if i%2 == 0:
      Should_be_bigger_than_B += ((2**i)+1)**(n-i)*T
    else:
      Should_be_bigger_than_B += ((3**i)+1)**(n-i)*T

  if Should_be_bigger_than_B <= B:
    if high-low <= 1:
      break
    low = T
    T = (high+low)//2
    Should_be_bigger_than_B = 0 

  elif Should_be_bigger_than_B > B:
    if high-low <= 1:
      break
    Smallest_T_at_the_moment = T 
    high = T
    T = (high+low)//2
    Should_be_bigger_than_B = 0 


T = Smallest_T_at_the_moment 

if T == 0:
  T = -1


# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)