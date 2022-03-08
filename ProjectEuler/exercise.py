#region exercise 1

'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

mul = 0
for i in range(1000):
    mul3 = i%3
    mul5 = i%5
    if mul3 == 0 or mul5 == 0:
        mul = mul + i
print(mul)

#endregion

#region exercise 2

'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

total=0
def fib(n):
    fibo = []
    for i in range(1,101):
        if i<=2:
            fibo.append(1)
        if i>2:
            x = fibo[i-3]
            y = fibo[i-2]
            z = x + y
            fibo.append(z)
            
    return fibo

num = fib(100)

total = 0
i=0
while num[i]<4000000:
    if num[i]%2==0:
        total = total + num[i]
    i=i+1
print(total)

#endregion

#region exercise 3

'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def Largest_Prime_Factor(n):
    prime_factor = 1
    i = 2

    while i <= n / i:
        if n % i == 0:
            prime_factor = i
            n /= i
        else:
            i += 1

    if prime_factor < n:
        prime_factor = n

    return prime_factor

print(int(Largest_Prime_Factor(600851475143)))

#endregion

#region exercise 4

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

num_one = 999
num_two = 999
palindromic = []

for i in range(100, num_one+1):
    for j in range(100, num_two+1):
        num = i*j
        if num>=100000:
            c = num%10
            d = (num%100)/10
            d = int(d)
            e = (num%1000)/100
            e = int(e)
            f = (num%10000)/1000
            f = int(f)
            g = (num%100000)/10000
            g = int(g)
            h = (num%1000000)/100000
            h = int(h)

            if (h-c==0 or c-h==0) and (g-d==0 or d-g==0) and (f-e==0 or e-f==0):
                final = num
                palindromic.append(final)

print(int(max(palindromic)))

#endregion

#region exercise 5

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def prime(num):
    my_list=list(range(2,num+1))
    n = num
    lista = my_list[::-1]
    while num>0:
        for i in lista:
            if num%i!=0:
                num = num+n
                break
        if i == 2:
            break
    return print(num)

prime(20)

#endregion

#region exercise 6

'''
The sum of the squares of the first ten natural numbers is, 385
The square of the sum of the first ten natural numbers is, 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

num = 100

sum_cua = (num*(num+1)*(2*num+1))/6
sum_nan = (1+num)*(num/2)
sum_nan = sum_nan*sum_nan
total=sum_nan-sum_cua
print(int(total))

#endregion

#region exercise 7

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

i = 9
ultimo = [2, 3, 5, 7]

while len(ultimo)!=10001:
  j=0
  for j in ultimo:
    if i%j == 0:
      i += 1
      break
  else:
    ultimo.append(i)
    i += 1

print(ultimo.pop())

#endregion

#region exercise 8

'''
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
'''

import functools
from functools import reduce
num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
x = [int(a) for a in str(num)]
resultado_final =[0]
i=0
while i!=1000:
  vec = x[i:i+13]
  if len(vec)==13:
    def multi(x,y):
      return x*y
    resultado = reduce(multi, vec)
    resultado_final.append(resultado)
  i += 1
print(max(resultado_final))

#endregion