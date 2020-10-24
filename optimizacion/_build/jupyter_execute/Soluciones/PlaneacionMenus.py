#!/usr/bin/env python
# coding: utf-8

# # Planeación de menús Solución

# ## Enunciado
# 
# El personal técnico de un hospital quiere desarrollar un sistema computarizado de planificación de
# menús. Para comenzar, el hospital llevará a cabo un piloto para planificar el menú del almuerzo.
# Este menú debe incluir 100 gramos (g) de cada uno de los siguientes tres grupos alimenticios ($T$): frutas,
# verduras, y carnes. La siguiente tabla presenta el costo por cada 100 g de algunos alimentos sugeridos ($A$), así
# como el porcentaje de macronutrientes (carbohidratos, proteínas y grasas) y la cantidad, en
# miligramos (mg), de vitaminas que contienen 100 g de dichos alimentos.

# 
# | ||Vitaminas (mg)|Carbohidratos (%)| Proteína (%)| Grasas (%)|Costo (\$) por cada 100g|
# |:-:|:-|-:|-:|-:|-:|-:|
# |**Frutas**|||||||
# ||Naranja|50.00|8.90|0.80|0.00|570.00|
# ||Manzana|5.00|10.50|0.30|0.00|650.00|
# ||Banano|35.00|20.80|1.20|0.30|200.00|
# ||Pera|12.00|11.70|0.40|0.10|550.00|
# |**Verduras**|||||||
# ||Brócoli|116.00|4.90|3.20|0.20|450.00|
# ||Espinaca|52.00|4.10|2.50|0.30|600.00|
# ||Guisantes|23.00|18.20|7.20|0.40|800.00|
# ||Pepino|9.00|0.70|0.15|2.70|500.00|
# ||Calabacín|21.00|7.30|4.20|0.10|450.00|
# |**Carnes**|||||||
# ||Pollo|61.00|1.00|23.00|2.00|1,420.00|
# ||Res|31.00|2.00|18.00|20.00|4,800.00|
# ||Cerdo|2.00|1.50|16.00|27.00|2,900.00|

# 
# El menú del almuerzo debe contener una cantidad mínima de cada uno de los cuatro
# macronutrientes mostrados en la tabla. Estas cantidades mínimas son: 100 mg de vitaminas, 25 g de carbohidratos, 17 g de proteínas y 5 g de grasas. El equipo técnico del hospital desea incluir un
# modelo de optimización en el sistema para planear el menú del almuerzo al menor costo posible.
# 
# ## Formulación
# **a.** Formule matemáticamente un modelo de optimización de forma general que represente la
# situación anterior. Defina clara y rigurosamente:  
# - Conjuntos
# - Parámetros
# - Variables de decisión
# - Función objetivo
# - Restricciones
# 

# ### Conjuntos 
# - $T$: conjunto de tipos de alimentos
# - $A$: conjunto de alimentos
# - $N$: conjunto de aspectos nutricionales
# 
# ### Parámetros 
# - $l_n$: contenido mínimo  del aspecto nutriconal $n\in N$ que debe tener el menú
# - $k_{an}$: cantidad del aspecto nutricional $n\in N$ que contiene el alimento $a\in A$
# - $c_a$: costo por porción (100g) del alimento $a\in A$
# - $p_{at}: \begin{cases}1&\text{, si el alimento }a\in A\text{ pertenece al tipo de alimento }t\in T\text{;} \\ 0 & \text{, d.l.c.}  \end{cases}$ 
# 
# 
# ### Variables de decisión 
# - $x_a$: cantidad de porciones (100g) del alimento $a\in A$ incluidas en el menú
# 
# ### Función Objetivo
# $$
# \text{minimizar}  \sum_{a\in A}c_a\cdot x_a \text{  (1)}
# $$
# ### Restricciones
# Sujeto a,
# \begin{align*}
# \sum_{a\in A|p_{at}=1}x_a&=1, &&\forall T\in T;   &(2)\\ 
# \sum_{a\in A}k_{an}\cdot x_a&\ge l_n, &&\forall n\in N;   &(3)\\
#  x_a&\ge 0,&&\forall a\in A;   &(4)
# \end{align*}

# La función objetivo (1) minimiza los costos totales. La restricción (2) garantiza que el menú tenga una porción (100g) de cada tipo de alimento $t \in T$. La restricción (3) garantiza que haya un mínimo $l_n$ de cada aspecto nutricional $n\in N$ en el menú. La restricción (4) describe la naturaleza de la variable $x_a$

