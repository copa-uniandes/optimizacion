# -*- coding: utf-8 -*-
from math import sin, cos, pi
import matplotlib.pyplot as plt
from MetodoGrafico import *
from typing import Tuple

def miRadar(x, d, n = 8):
	'''
	Se usa la ecuación paramétrica del circulo para crear un radar circular. 
	Puede consultar el siguiente link para mas información sobre esta ecuación:
	http://jwilson.coe.uga.edu/EMAT6680Fa05/Schultz/Assignment10/Parametric_Circles#:~:text=In%20parametric%20equations%2C%20each%20variable,0%2C%202*pi%5D).&text=At%20t%3D0%2C%20x%20%3D,or%20(1%2C%200) 

	ROUTINE:
		miRadar(x,d)
	PURPOSE:
		Crear los puntos en el radar de búsqueda. 	

	ARGUMENTS:
		x (tuple): Punto central del radar.
		d (float): Radio del radar de búsqueda.
	
	RETURN VALUE:
		Una lista con los puntos en el radar.

	EXAMPLE:
		puntosRadar = radar((0,0),1)
	'''
	if type(x) == tuple:
		if len(x) == 2:
			t=[i/(n/2)*pi for i in range(n)]						#Se guardan los valores del parámetro t en los que se evalua la ecuación paramétrica del circulo en una lista: [0, π/4, 2π/4, 3π/4, π, 5π/4, 6π/4, 7π/4, 2π].
			puntos=[(x[0]+d*cos(i),x[1]+d*sin(i)) for i  in t]		#Se evalua la ecuación paramétrica del círculo en cada uno de los puntos de la lista t y se guardan en una lista.
			return puntos 											#Retorna los puntos del radar centrado en x con radio d
		else:
			raise TypeError("La posición inicial debe ser una tupla de dos números")
	else:
		raise TypeError("La posición inicial debe ser una tupla de dos números")

def busquedaLocal(f,restricciones,radar,x0,d0):
	'''
	Corre un algorítmo sencillo de búsqueda local.	

	ROUTINE:
		busquedaLocal(f,restricciones,radar,x0)
	PURPOSE:
		Encontrar un punto (x1,x2) que mejore el valor de la función objetivo f,
		cumpliendo con todas las restricciones.

	ARGUMENTS:
		f (function): Función objetivo a minimizar.
		restricciones (list): Lista de funciones booleanas que evaluan factibilidad del punto x.
		radar (function): Función que dado un punto central y un radio del radar,
		retorna los puntos en el radar de búsqueda.
		x0 (tuple): Punto donde se inicia la búsqueda local.
		d0 (float): Radio del radar de búsqueda.		

	RETURN VALUE:
		Punto factible (x1,x2) con mejor función objetivo encontrado.
	
	EXAMPLE:
		xStar=busquedaLocal(f,restricciones,radar,x0,d0)
	'''
	Termine=False									#Variable booleana con la condición de parada. El algorítmo termina cuando Termine==True.
	xStar=x0										#La variable xStar guardará el mejor punto encontrado. Por ahora el punto inicial x0.

	while not Termine:								#Mientras que no se haya terminado se repite el la búsqueda
		Termine=True								#Se establece la condición de parada en True
		candidatos=radar(xStar,d0)					#Se usa la función radar para obtener los puntos a evaluar 
		for p in candidatos:						#Se evaluan todos los puntos en el radar			
			if f(*p)<f(*xStar):						#Si el punto a evaluar tiene valor en la función objetivo menor al punto actual, es candidato a ser el nuevo mejor punto y se evalua factibilidad.
				Factible=True						#Se asume que el punto p es factible
				for r in restricciones:				#Se evalua que el punto p cumpla todas las restricciones	
					if not r(*p):					#Si el punto p no cumple la restricción r
						Factible=False				#Se establece la variable Factible en False
						break						#Se detiene la búsqueda, pues basta que el punto p incupla una restriccion para que sea infactible				
				if Factible:						#Si el punto p es factible (i.e., Factible==True), el nuevo mejor punto es p
					xStar=p 						#Se actualiza el mejor punto
					Termine=False					#Si se encontró un mejor punto factible quiere decir que la búsqueda no ha terminado
	
	return xStar									#Se retorna el mejor punto encontrado

def busquedaLocalGrafica(f,restricciones,radar,x0,d0,xlim,ylim):
	'''
	Corre un algorítmo sencillo de búsqueda local.	

	ROUTINE:
		busquedaLocal(f,restricciones,radar,x0)
	PURPOSE:
		Encontrar un punto (x1,x2) que mejore el valor de la función objetivo f, cumpliendo con todas las restricciones.

	ARGUMENTS:
		f (function): Función objetivo a minimizar.
		restricciones (list): Lista de funciones booleanas que evaluan factibilidad del punto x.
		radar (function): Función que dado un punto central y un radio del radar, retorna los puntos en el radar de búsqueda.
		x0 (tuple): Punto donde se inicia la búsqueda local.
		d0 (float): Radio del radar de búsqueda.		
	
	RETURN VALUE:
		Punto factible (x1,x2) con mejor función objetivo encontrado.
	
	EXAMPLE:
		xStar=busquedaLocal(f,restricciones,radar,x0,d0)
	'''
	
	X=[x0]
	Termine=False	
	xStar=x0

	while not Termine:
		Termine=True
		candidatos=radar(xStar,d0)		#Se usa la función radar para obtener los puntos a evaluar 
		for p in candidatos:	#Se evaluan todos los puntos en el radar						
			if f(p[0],p[1])<f(xStar[0],xStar[1]):	#Si el punto a evaluar tiene valor en la función objetivo menor al punto actual, es candidato a ser el nuevo mejor punto y se evalua factibilidad.
				#print('entre')
				Factible=True
				for r in restricciones:
					#print(r(p))
					if not r(p[0],p[1]):
						Factible=False
						break
				
				if Factible:		
					xStar=p
					Termine=False
		
		X.append(xStar)		
	
	
	ax=metodoGrafico(f,restricciones,grad=None,xlim=xlim,ylim=ylim)
	h=(xlim[1]-xlim[0])/100
	for x,dx in zip(X[:-1],X[1:]):
		ax.arrow(x[0],x[1],dx[0]-x[0],dx[1]-x[1],head_length=h,head_width=h,length_includes_head=True)

	plt.show()
	
	fig = plt.figure(figsize=(12,8))
	ax = fig.add_subplot(111)

	F=[f(x1,x2) for x1,x2 in X]
	ax.plot(range(len(X)),F,'-o')
	plt.xlabel('Iteraciones')
	plt.ylabel('Función objetivo')
	plt.show()

if __name__=='__main__':
	pass
