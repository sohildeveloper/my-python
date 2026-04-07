"""mathceil function in biled metherd rahta hai isme ye float value nhi intiger value deta 
hai agar hamene 12.3 diya to ye uske age ki value dega 13 float valuve nhi dega integer 
value dega isliye mathceil metherd use hota hai """
import math
x=12.2
print(math.ceil(x))

"""math.fabs matherd ye hame absalute value return karega mtlb ki ye ham jese - me value dege to ye hame pluse me dega 
jese -20 diyato ye hame return kare 20.0 ese """
v=-30
print(math.fabs(v))

"""ye abe factorial numaber dega 5 ka Kisi number n ka factorial likhte hain n!
Iska matlab hota hai:
1 se lekar n tak sab numbers ka multiplication"""
a=5
print(math.factorial(a))


s=20.5
print(math.floor(s))
# outpur 20 

"""fsum list or tapule ki value ka sum kar deta hai """
l=[10,20,30,40,50]
print(math.fsum(l))


sq=30
print(math.sqrt(sq))


# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result

# print(factorial(10))  # 120
