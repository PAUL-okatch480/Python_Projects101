from collections import deque
queue=deque(["Paul","John","James"])
queue.append("Ringo")
queue.append("George")
print(queue)
#implementation of queues using lists. We import from collections beause lists methods are not very efficient
print(queue.popleft())
print(queue.popleft())
print(queue)
squares=[]
for x in range(10):
    squares.append(x**2)
print(squares)
#the above code can be written in a more compact way using list comprehension
squares1=[x**2 for x in range(10)]
print(squares1)
#similarly
squares2=list(map(lambda x:x**2, range(10)))
print(squares2)
#list comprehension
combs=[(x,y) for x in [1,2,3] for y in [3,1,4] if x !=y]
print(combs)

combs1=[]
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs1.append((x,y))
print(combs1)
#a delv into the lambda function
sum=lambda x,y: x+y
print(sum(2,3))

def sum(x,y):
    return x + y
print(sum(3,4))
#illustartion of the working of a map function
def fahreinheit(T):
    return ((float(9)/5)*T + 32)

def celcius(T):
    return (float(5)/9)*(T-32)
temperatures = (36.5, 37, 37.5, 38, 39)
F = map(fahreinheit, temperatures)
C= map(celcius, F)
temperature_in_fahrenheit=list(map(fahreinheit, temperatures))
temperatures_in_celcius=list(map(celcius, temperature_in_fahrenheit))
print(temperature_in_fahrenheit)
print(temperatures_in_celcius)
#when we use the lambda function, we can write the above code as follows
c=[39.2, 36.5, 37.3, 37.8]
F=list(map(lambda x: (float(9)/5)*x + 32, c))
C=list(map(lambda x: (float(5)/9)*(x-32), F))
print(F)
print(C)
