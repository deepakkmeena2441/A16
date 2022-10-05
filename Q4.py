from turtle import TurtleGraphicsError
t=tuple([eval(e)  for e in input().split(",")])
print(t)
w=list(t)
q=w[1]
w[1]=w[2]
w[2]=q


print(tuple(w))
