from numpy import zeros
from matplotlib import pyplot as plt


# QUESTÃO 1

#função de Euler
a=float 
b=float
h=float
y0=float

def euler(a, b, h, y0, f):
    n = int((b - a)/h)
    x = zeros([n+1,1])
    y = zeros([n+1,1])
    x[1] = a
    y[1] = y0
    for k in range(1,n):
        y[k+1] = y[k] + h * f(x[k],  y[k])
        x[k+1] = x[k] + h
    return x,y
  
#função de  Runge-Kutta de 3aordem
def rk3(a, b, h, y0, f):
  n=int((b - a)/h)
  x = zeros([n+1,1])
  y = zeros([n+1,1])
  x[1] = a
  y[1] = y0
  for k in range(1, n):
      f1 = f(x[k], y[k])
      f2 = f(x[k] + h/2, y[k] + h/2 * f1)
      f3 = f(x[k] + h, y[k] + 2*h*f2 - h*f1)
      y[k+1] = y[k] + h/6 * (f1 + 4*f2 + f3)
      x[k+1] = x[k] + h
  return x,y

#definição da funçã questão 1 
def f (a,b):
  dbda=((-2*a*b+10)/5)
  return dbda

#solicitação e impressão de Runge-Kutta de 3ª ordem
sol_rk3=rk3(0,1,0.1,0,f)

print ("A resoluçã por  Runge-Kutta de 3ª ordem\n\n Valores de x:")
print (sol_rk3[0])

print ("\nValores de y:")
print (sol_rk3[1])


#solicitação e impressão de Euler
sol_euler=euler(0,1,0.1,0,f)

print ("\nA resolução por Euler\n\n Valores de x:")
print (sol_euler[0])

print ("\nValores de y:")
print (sol_euler[1])




#///////////////////////#

#Questão 2

def heun(a, b, h, y0, f):
    n = int((b - a)/h)
    x = zeros([n+1,1])
    y = zeros([n+1,1])
    p = zeros([n+1,1])
    x[1] = a
    y[1] = y0
    for k in range(1,n):
        x[k+1] = x[k] + h
        p[k+1] = y[k] + h*f(x[k],y[k])
        y[k+1] = y[k] + h/2*(f(x[k],  y[k]) + f(x[k+1], p[k+1]))
    return x,y
  

def rk4(a, b, h, y0, f):
    n = int((b - a)/h)
    x = zeros([n+1,1])
    y = zeros([n+1,1])
    x[1] = a
    y[1] = y0
    for k in range(1,n):
        f1 = f(x[k], y[k])
        f2 = f(x[k] + h/2, y[k] + h/2 * f1)
        f3 = f(x[k] + h/2, y[k] + h/2 * f2)
        f4 =  f(x[k] + h, y[k] + h * f3)
        y[k+1] = y[k] + h/6 * (f1 + 2*f2 + 2*f3 + f4)
        x[k+1] = x[k] + h
    return x,y  

#definição da funçã questão 2
def g (c,f):
  dfdc=c**(1/3)
  return dfdc


#solicitação e impressão de Heun
sol_heun=heun(0,1,0.1,0,g)

print ("\nA resolução por Heun\n\n Valores de x:")
print (sol_heun[0])

print ("\nValores de y:")
print (sol_heun[1])

#solicitação e impressão de #função de  Runge-Kutta de 4ª ordem
sol_rk4=rk4(0,1,0.1,0,g)

print ("\nA resolução por Runge-Kutta de 4ª ordem\n\n Valores de x:")
print (sol_rk4[0])

print ("\nValores de y:")
print (sol_rk4[1])



#plotando o grafico
fig,(graf1, graf2)=plt.subplots(nrows=1, ncols=2,constrained_layout=True)
graf1.plot(sol_rk3[0], sol_rk3[1], 'g',  label='Runge-Kutta de 3ª ordem', marker='o')
graf1.plot(sol_euler[0],sol_euler[1], 'b',label='Euler', marker='o')
graf1.set_ylabel('Valores de y')
graf1.set_xlabel('Valores de x')
graf1.set_title('Solução Euler e Runge-Kutta de 3ª ordem')
#plt.scatter(sol_rk3[0], sol_rk3[1], color='green')
#plt.scatter(sol_euler[0],sol_euler[1], color='blue' )

#plt.show()


graf2.plot(sol_heun[0], sol_heun[1], 'r',  label='Heun', marker='o')
graf2.plot(sol_rk4[0],sol_rk4[1], 'y',label='Runge-Kutta de 4ª ordem', marker='o')
graf2.set_ylabel('Valores de y')
graf2.set_xlabel('Valores de x')
graf2.set_title('Solução Heun e Runge-Kutta de 4ª ordem')
#plt.scatter(sol_heun[0], sol_heun[1],color='red')
#plt.scatter(sol_rk4[0],sol_rk4[1], color='yellow' )

plt.show()
