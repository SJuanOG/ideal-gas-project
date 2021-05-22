#Algoritmo realizado por 
#Laura Camila Pardo Suarez
#Juan Pablo Ortiz Gil 
import numpy as np
import matplotlib.pyplot as plt
import os 
 
os.system('clear') 
input(" --------------------------------------------------------------------------------------------------------------------------\n Este programa, por medio de las ecuaciones de estado de Van der Waals, Berthelot (gases reales) y la ecuación de gas ideal\n permite la realización de calculos de complejidad media y sus respectivas graficas, las cuales sirven para\n comparar resultados y analizar el comportamiento de dicho gas\n --------------------------------------------------------------------------------------------------------------------------\n Las graficas representan los isotermas de cada gas que se desee analizar, por lo tanto se deben ingresar\n las temperaturas a las cuales se quiere conocer y las condiciones que esta presenta\n como el volumen máximo a evaluar y el número de moles\n --------------------------------------------------------------------------------------------------------------------------\n (pulse enter para iniciar)")
os.system('clear')
Vm = float(input("Ingrese el volumen(L/mol) maximo que desea evaluar >= 0.1: "))
datos = input("Ingrese tres temperaturas(K) a evaluar en el sistema (sep. por coma): ")
t1, t2, t3 = [float(i) for i in datos.split(",")]
os.system('clear')
gas = int(input("¿Que gas desea evaluar?\n 1.Aire\n 2.NH3\n 3.CO2\n 4.H2\n 5.CH4\n 6.CO\n 7.N2\n 8.O2\n "))
n = float(input("Ingrese el numero de moles del gas que ha elegido >= 2: "))

gases = {"Aire":{"a":1.330,
                 "b":0.036},
         "NH3":{"a":4.170,
                "b":0.037},
         "CO2":{"a":3.590,
                "b":0.043},
         "H2":{"a":0.240,
               "b":0.027},
         "CH4":{"a":2.250,
                "b":0.043},
         "CO":{"a":1.490,
               "b":0.040},
         "N2":{"a":1.390,
               "b":0.03913},
         "O2":{"a":1.360,
               "b":0.032}}

if gas == 1:
    a = gases["Aire"]["a"]
    b = gases["Aire"]["b"]

if gas == 2:
    a = gases["NH3"]["a"]
    b = gases["NH3"]["b"]
    
if gas == 3:
    a = gases["CO2"]["a"]
    b = gases["CO2"]["b"]

if gas == 4:
    a = gases["H2"]["a"]
    b = gases["H2"]["b"]
    
if gas == 5:
    a = gases["CH4"]["a"]
    b = gases["CH4"]["b"]
    
if gas == 6:
    a = gases["CO"]["a"]
    b = gases["CO"]["b"]

if gas == 7:
    a = gases["N2"]["a"]
    b = gases["N2"]["b"]

if gas == 8:
    a = gases["O2"]["a"]
    b = gases["O2"]["b"]

v = np.arange(0.1,Vm+0.1,0.01)
v = v[1:]

R = 0.08205746

p1 = np.zeros_like(v)
for i in range(len(v)):
    p1[i] = ((n*R*t1)/(v[i]- n*b)) - ((a*n**2)/(v[i]**2))
p2 = np.zeros_like(v)
for i in range(len(v)):
    p2[i] = ((n*R*t2)/(v[i]- n*b)) - ((a*n**2)/(v[i]**2))
p3 = np.zeros_like(v)
for i in range(len(v)):
    p3[i] = ((n*R*t3)/(v[i]- n*b)) - ((a*n**2)/(v[i]**2))
    
p5 = np.zeros_like(v)
for i in range(len(v)):
    p5[i] = (n*R*t1)/(v[i])
p6 = np.zeros_like(v)
for i in range(len(v)):
    p6[i] = (n*R*t2)/(v[i])
p7 = np.zeros_like(v)
for i in range(len(v)):
    p7[i] = (n*R*t3)/(v[i])

v4 = np.linspace(0.1,Vm+0.1,len(v))

os.system('clear')

