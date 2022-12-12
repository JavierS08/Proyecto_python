from builtins import int

import pandas as pd
from urllib import request as rq
import requests
import numpy as np
import ssl
import xlrd
from statistics import mode

from functools import reduce
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.ine.es/jaxiT3/files/t/es/xls/32449.xls?nocab=1"

filexls ='recursos/filexls.xlsx'
rq.urlretrieve(url, filexls)
fichero_excel = pd.ExcelFile('recursos/filexls.xlsx' )
dataframe = fichero_excel.parse('tabla-32449', header=6)

#print(dataframe.shape)
filas=dataframe.tail(805)
filas=filas.head(799)

nulo=dataframe["2021"][0]

filas=filas.replace({nulo:0})

arr=[]
def arr():
    ind=filas.iloc[2,0:28]
    ser=pd.Series(ind)
    arr=np.array(ser)

    lis=arr.tolist()
    print(lis)
arr()

def tupl():
    ind=filas.iloc[10,0:28]
    ser=pd.Series(ind)
    arr=np.array(ser)
    tupla=tuple(arr)
    print(tupla)

tupl()
def dic():
    ind=filas.iloc[80,0:28]
    dic=ind.to_dict()
    print(dic)

dic()
def invertir():
    dfi=filas.transpose()
    print(dfi)

with open("lista.txt" , "wt") as fich:
    ind=filas.iloc[2,0:28]
    ser=pd.Series(ind)
    arr=np.array(ser)
    for x in range(1,len(arr)):
        print(arr[x])
        fich.write(str(arr[x])+" ")
   

invertir()


def calcmod(año):
    df=filas[año]
    return mode(df)

def calcvar(año):
    df=filas[año]
    return np.var(df)
    
def calcmed(año):
    df=filas[año]
    return np.mean(df)

print("Moda:")
print(calcmod("2020"))
print("Media:")
print(calcmed("2020"))
print("Varianza:")
print(calcvar("2020"))


def mapi():
    filas["2025"]=filas["2020"].map(lambda x:300+x)
    print(filas)
mapi()

def filtro(age1):
    filt=filas.filter(items=[age1])
    print(filt)
    
    
filtro('2003')

import sqlite3
conn = sqlite3.connect('dato1.db',timeout=10)
c = conn.cursor()
filas.iloc[:,1:42].to_sql('dfSoloParo', conn, if_exists='replace')

#Seleccionamos todos los valores que estén en la fila 6
res=c.execute('SELECT * from "dfSoloParo" WHERE "index"=6')

print(res.fetchall())


#Seleccionamos todos los valores de la columna 2020
resu=c.execute('SELECT "2020" from "dfSoloParo"')

print(resu.fetchall())

#Seleccionamos todos los valores de la columna 2020 cuyos valores sean menores a 1000
resui=c.execute('SELECT "2020" from "dfSoloParo" WHERE "2020"<"1000"')
print("---------------------------------------------------------------------------------------")
print(resui.fetchall())

print("---------------------------------------------------------------------------------------")
#Guardar datos consulta en un Dataframe
dti=pd.DataFrame
def guar():
    arry=[]
    for row in c.execute('SELECT "2020" from "dfSoloParo" WHERE "2020"<"1000"'):
        print(row)
        arry.append(row)
    print("---------------------------------------------------------------------------------------")
    dti=pd.DataFrame(arry)
    print(dti)
    dti.to_sql(name='2020_1000', con=conn, if_exists='replace')
guar()

neg=dataframe["2020"][325]

conn.close()


class Datos():
    def __init__(self,a):
        self.a=a
    def __str__(self):
        print(f"Columna: {filas[self.a]}")


    def edit(self,fil):
        dec=input("Que quieres hacer aumentar o disminuir los valores\n")
        if(dec=="aumentar"):
            aum=input("¿Cúanto?\n")
            aum=int(aum)
            print(filas[fil].map(lambda x:x+aum))

        elif(dec=="disminuir"):
            aum=input("¿Cúanto?\n")
            aum = int(aum)
            print(filas[fil].map(lambda x: x - aum))

    def sumi(self,fil):
        print(sum(filas[fil]))
    def resta(self,fil):
        def rest(x,y):
            return x - y
        fril=filas[fil]
        y=pd.Series(fril)
        z=np.array(y)
        orden=sorted(z,reverse=True)
        print(orden)
        resul=reduce(rest,orden)
        print(resul)
    def __le__(self, other):
        su=sum(filas[self.a])
        print(f"Sumatorio {self.a}={su}")
        print(f"Sumatorio {other}={sum(filas[other])}")
        if(su<=sum(filas[other])):
            print(f"Los valores de la columna {self.a} es menor o igual que {other}")
        else:
            print(f"Los valores de la columna {other} es mayor o igual que {self.a}")

    def __lt__(self, other):
        su=sum(filas[self.a])
        print(f"Sumatorio {self.a}={su}")
        print(f"Sumatorio {other}={sum(filas[other])}")
        if(su<sum(filas[other])):
            print(f"Los valores de la columna {self.a} es menor que {other}")
        else:
            print(f"Los valores de la columna {other} es mayor que {self.a}")
    def __eq__(self, other):
        su = sum(filas[self.a])
        print(f"Sumatorio {self.a}={su}")
        print(f"Sumatorio {other}={sum(filas[other])}")
        if (su == sum(filas[other])):
            print(f"Los valores de la columna {other} son iguales que {self.a}")
        else:
            print(f"Los valores de la columna {other} no son iguales que {self.a}")

    def __ge__(self, other):
        su=sum(filas[self.a])
        print(f"Sumatorio {self.a}={su}")
        print(f"Sumatorio {other}={sum(filas[other])}")
        if(su<=sum(filas[other])):
            print(f"Los valores de la columna {self.a} es menor o igual que {other}")
        else:
            print(f"Los valores de la columna {other} es mayor o igual que {self.a}")

    def __gt__(self, other):
        su=sum(filas[self.a])
        print(f"Sumatorio {self.a}={su}")
        print(f"Sumatorio {other}={sum(filas[other])}")
        if(su<sum(filas[other])):
            print(f"Los valores de la columna {self.a} es menor que {other}")
        else:
            print(f"Los valores de la columna {other} es mayor que {self.a}")

    def __ne__(self, other):
        su=sum(filas[self.a])
        print(f"Sumatorio {self.a}={su}")
        print(f"Sumatorio {other}={sum(filas[other])}")
        if(su!=sum(filas[other])):
            print(f"Los valores de la columna {self.a} no son iguales que los de la columna {other}")
        else:
            print(f"Los valores de la columna {other} son iguales que los de la columna {self.a}")

