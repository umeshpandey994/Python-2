def power(x,e,m):
    y=1
    while e>0:
        if e%2==0:
            x=(x*x)%m
            e=e/2
        else:
            y=(x*y)%m
            e=e-1
    return y 