plt.figure()
plt.plot(v4, p1, 'r-', label="T(K)= "+str(t1))
plt.plot(v4, p2, 'g-', label="T(K)= "+str(t2))
plt.plot(v4, p3, 'k-', label="T(K)= "+str(t3))
plt.xlabel("V[L/mol]")
plt.ylabel("P[atm]")
plt.xlim(xmin=v[0],xmax=Vm)
plt.ylim(ymin=-100,ymax=200)
if gas ==1:
    plt.title("Aire")
if gas ==2:
    plt.title("Amoniaco")
if gas ==3:
    plt.title("Dioxido de carbono")
if gas ==4:
    plt.title("Hidrogeno")
if gas ==5:
    plt.title("Metano")
if gas ==6:
    plt.title("Monoxido de carbono")
if gas ==7:
    plt.title("Nitrogeno")
if gas ==8:
    plt.title("Oxigeno")
plt.grid()
plt.legend()
l = int(input("A continuación se le mostrara el estado del gas segun la ecacion de Van der Waals\n ¿Desea guardar la grafica?\n 1.Si\n 2.No\n "))
if l ==1:
    plt.savefig('Grafica VDW P vs V.pdf')
plt.show()

os.system('clear')

def Biseccion( f, V1, V2, Nmax):
    if f(a)*f(b)>0:
        print("Error, VDW(V1) y VDW(V2) deben tener signos opuestos")
        return False
    V1i = V1
    V2i = V2
    n = 1.0
    while n<=Nmax:
        Vci = (V1i+V2i)/2.0
        if f(Vci)*f(V1i)>0:
            V1i = Vci
        elif f(Vci)*f(V1i)<0:
            V2i = Vci
        n = n+1
    return Vci

Pc = a / (27 * b**2)
Tc = (8*a) / (27*R*b)

Pm = 200

p = np.arange(0.1,Pm+0.1,0.01)
p = p[1:]

v1 = np.zeros_like(p)
for i in range(len(p)):
    v1[i] = ((n*R)*((9 * p[i] * t1**2) - (54 * p[i] * Tc**3) + (128 * Pc * t1**3)))/(128 * p[i] * Pc * t1**2)
v2 = np.zeros_like(p)
for i in range(len(p)):
    v2[i] = ((n*R)*((9 * p[i] * t2**2) - (54 * p[i] * Tc**3) + (128 * Pc * t2**3)))/(128 * p[i] * Pc * t2**2)
v3 = np.zeros_like(p)
for i in range(len(p)):
    v3[i] = ((n*R)*((9 * p[i] * t3**2) - (54 * p[i] * Tc**3) + (128 * Pc * t3**3)))/(128 * p[i] * Pc * t3**2)

p4 = np.linspace(0.1,Pm+0.1,len(p))

os.system('clear')

plt.figure()
plt.plot(v1, p4, 'r-', label="T(K)= "+str(t1))
plt.plot(v2, p4, 'g-', label="T(K)= "+str(t2))
plt.plot(v3, p4, 'k-', label="T(K)= "+str(t3))
plt.xlabel("V[L/mol]")
plt.ylabel("P[atm]")
plt.xlim(xmin=v[0],xmax=Vm)
plt.ylim(ymin=-100,ymax=Pm)
if gas ==1:
    plt.title("Aire")
if gas ==2:
    plt.title("Amoniaco")
if gas ==3:
    plt.title("Dioxido de carbono")
if gas ==4:
    plt.title("Hidrogeno")
if gas ==5:
    plt.title("Metano")
if gas ==6:
    plt.title("Monoxido de carbono")
if gas ==7:
    plt.title("Nitrogeno")
if gas ==8:
    plt.title("Oxigeno")
plt.grid()
plt.legend()
m = int(input("A continuación se le mostrara el estado del gas segun la ecacion de Berthelot\n ¿Desea guardar la grafica?\n 1.Si\n 2.No\n "))
if m ==1:
    plt.savefig('Grafica B P vs V.pdf')
plt.show()

os.system('clear')

plt.figure(3)