print("-----------------------------------------------------------------------------")

dato1=Datos('2003')
dato1.__str__()
dato1.edit("2020")
dato1.sumi('2003')
dato1.resta('2003')
dato1.__le__('2000')
dato1.__eq__('2000')
dato1.__ge__('2000')
dato1.__lt__('2000')
dato1.__gt__('2000')
dato1.__ne__('2000')

dato2=Datos('2001')
dato2.__str__()
dato2.edit("2001")
dato2.sumi('2001')
dato2.resta('2001')
dato2.__le__('2000')
dato2.__eq__('2000')
dato2.__ge__('2000')
dato2.__gt__('2000')
dato2.__ne__('2000')



dato3=Datos('2002')
dato3.__str__()
dato3.edit("2002")
dato3.sumi('2002')
dato3.resta('2002')
dato3.__ge__('2000')
dato3.__gt__('2000')
dato3.__ne__('2000')

dato4=Datos('2000')
dato4.__str__()
dato4.edit("2000")
dato4.sumi('2000')
dato4.resta('2000')
dato4.__ge__('2018')
dato4.__gt__('2018')
dato4.__ne__('2018')


dato5=Datos('2025')
dato5.__str__()
dato5.edit("2025")
dato5.sumi('2025')
dato5.resta('2025')
dato5.__ge__('2000')
dato5.__gt__('2000')
dato5.__ne__('2000')

from matplotlib import pyplot as plt
print("---------------------------------- Gráfico 1 columna --------------------------")


def graf1():
    d=[]
    for i in filas["2003"]:
        d.append(i)
    print(d)
    fig, ax = plt.subplots()
    ax.violinplot(d)
    plt.show()

graf1()
print("---------------------------------- Gráfico 2 columnas --------------------------")

def graf2():
    d1=sum(filas["2003"])
    print(d1)
    d2=sum(filas["2004"])
    print(d2)
    fig, ax = plt.subplots()
    ax.fill_between([0,1,2,3], [0,d1,300,d2])
    plt.show()

graf2()
print("---------------------------------- Gráfico 3 columnas --------------------------")
def graf3():
    d1=sum(filas["2003"])
    print(d1)
    d2=sum(filas["2004"])
    print(d2)
    d3=sum(filas["2002"])
    print(d3)
    fig, ax = plt.subplots()
    ax.pie([d1, d2, d3])
    plt.plot(d1,label="2003")
    plt.plot(d2, label="2004")
    plt.plot(d3, label="2002")
    plt.legend()
    plt.show()

graf3()

print("---------------------------------- Todas las columnas--------------------------")

def graf4():
    d1 = sum(filas["1995"])
    d2 = sum(filas["1996"])
    d3 = sum(filas["1997"])
    d4 = sum(filas["1998"])
    d5 = sum(filas["1999"])
    d6 = sum(filas["2000"])
    d7 = sum(filas["2001"])
    d8 = sum(filas["2002"])
    d9 = sum(filas["2003"])
    d10 = sum(filas["2004"])
    d11 = sum(filas["2005"])
    d12 = sum(filas["2006"])
    d13 = sum(filas["2007"])
    d14 = sum(filas["2008"])
    d15 = sum(filas["2009"])
    d16 = sum(filas["2010"])
    d17 = sum(filas["2011"])
    d18 = sum(filas["2012"])
    d19 = sum(filas["2013"])
    d20 = sum(filas["2014"])
    d21 = sum(filas["2015"])
    d22 = sum(filas["2016"])
    d23 = sum(filas["2017"])
    d24 = sum(filas["2018"])
    d25 = sum(filas["2019"])
    d26 = sum(filas["2020"])
    d28 = sum(filas["2025"])

    fig, ax = plt.subplots()
    x =[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25,d26,d28]
    num_bins = 20
    n, bins, patches = ax.hist(x, num_bins, orientation='horizontal', facecolor =
    'violet')
    plt.show()
graf4()