# ## Implementación
# 
# **b.** Resuelva el modelo planteado utilizando la librería de PuLP en Python. ¿Cuál es la solución
# óptima del problema? 

# In[1]:


#%% se importa la libreria de PulP 
import pulp as lp

#-----------------
# Conjuntos
#-----------------

#Tipos de Alimentos
T=["Frutas",
   "Verduras",
   "Carnes"]

#Alimentos
A=["Naranja",
   "Manzana",
   "Banano",
   "Pera",
   "Brócoli",
   "Espinaca",
   "Guisantes",
   "Pepino",
   "Calabacín",
   "Pollo",
   "Res",
   "Cerdo"]

#Aspectos Nutricionales
N=["Vitaminas",
   "Carbohidratos",
   "Proteína",
   "Grasas"]


#-----------------
# Parámetros
#-----------------

#Contenido minimo del aspecto nutricional n que debe tener el menú
l={'Vitaminas': 100, 
   'Carbohidratos': 25, 
   'Proteína': 17, 
   'Grasas': 5}

#Cantidad del aspecto nutricional n que tiene el alimento a
#WATCH OUT: Algunos parámetros en la tabla son "porcentajes" por lo que toca dividirlos por cien para utilizarlos en el modelo y obtener resultados consistentes. 
k={('Naranja', 'Vitaminas'): 50,
   ('Naranja', 'Carbohidratos'): 8.9,
   ('Naranja', 'Proteína'): 0.8,
   ('Naranja', 'Grasas'): 0,
   ('Manzana', 'Vitaminas'): 5,
   ('Manzana', 'Carbohidratos'): 10.5,
   ('Manzana', 'Proteína'): 0.3,
   ('Manzana', 'Grasas'): 0,
   ('Banano', 'Vitaminas'): 35,
   ('Banano', 'Carbohidratos'): 20.8,
   ('Banano', 'Proteína'): 1.2,
   ('Banano', 'Grasas'): 0.3,
   ('Pera', 'Vitaminas'): 12,
   ('Pera', 'Carbohidratos'): 11.7,
   ('Pera', 'Proteína'): 0.4,
   ('Pera', 'Grasas'): 0.1,
   ('Brócoli', 'Vitaminas'): 116,
   ('Brócoli', 'Carbohidratos'): 4.9,
   ('Brócoli', 'Proteína'): 3.2,
   ('Brócoli', 'Grasas'): 0.2,
   ('Espinaca', 'Vitaminas'): 52,
   ('Espinaca', 'Carbohidratos'): 4.1,
   ('Espinaca', 'Proteína'): 2.5,
   ('Espinaca', 'Grasas'): 0.3,
   ('Guisantes', 'Vitaminas'): 23,
   ('Guisantes', 'Carbohidratos'): 18.2,
   ('Guisantes', 'Proteína'): 7.2,
   ('Guisantes', 'Grasas'): 0.4,
   ('Pepino', 'Vitaminas'): 9,
   ('Pepino', 'Carbohidratos'): 0.7,
   ('Pepino', 'Proteína'): 0.15,
   ('Pepino', 'Grasas'): 2.7,
   ('Calabacín', 'Vitaminas'): 21,
   ('Calabacín', 'Carbohidratos'): 7.3,
   ('Calabacín', 'Proteína'): 4.2,
   ('Calabacín', 'Grasas'): 0.1,
   ('Pollo', 'Vitaminas'): 61,
   ('Pollo', 'Carbohidratos'): 1,
   ('Pollo', 'Proteína'): 23,
   ('Pollo', 'Grasas'): 2,
   ('Res', 'Vitaminas'): 31,
   ('Res', 'Carbohidratos'): 2,
   ('Res', 'Proteína'): 18,
   ('Res', 'Grasas'): 20,
   ('Cerdo', 'Vitaminas'): 2,
   ('Cerdo', 'Carbohidratos'): 1.5,
   ('Cerdo', 'Proteína'): 16,
   ('Cerdo', 'Grasas'): 27}

#Costo por porción (100g) de alimento a
c={'Naranja': 570,
   'Manzana': 650,
   'Banano': 200,
   'Pera': 550,
   'Brócoli': 450,
   'Espinaca': 600,
   'Guisantes': 800,
   'Pepino': 500,
   'Calabacín': 450,
   'Pollo': 1420,
   'Res': 4800,
   'Cerdo': 2900}