plt.subplot(221)
plt.plot(v4, p1, 'r-', label="T(K)= "+str(t1))
plt.plot(v4, p2, 'g-', label="T(K)= "+str(t2))
plt.plot(v4, p3, 'k-', label="T(K)= "+str(t3))
plt.xlabel("V[L/mol]")
plt.ylabel("P[atm]")
plt.xlim(xmin=v[0],xmax=Vm)
plt.ylim(ymin=-100,ymax=200)
plt.title("Van der Waals")
plt.grid()
plt.legend()

plt.subplot(222)
plt.plot(v1, p4, 'r-', label="T(K)= "+str(t1))
plt.plot(v2, p4, 'g-', label="T(K)= "+str(t2))
plt.plot(v3, p4, 'k-', label="T(K)= "+str(t3))
plt.xlabel("V[L/mol]")
plt.ylabel("P[atm]")
plt.xlim(xmin=v[0],xmax=Vm)
plt.ylim(ymin=-100,ymax=Pm)
plt.title("Berthelot")
plt.grid()
plt.legend()

plt.subplot(223)
plt.plot(v4, p5, 'r-', label="T(K)= "+str(t1))
plt.plot(v4, p6, 'g-', label="T(K)= "+str(t2))
plt.plot(v4, p7, 'k-', label="T(K)= "+str(t3))
plt.xlabel("V[L/mol]")
plt.ylabel("P[atm]")
plt.xlim(xmin=v[0],xmax=Vm)
plt.ylim(ymin=-100,ymax=200)
plt.title("Gases Ideales")
plt.grid()
plt.legend()

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,wspace=0.35)
v = int(input("A continuación se le mostrara la comparacion de las anteriores y como actuarian si se evaluara sobre un gas ideal\n ¿Desea guardar la grafica?\n 1.Si\n 2.No\n "))
if v ==1:
    plt.savefig('Graficas P vs V.pdf')
plt.show()

os.system('clear')

def Funcion_VDW(Vc):
    global R
    global Pc
    global Tc
    global a
    global b
    vdw = (Pc + a/(Vc**2) )*(Vc - b) - R*Tc
    return vdw

input(" --------------------------------------------------------------------------------------------------------------------------\n Para esta parte del programa, con la ecuación de Van der Waals, se hallarán los ceros de la función  con el fin de determinar\n el volumen crítico junto con la temperatura y presión críticas, las cuales se acercan a un comportamiento comportamiento\n similar a un gas ideal. Esto se realiza con la intención de encontrar un método no teórico que calcule dicho volumen\n y que pueda ser comparado con el teórico y hallar el error del método numérico frente al teórico.\n --------------------------------------------------------------------------------------------------------------------------\n Para este se le pediran al usuario valores para delimitar los ceros de la función y un número máximo de iteraciones\n que serviran para determinar la exactitud del calculo anteriormente mencionado\n --------------------------------------------------------------------------------------------------------------------------\n (pulse enter para continuar)")

os.system('clear')

j = int(input("¿Desea escribir sus propios valores para acotar los ceros de la funcion?\n 1.Si [No Recomendado]\n 2.No\n "))
if j ==1:
    V1 = float(input("Ingrese el primer valor para acotar: "))
    V2 = float(input("Ingrese el segundo valor para acotar: "))
if j ==2:
    V1 = (1/8)*(Tc*R)/(Pc)
    V2 = ((R*Tc)/Pc)

Nmax = int(input("Ingrese el numero maximo de interaciones que desea realizar: "))

Vc = Biseccion(Funcion_VDW, V1, V2, Nmax)

print("El valor calculado del volumen critico(Vc) es de: %.3f L/mol"%Vc)
print("El valor teorico del volumen critico(Vc) es de: %.3f L/mol"%(V2*(3/8)))
print("El error del volumen critico(Vc) es de: ", np.fabs(Vc-(V2*(3/8))))
print("El valor de la temperatura critica(Tc) es de: %.3f K"%Tc)
print("El valor de la presion critica(Pc) es de: %.3f atm"%Pc)

