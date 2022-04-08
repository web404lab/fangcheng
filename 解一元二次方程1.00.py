'''
本程序由蜗牛的告白制做
2022.4.6
'''
for i in range(3):

    a=eval(input('二次项系数：'))
    b=eval(input("一次项系数："))
    c=eval(input("常数项"))
    if a==0:
        print("这不是一元二次方程")
    elif b**2-4*a*c<0:
        print('原方程没有实数根')
    elif b**2-4*a*c>0:
         x1=(((b**2)-4*a*c)**0.5-b)/2*a
         x2=(-((b**2)-4*a*c)**0.5-b)/2*a
         print('x1=',x1,'   ',"x2=",x2)
    else:
        x1=(((b**2)-4*a*c)**0.5-b)/2*a
        print('x1=x2=',x1)
for x in range(10):
    print('再用这个程序算下去你迟早会被计算机所替代')
