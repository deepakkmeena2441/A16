tuple1 = (11, [22, 33], 44, 55)
w=list(tuple1)
w[1][0]=222
print(tuple(w))