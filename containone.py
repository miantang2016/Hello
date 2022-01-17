import os
import sys



# How many whole numbers between 1 and 1000 do not contain the digit 1?

# num = 100
# num_s = '100'


counter = 0
for num in range(1, 1001):
    num_s = str(num)
    if not '1' in num_s: 
        counter = counter + 1

print('The total whoe numbers is ' + str(counter))