#Si el alimento a pertenece al tipo de alimento t
p={('Naranja', 'Frutas'): 1,
   ('Naranja', 'Verduras'): 0,
   ('Naranja', 'Carnes'): 0,
   ('Manzana', 'Frutas'): 1,
   ('Manzana', 'Verduras'): 0,
   ('Manzana', 'Carnes'): 0,
   ('Banano', 'Frutas'): 1,
   ('Banano', 'Verduras'): 0,
   ('Banano', 'Carnes'): 0,
   ('Pera', 'Frutas'): 1,
   ('Pera', 'Verduras'): 0,
   ('Pera', 'Carnes'): 0,
   ('Brócoli', 'Frutas'): 0,
   ('Brócoli', 'Verduras'): 1,
   ('Brócoli', 'Carnes'): 0,
   ('Espinaca', 'Frutas'): 0,
   ('Espinaca', 'Verduras'): 1,
   ('Espinaca', 'Carnes'): 0,
   ('Guisantes', 'Frutas'): 0,
   ('Guisantes', 'Verduras'): 1,
   ('Guisantes', 'Carnes'): 0,
   ('Pepino', 'Frutas'): 0,
   ('Pepino', 'Verduras'): 1,
   ('Pepino', 'Carnes'): 0,
   ('Calabacín', 'Frutas'): 0,
   ('Calabacín', 'Verduras'): 1,
   ('Calabacín', 'Carnes'): 0,
   ('Pollo', 'Frutas'): 0,
   ('Pollo', 'Verduras'): 0,
   ('Pollo', 'Carnes'): 1,
   ('Res', 'Frutas'): 0,
   ('Res', 'Verduras'): 0,
   ('Res', 'Carnes'): 1,
   ('Cerdo', 'Frutas'): 0,
   ('Cerdo', 'Verduras'): 0,
   ('Cerdo', 'Carnes'): 1}

#%%
#-------------------------------------
# Creación del objeto problema en PuLP
#-------------------------------------
#Crea el problema para cargarlo con la instancia 
problema=lp.LpProblem("PlaneaciónMenús",lp.LpMinimize)

#-----------------------------
# Variables de Decisión
#-----------------------------
x=lp.LpVariable.dicts('x',A,lowBound=0,cat='Continuous') #Cantidad de porciones del alimento a incluidas en el menú

#-----------------------------
# Función objetivo
#-----------------------------
#Crea la expresión de minimización de costos
problema+=lp.lpSum(c[a]*x[a] for a in A)

#-----------------------------
# Restricciones
#-----------------------------
#Se garantizan 100 gramos por cada tipo de alimento
for t in T:
    problema+=lp.lpSum(x[a] for a in A if p[a,t]==1)==1, "100 gramos del tipo de alimento " + t
    
#Se garantiza el requerimiento mínimo de cada aspecto nutricional
for n in N:
    problema+=lp.lpSum(k[a,n]*x[a] for a in A)>=l[n], "Mínimo aspecto nutricional " + n

#-----------------------------
# Invocar el optimizador
#-----------------------------
#Optimizar el modelo con CBC (default de PuLP)
problema.solve()

#%%
#-----------------------------
# Imprimir formato LP
#-----------------------------
#Escribe el problema en un archivo con formato LP 
problema.writeLP("PlaneaciónMenús.lp")

#-----------------------------
#    Imprimir resultados
#-----------------------------
#Imprimir estado final del optimizador
print("Estado (optimizador):", lp.LpStatus[problema.status],end='\n')

#Valor óptimo del costo del menú  
print("\nPlaneación Menús - Costos Totales = $", round(lp.value(problema.objective),2))

#Imprimir variables de decisión
print("Variables de decisión\n")
for t in T:
    print(t)
    for a in A:
        if p[a,t]==1:
            print("\t",a,":",round(x[a].value()*100,1),"gramos")


# <div style="text-align:justify"><strong>c.</strong> Varios aspectos prácticos no fueron tenidos en cuenta en el modelo planteado
# anteriormente. Algunos de estos aspectos son: la inclusión de alimentos de los otros cuatro
# grupos alimenticios, la planeación de menús para desayunos, almuerzos y cenas; la
# planeación de menús para que los pacientes reciban menús variados de comida a lo largo
# de la semana; y menús especiales para pacientes con ciertas restricciones, entre otros.
# Discuta en detalle cómo podría tener en cuenta estos aspectos dentro de un modelo de
# optimización en el sistema de planeación del hospital.
# </div>

# ## Créditos
# 
# Desarrollador: Camilo Aguilar León<br>
# Fecha: 08/09/2020
