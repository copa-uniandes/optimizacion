# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.colors as col
import numpy as np

from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection


def AND(l):
	r=l[0]
	for i in l:
		r=r & i
	return r

def metodoGrafico(fo,constraints,grad=None,xlim=[-0.2,5],ylim=[-0.2,5]):
	'''
	Crea una gráfica con el método gráfico.
	
	Input:
		- fo (función de python): Función objetivo
		- constraints (Lista fuciones): Lista que continene las restricciones. Cada restricción es una función booleana que evaua cada punto										 
		-grad (Tupla o lista): Las componentes del gradiente.
		
		-xlim (Tupla o lista): Los limites inferiores y superiores del eje x de la gráfica.
		-ylim (Tupla o lista): Los limites inferiores y superiores del eje y de la gráfica.

	Output:
		-None
		- Muestra una grafica con la región factible e isoclinas.
	'''

	fig = plt.figure(figsize=(12,8))
	ax = fig.add_subplot(111)

	d = np.linspace(min(xlim[0],ylim[0]),max(xlim[1],ylim[1]),2000)
	x,y = np.meshgrid(d,d)
	
		
	if grad!=None:
		leng=1/10*(grad[0]**2+grad[1]**2)**(0.5)
		print(leng)
		plt.arrow(0,0,grad[0],grad[1],head_width=leng/2,head_length=leng,color="black")#Plots Grad
		plt.text(grad[0]/2+2*leng,grad[1]/2,r'$\nabla Z$=('+str(grad[0])+","+str(grad[1])+")",size=15 )
	


	z=fo(x,y) 

	cmap=plt.get_cmap('cool')
	cs = ax.contour(x,y,z,40 ,cmap=cmap) #Plots isoclines of Z
	ax.clabel(cs, fontsize=8) #Plots labels of isoclines of Z

	

	#(f(x,y)<=0) & (g(x,y)<=2) &(x>=0) & (y>=0)
	#[x>=0,y>=0]
	if len(constraints)>0:
		z = (AND([f(x,y) for f in constraints])).astype(int) 
		#cmap = col.ListedColormap(["lime","lime"])
		plt.contourf(x,y,z, [0.99999, 1.00001], cmap=col.ListedColormap(["lime","lime"]),alpha=0.3)
		plt.contour(x,y,z, [0.99999, 1.00001], cmap=col.ListedColormap(["k","k"]),alpha=1)

	#plt.plot(1/2,5/2,'o',markersize=10,color='g')

	plt.xlim(xlim)
	plt.ylim(ylim)
	plt.xlabel("Coordenada x")
	plt.ylabel("Coordenada y")

	#fig.colorbar(cm.ScalarMappable(norm=[0,1], cmap=cmap), ax=ax)

	return ax



if __name__=='__main__':
	'''
	Ejemplo
	'''

	fo=lambda x,y: abs((1/2)*x) +abs((1/2)*(y-3)) #Se define la función Objetivo. No tiene que ser con una lambda function
	

	'''
	Se definen todas las restricciones que sean necesarioas, no tiene que ser con lambda functions
	'''
	f = lambda x,y : x**2-y<=0
	g = lambda x,y : -x+y<=2

	#Se ponen las restricciones en una lista que tiene la función 
	constraints=[f,g]

	'''
	Se llama la funcion de meetodo gráfico con los argumentos necesarios.	
	En este caso como la Fo no es lineal no se pintaba el gradiente, 
	pero para una fo lineal se pone el gradiente de la función en forma de lista en el parámetro grad.
	'''
	metodoGrafico(fo,constraints,grad=None,xlim=[-3,3],ylim=[-0.2,5])
	plt.show()


