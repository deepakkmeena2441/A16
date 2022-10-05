l=tuple([eval(e)for e in input().split(",") ])
w=list(l)
result=w.count(w[0]==len(w))
if(result):
    print(" all element are same")
else:
    print(" all element are not same") 

