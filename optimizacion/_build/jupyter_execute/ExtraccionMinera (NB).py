<div style="background-color: RGB(0,0,30); color: white">
    
<br>
<br>
    
<h1 style="text-align:center">IIND 2103 Principios de Optimización</h1>

<br>


<h3 style='text-align: right;'> Departamento de Ingeniería Industrial &emsp;<br> Facultad de Ingeniería &emsp; <br>
     Universidad de los Andes &emsp; <br>
</h3>

<br>
</div>

## Práctica de formulación: Extracción minera

### Punto 1

<div style="text-align:justify">
La minería de cielo abierto es una actividad industrial que consiste en remover grandes cantidades de suelo para extraer el mineral deseado. Este tipo de minas son comunes en la extracción de materiales como: arena, arcilla, cobre y carbón. Las directivas de una empresa de extracción minera desean explotar un conjunto de zonas ($M$), de las cuales se puede extraer un conjunto de diferentes tipos de carbón ($K$). Se sabe que de la zona $i\in M$ sólo puede extraerse el carbón tipo $j\in K$. Para ello, suponga que $a_{ij}$ es un parámetro binario que toma el valor de 1 si en la zona $i\in M$ se puede extraer carbón del tipo $j\in K$ y 0 en el caso contrario. La Figura 1 presenta un ejemplo en el cual hay 36 zonas y 4 tipos de carbón. Por ejemplo, para la zona uno se tiene que $a_{11}=0$, $a_{12}=1$, $a_{13}=0$ y $a_{14}=0$ ya que de la zona 1 sólo puede extraerse el tipo de carbón 2 (hulla). 

*Figura 1:*
<table>
  <tr id="ROW1">
	<td style="text-align:center; background-color: lightblue">1</td>
	<td style="text-align:center; background-color: lightblue">2</td>
	<td style="text-align:center; background-color: green">3</td>
    <td style="text-align:center; background-color: green">4</td> 
    <td style="text-align:center; background-color: lightblue">5</td>
    <td style="text-align:center; background-color: green">6</td>
  </tr>
  <tr id="ROW2">
	<td style="text-align:center; background-color: lightblue">7</td>
	<td style="text-align:center; background-color: lightblue">8</td>
	<td style="text-align:center; background-color: purple">9</td>
    <td style="text-align:center; background-color: purple">10</td> 
    <td style="text-align:center; background-color: lightblue">11</td>
    <td style="text-align:center; background-color: green">12</td>
  </tr>
  <tr id="ROW3">
	<td style="text-align:center; background-color: purple">13</td>
	<td style="text-align:center; background-color: green">14</td>
	<td style="text-align:center; background-color: green">15</td>
    <td style="text-align:center; background-color: lightblue">16</td> 
    <td style="text-align:center; background-color: lightblue">17</td>
    <td style="text-align:center; background-color: green">18</td>
  </tr>
  <tr id="ROW4">
	<td style="text-align:center; background-color: purple">19</td>
	<td style="text-align:center; background-color: red">20</td>
	<td style="text-align:center; background-color: green">21</td>
    <td style="text-align:center; background-color: purple">22</td> 
    <td style="text-align:center; background-color: purple">23</td>
    <td style="text-align:center; background-color: purple">24</td>
  </tr>
  <tr id="ROW5">
	<td style="text-align:center; background-color: purple">25</td>
	<td style="text-align:center; background-color: green">26</td>
	<td style="text-align:center; background-color: green">27</td>
    <td style="text-align:center; background-color: red">28</td> 
    <td style="text-align:center; background-color: red">29</td>
    <td style="text-align:center; background-color: red">30</td>
  </tr>
  <tr id="ROW6">
	<td style="text-align:center; background-color: lightblue">31</td>
	<td style="text-align:center; background-color: green">32</td>
	<td style="text-align:center; background-color: lightblue">33</td>
    <td style="text-align:center; background-color: purple">34</td> 
    <td style="text-align:center; background-color: red">35</td>
    <td style="text-align:center; background-color: purple">36</td>
  </tr>
</table>
<table>
  <tr id="ROW1">
	<td style="text-align:center; background-color: purple">Antracita</td>
	<td style="text-align:center; background-color: lightblue">Hulla</td>
	<td style="text-align:center; background-color: green">Turba</td>
    <td style="text-align:center; background-color: red">Lignito</td> 
  </tr>

<div style="text-align:justify">
Cada tonelada de carbón extraída de la zona $i\in M$ le cuesta a la empresa $c_i$ pesos.  Adicionalmente, cada zona tiene una capacidad máxima de extracción de carbón de $n_i$ toneladas. Suponga que las directivas desean explotar un mínimo de $b_j$ toneladas de cada tipo de carbón $j\in K$.    
<br> 
<br> 
<div style="text-align:justify">
Usted debe formular un programa lineal que le permita a la empresa decidir cuánto deben extraer en cada zona de manera que se cumplan los requerimientos a un mínimo costo. Para esto usted debe seguir los siguientes pasos: 

**a.** Describa la(s) variable(s) de decisión que utilizará en el modelo. 

\begin{align}
x_i: \text{cantidad de carbón extraído en la zona $i\in M$ (en toneladas)}\\
\end{align}

**b.** Escriba la(s) restricción(es) lineal(es) que describe(n) la cantidad de carbón extraído del tipo $j\in K$, debe como mínimo $b_j$.    

*Opción 1:*
\begin{align}
\sum_{i\in M}a_{ij}x_i &\ge b_j, &&\forall j\in K.\\
\end{align}

*Opción 2:*
\begin{align}
\sum_{i\in M|a_{ij}=1}x_i &\ge b_j, &&\forall j\in K.\\
\end{align}

**c.** Escriba la(s) restricción(es) lineal(es) que describe(n) que no se pueden extraer más de ($n_i$) toneladas de carbón en la zona $i\in M$.   

\begin{align}
x_i &\le n_i, &&\forall i\in M.
\end{align}

**d.** EEscriba la(s) restricción(es) que describe(n) la naturaleza de la(s) variable(s) incluida(s) en el modelo. 

\begin{align}
x_i &\ge 0, &&\forall i\in M.
\end{align}

**e.** Escriba la función objetivo.

$$
\text{minimizar }  \sum_{i\in M}x_ic_i 
$$

### Formulación matemática completa punto 1

#### Conjuntos:
- $M$: Zonas
- $K$: Tipos de carbón

#### Parámetros:
- $a_{ij}:\begin{cases}1&\text{, si en la zona $i\in M$ se puede extraer carbón del tipo $j\in K$} \\ 0 & \text{, d.l.c}  \end{cases}$
- $c_i$: costo por cada tonelada de carbón extraída en la zona $i\in M$  
- $n_i$: capacidad máxima de extracción de carbón (en toneladas) en la zona $i\in M$
- $b_j$: mínimo de toneladas a explotar del tipo de carbón $j\in K$

#### Variables de decisión:
- $x_i$: toneladas de carbón extraído en la zona $i\in M$  

#### Modelo:

$$
\text{minimizar }  \sum_{i\in M}x_ic_i \text{ (1)} 
$$

Sujeto a,
\begin{align}
\sum_{i\in M}a_{ij}x_i &\ge b_j, &&\forall j\in K; &(2)\\
x_i &\le n_i, &&\forall i\in M; &(3)\\
x_i &\ge 0, &&\forall i\in M. &(4)
\end{align}

<div style="text-align:justify">
La función objetivo (1) minimiza los costos totales. La restricción (2) describe que la cantidad de carbón extraído del tipo $j\in K$ debe ser mínimo $b_j$ toneladas. La restricción (3) describe que no se pueden extraer más de ($n_i$) toneladas de carbón en la zona $i\in M$. La restricción (4) describe la naturaleza de la variable $x_i$. 

**g.** Resuelva el modelo planteado utilizando la librería de PulP en Python. ¿Cuál es la solución
óptima del problema? 

#se importa la libreria de PulP
from pulp import *

#-----------------
# Conjuntos
#-----------------
#Zonas
M=[]
for i in range(1,37):
    M.append(i)

#Tipos de carbón
K=["Antracita",
   "Hulla",
   "Turba",
   "Lignito"]

#-----------------
# Parámetros
#-----------------
a={#(zona, tipo de carbón): 1 si en la zona i se puede extraer carbón del tipo j, 0 d.l.c.
    (1,"Antracita"):0,
    (1,"Hulla"):1,
    (1,"Turba"):0,
    (1,"Lignito"):0,
    (2,"Antracita"):0,
    (2,"Hulla"):1,
    (2,"Turba"):0,
    (2,"Lignito"):0,
    (3,"Antracita"):0,
    (3,"Hulla"):0,
    (3,"Turba"):1,
    (3,"Lignito"):0,
    (4,"Antracita"):0,
    (4,"Hulla"):0,
    (4,"Turba"):1,
    (4,"Lignito"):0,
    (5,"Antracita"):0,
    (5,"Hulla"):1,
    (5,"Turba"):0,
    (5,"Lignito"):0,
    (6,"Antracita"):0,
    (6,"Hulla"):0,
    (6,"Turba"):1,
    (6,"Lignito"):0,
    (7,"Antracita"):0,
    (7,"Hulla"):1,
    (7,"Turba"):0,
    (7,"Lignito"):0,
    (8,"Antracita"):0,
    (8,"Hulla"):1,
    (8,"Turba"):0,
    (8,"Lignito"):0,
    (9,"Antracita"):1,
    (9,"Hulla"):0,
    (9,"Turba"):0,
    (9,"Lignito"):0,
    (10,"Antracita"):1,
    (10,"Hulla"):0,
    (10,"Turba"):0,
    (10,"Lignito"):0,
    (11,"Antracita"):0,
    (11,"Hulla"):1,
    (11,"Turba"):0,
    (11,"Lignito"):0,
    (12,"Antracita"):0,
    (12,"Hulla"):0,
    (12,"Turba"):1,
    (12,"Lignito"):0,
    (13,"Antracita"):1,
    (13,"Hulla"):0,
    (13,"Turba"):0,
    (13,"Lignito"):0,
    (14,"Antracita"):0,
    (14,"Hulla"):0,
    (14,"Turba"):1,
    (14,"Lignito"):0,
    (15,"Antracita"):0,
    (15,"Hulla"):0,
    (15,"Turba"):1,
    (15,"Lignito"):0,
    (16,"Antracita"):0,
    (16,"Hulla"):1,
    (16,"Turba"):0,
    (16,"Lignito"):0,
    (17,"Antracita"):0,
    (17,"Hulla"):1,
    (17,"Turba"):0,
    (17,"Lignito"):0,
    (18,"Antracita"):0,
    (18,"Hulla"):0,
    (18,"Turba"):1,
    (18,"Lignito"):0,
    (19,"Antracita"):1,
    (19,"Hulla"):0,
    (19,"Turba"):0,
    (19,"Lignito"):0,
    (20,"Antracita"):0,
    (20,"Hulla"):0,
    (20,"Turba"):0,
    (20,"Lignito"):1,
    (21,"Antracita"):0,
    (21,"Hulla"):0,
    (21,"Turba"):1,
    (21,"Lignito"):0,
    (22,"Antracita"):1,
    (22,"Hulla"):0,
    (22,"Turba"):0,
    (22,"Lignito"):0,
    (23,"Antracita"):1,
    (23,"Hulla"):0,
    (23,"Turba"):0,
    (23,"Lignito"):0,
    (24,"Antracita"):1,
    (24,"Hulla"):0,
    (24,"Turba"):0,
    (24,"Lignito"):0,
    (25,"Antracita"):1,
    (25,"Hulla"):0,
    (25,"Turba"):0,
    (25,"Lignito"):0,
    (26,"Antracita"):0,
    (26,"Hulla"):0,
    (26,"Turba"):1,
    (26,"Lignito"):0,
    (27,"Antracita"):0,
    (27,"Hulla"):0,
    (27,"Turba"):1,
    (27,"Lignito"):0,
    (28,"Antracita"):0,
    (28,"Hulla"):0,
    (28,"Turba"):0,
    (28,"Lignito"):1,
    (29,"Antracita"):0,
    (29,"Hulla"):0,
    (29,"Turba"):0,
    (29,"Lignito"):1,
    (30,"Antracita"):0,
    (30,"Hulla"):0,
    (30,"Turba"):0,
    (30,"Lignito"):1,
    (31,"Antracita"):0,
    (31,"Hulla"):1,
    (31,"Turba"):0,
    (31,"Lignito"):0,
    (32,"Antracita"):0,
    (32,"Hulla"):0,
    (32,"Turba"):1,
    (32,"Lignito"):0,
    (33,"Antracita"):0,
    (33,"Hulla"):1,
    (33,"Turba"):0,
    (33,"Lignito"):0,
    (34,"Antracita"):1,
    (34,"Hulla"):0,
    (34,"Turba"):0,
    (34,"Lignito"):0,
    (35,"Antracita"):0,
    (35,"Hulla"):0,
    (35,"Turba"):0,
    (35,"Lignito"):1,
    (36,"Antracita"):1,
    (36,"Hulla"):0,
    (36,"Turba"):0,
    (36,"Lignito"):0} 

c={#zona: costo por cada tonelada de carbón extraída en la zona i
    (1):6,
    (2):23,
    (3):20,
    (4):13,
    (5):26,
    (6):13,
    (7):29,
    (8):19,
    (9):14,
    (10):27,
    (11):27,
    (12):19,
    (13):16,
    (14):23,
    (15):22,
    (16):5,
    (17):25,
    (18):5,
    (19):26,
    (20):15,
    (21):28,
    (22):15,
    (23):12,
    (24):15,
    (25):16,
    (26):19,
    (27):13,
    (28):9,
    (29):16,
    (30):22,
    (31):24,
    (32):10,
    (33):21,
    (34):18,
    (35):10,
    (36):23}  

n={#zona: capacidad máxima de extracción de carbón (en toneladas) en la zona i
    (1):149,
    (2):176,
    (3):190,
    (4):134,
    (5):174,
    (6):197,
    (7):113,
    (8):161,
    (9):135,
    (10):159,
    (11):173,
    (12):114,
    (13):170,
    (14):183,
    (15):133,
    (16):190,
    (17):163,
    (18):126,
    (19):187,
    (20):105,
    (21):121,
    (22):126,
    (23):167,
    (24):194,
    (25):160,
    (26):128,
    (27):132,
    (28):172,
    (29):165,
    (30):186,
    (31):146,
    (32):175,
    (33):115,
    (34):157,
    (35):168,
    (36):108} 

b={#mínimo de toneladas a explotar del tipo de carbón j
    ("Antracita"):862,
    ("Hulla"):898,
    ("Turba"):562,
    ("Lignito"):742}  


#-------------------------------------
# Creación del objeto problema en PuLP
#-------------------------------------
#Crea el problema para cargarlo con la instancia 
problema=LpProblem("Extracción Minera",LpMinimize)

#-----------------------------
# Variables de Decisión
#-----------------------------
x=LpVariable.dicts('x',M,lowBound=0,cat='Continuous') #toneladas de carbón extraído de la zona i; aca se añade de una vez la naturaleza de las variables

#-----------------------------
# Función objetivo
#-----------------------------
#Crea la expresión de minimización de costos
problema+=lpSum(x[i]*c[i] for i in M), "Costos Totales"

#-----------------------------
# Restricciones
#-----------------------------
#sum(i in M)a_ij*x_i >= b_j forall j in K
for j in K:
    problema+= lpSum(a[i,j]*x[i] for i in M) >= b[j], "Mínimo toneladas de extracción del tipo de carbón "+j #se garantiza el mínimo de toneladas extraidas del tipo de carbón j

#x_i <= n_i*y_i forall i in M
for i in M:
    problema+= x[i] <= n[i], "Máximo toneladas de extracción de la zona "+str(i)   #se garantiza el máximo de toneladas de carbón que se pueden extraer de la zona i

#-----------------------------
# Imprimir formato LP
#-----------------------------
#Escribe el problema en un archivo con formato LP 
problema.writeLP("ExtraccionMinera.lp")

#-----------------------------
# Invocar el optimizador
#-----------------------------
#Optimizar el modelo con CBC (default de PuLP)
problema.solve()

#-----------------------------
#    Imprimir resultados
#-----------------------------
#Imprimir estado final del optimizador
print("Estado (optimizador):", LpStatus[problema.status],end='\n')

#Valor óptimo del portafolio de Petroco    
print("\nExtracción Minera - Costos totales = $", round(value(problema.objective),2))
print()

#Imprimir variables de decisión
print("Extracción de las zonas")
print(" ","Antracita", "Hulla", "Turba", "Lignito",sep='\t')
for i in M:
    print(i,round(x[i].value(),0),round(x[i].value(),0),round(x[i].value(),0),round(x[i].value(),0),sep='\t')




### Punto 2

<div style="text-align:justify">
Ahora considere el escenario en que la empresa incurre en un costo fijo de $q_i$ pesos cuando decide extraer carbón de la zona $i\in M$. Por lo tanto, si se decide explotar la mina $i\in M$, no se pueden extraer más de ($n_i$) toneladas de carbón. Pero si no se decide explotar, la extracción de carbón en esa zona debe ser igual a cero (0). Para esto usted debe seguir los siguientes pasos: 

**a.** Describa la(s) variable(s) de decisión adicional(es) que utilizará en el modelo. 

\begin{align}
y_i:\begin{cases}1&\text{, si se decide explotar la zona $i\in M$} \\ 0 & \text{, d.l.c}  \end{cases}
\end{align}

**b.** Escriba la(s) restricción(es) lineal(es) que describe(n) que si se decide explotar la mina $i\in M$, no se pueden extraer más de ($n_i$) toneladas de carbón. Pero que, si no se decide explotar, la extracción de carbón debe ser igual a cero.    

\begin{align}
x_i &\le n_iy_i, &&\forall i\in M.
\end{align}

**c.** Escriba la(s) restricción(es) que describe(n) la naturaleza de la(s) variable(s) adicional(es).

\begin{align}
y_i &\in \text{{0,1}}, &&\forall i\in M.
\end{align}

**e.** Escriba la función objetivo.

$$
\text{minimizar }  \sum_{i\in M}y_iq_i+\sum_{i\in M}x_ic_i
$$

### Formulación matemática completa punto 2

#### Conjuntos:
- $M$: Zonas
- $K$: Tipos de carbón

#### Parámetros:
- $a_{ij}:\begin{cases}1&\text{, si en la zona $i\in M$ se puede extraer carbón del tipo $j\in K$} \\ 0 & \text{, d.l.c}  \end{cases}$
- $c_i$: costo por cada tonelada de carbón extraída en la zona $i\in M$  
- $n_i$: capacidad máxima de extracción de carbón (en toneladas) en la zona $i\in M$
- $b_j$: mínimo de toneladas a explotar del tipo de carbón $j\in K$
- $q_i$: costo fijo si se decide extraer carbón de la zona $i\in M$

#### Variables de decisión:
- $x_i$: toneladas de carbón extraído en la zona $i\in M$ 
- $y_i:\begin{cases}1&\text{, si se decide explotar la zona $i\in M$} \\ 0 & \text{, d.l.c}  \end{cases}$ 

#### Modelo:

$$
\text{minimizar }  \sum_{i\in M}y_iq_i+\sum_{i\in M}x_ic_i \text{ (1)} 
$$

Sujeto a,
\begin{align}
\sum_{i\in M|a_{ij}=1}x_i &\ge b_j, &&\forall j\in K; &(2)\\
x_i &\le n_iy_i, &&\forall i\in M; &(3)\\
x_i &\ge 0, &&\forall i\in M; &(4)\\
y_i &\in \text{{0,1}}, &&\forall i\in M. &(5)
\end{align}

<div style="text-align:justify">
La función objetivo (1) minimiza los costos totales. La restricción (2) describe que la cantidad de carbón extraído del tipo $j\in K$ debe ser mínimo $b_j$ toneladas. La restricción (3) describe que si se decide explotar la mina $i\in M$, no se pueden extraer más de ($n_i$) toneladas de carbón, pero que si no se decide explotar, la extracción de carbón debe ser igual a cero. Las restricciones (4) y (5) describen la naturaleza de las variables $x_i$ y $y_i$. 

**f.** Resuelva el modelo planteado utilizando la librería de PulP en Python. ¿Cuál es la solución
óptima del problema? 

#se importa la libreria de PulP
from pulp import *

#-----------------
# Conjuntos
#-----------------
#Zonas
M=[]
for i in range(1,37):
    M.append(i)

#Tipos de carbón
K=["Antracita",
   "Hulla",
   "Turba",
   "Lignito"]

#-----------------
# Parámetros
#-----------------
a={#(zona, tipo de carbón): 1 si en la zona i se puede extraer carbón del tipo j, 0 d.l.c.
    (1,"Antracita"):0,
    (1,"Hulla"):1,
    (1,"Turba"):0,
    (1,"Lignito"):0,
    (2,"Antracita"):0,
    (2,"Hulla"):1,
    (2,"Turba"):0,
    (2,"Lignito"):0,
    (3,"Antracita"):0,
    (3,"Hulla"):0,
    (3,"Turba"):1,
    (3,"Lignito"):0,
    (4,"Antracita"):0,
    (4,"Hulla"):0,
    (4,"Turba"):1,
    (4,"Lignito"):0,
    (5,"Antracita"):0,
    (5,"Hulla"):1,
    (5,"Turba"):0,
    (5,"Lignito"):0,
    (6,"Antracita"):0,
    (6,"Hulla"):0,
    (6,"Turba"):1,
    (6,"Lignito"):0,
    (7,"Antracita"):0,
    (7,"Hulla"):1,
    (7,"Turba"):0,
    (7,"Lignito"):0,
    (8,"Antracita"):0,
    (8,"Hulla"):1,
    (8,"Turba"):0,
    (8,"Lignito"):0,
    (9,"Antracita"):1,
    (9,"Hulla"):0,
    (9,"Turba"):0,
    (9,"Lignito"):0,
    (10,"Antracita"):1,
    (10,"Hulla"):0,
    (10,"Turba"):0,
    (10,"Lignito"):0,
    (11,"Antracita"):0,
    (11,"Hulla"):1,
    (11,"Turba"):0,
    (11,"Lignito"):0,
    (12,"Antracita"):0,
    (12,"Hulla"):0,
    (12,"Turba"):1,
    (12,"Lignito"):0,
    (13,"Antracita"):1,
    (13,"Hulla"):0,
    (13,"Turba"):0,
    (13,"Lignito"):0,
    (14,"Antracita"):0,
    (14,"Hulla"):0,
    (14,"Turba"):1,
    (14,"Lignito"):0,
    (15,"Antracita"):0,
    (15,"Hulla"):0,
    (15,"Turba"):1,
    (15,"Lignito"):0,
    (16,"Antracita"):0,
    (16,"Hulla"):1,
    (16,"Turba"):0,
    (16,"Lignito"):0,
    (17,"Antracita"):0,
    (17,"Hulla"):1,
    (17,"Turba"):0,
    (17,"Lignito"):0,
    (18,"Antracita"):0,
    (18,"Hulla"):0,
    (18,"Turba"):1,
    (18,"Lignito"):0,
    (19,"Antracita"):1,
    (19,"Hulla"):0,
    (19,"Turba"):0,
    (19,"Lignito"):0,
    (20,"Antracita"):0,
    (20,"Hulla"):0,
    (20,"Turba"):0,
    (20,"Lignito"):1,
    (21,"Antracita"):0,
    (21,"Hulla"):0,
    (21,"Turba"):1,
    (21,"Lignito"):0,
    (22,"Antracita"):1,
    (22,"Hulla"):0,
    (22,"Turba"):0,
    (22,"Lignito"):0,
    (23,"Antracita"):1,
    (23,"Hulla"):0,
    (23,"Turba"):0,
    (23,"Lignito"):0,
    (24,"Antracita"):1,
    (24,"Hulla"):0,
    (24,"Turba"):0,
    (24,"Lignito"):0,
    (25,"Antracita"):1,
    (25,"Hulla"):0,
    (25,"Turba"):0,
    (25,"Lignito"):0,
    (26,"Antracita"):0,
    (26,"Hulla"):0,
    (26,"Turba"):1,
    (26,"Lignito"):0,
    (27,"Antracita"):0,
    (27,"Hulla"):0,
    (27,"Turba"):1,
    (27,"Lignito"):0,
    (28,"Antracita"):0,
    (28,"Hulla"):0,
    (28,"Turba"):0,
    (28,"Lignito"):1,
    (29,"Antracita"):0,
    (29,"Hulla"):0,
    (29,"Turba"):0,
    (29,"Lignito"):1,
    (30,"Antracita"):0,
    (30,"Hulla"):0,
    (30,"Turba"):0,
    (30,"Lignito"):1,
    (31,"Antracita"):0,
    (31,"Hulla"):1,
    (31,"Turba"):0,
    (31,"Lignito"):0,
    (32,"Antracita"):0,
    (32,"Hulla"):0,
    (32,"Turba"):1,
    (32,"Lignito"):0,
    (33,"Antracita"):0,
    (33,"Hulla"):1,
    (33,"Turba"):0,
    (33,"Lignito"):0,
    (34,"Antracita"):1,
    (34,"Hulla"):0,
    (34,"Turba"):0,
    (34,"Lignito"):0,
    (35,"Antracita"):0,
    (35,"Hulla"):0,
    (35,"Turba"):0,
    (35,"Lignito"):1,
    (36,"Antracita"):1,
    (36,"Hulla"):0,
    (36,"Turba"):0,
    (36,"Lignito"):0} 

q={#zona: costo fijo si se decide extraer carbón de la zona i 
    (1):429,
    (2):409,
    (3):290,
    (4):404,
    (5):357,
    (6):264,
    (7):159,
    (8):409,
    (9):388,
    (10):356,
    (11):447,
    (12):152,
    (13):443,
    (14):407,
    (15):163,
    (16):237,
    (17):176,
    (18):174,
    (19):182,
    (20):161,
    (21):485,
    (22):329,
    (23):352,
    (24):417,
    (25):337,
    (26):438,
    (27):226,
    (28):366,
    (29):485,
    (30):395,
    (31):108,
    (32):468,
    (33):291,
    (34):458,
    (35):228,
    (36):157} 

c={#zona: costo por cada tonelada de carbón extraída en la zona i
    (1):6,
    (2):23,
    (3):20,
    (4):13,
    (5):26,
    (6):13,
    (7):29,
    (8):19,
    (9):14,
    (10):27,
    (11):27,
    (12):19,
    (13):16,
    (14):23,
    (15):22,
    (16):5,
    (17):25,
    (18):5,
    (19):26,
    (20):15,
    (21):28,
    (22):15,
    (23):12,
    (24):15,
    (25):16,
    (26):19,
    (27):13,
    (28):9,
    (29):16,
    (30):22,
    (31):24,
    (32):10,
    (33):21,
    (34):18,
    (35):10,
    (36):23}  

n={#zona: capacidad máxima de extracción de carbón (en toneladas) en la zona i
    (1):149,
    (2):176,
    (3):190,
    (4):134,
    (5):174,
    (6):197,
    (7):113,
    (8):161,
    (9):135,
    (10):159,
    (11):173,
    (12):114,
    (13):170,
    (14):183,
    (15):133,
    (16):190,
    (17):163,
    (18):126,
    (19):187,
    (20):105,
    (21):121,
    (22):126,
    (23):167,
    (24):194,
    (25):160,
    (26):128,
    (27):132,
    (28):172,
    (29):165,
    (30):186,
    (31):146,
    (32):175,
    (33):115,
    (34):157,
    (35):168,
    (36):108} 

b={#mínimo de toneladas a explotar del tipo de carbón j
    ("Antracita"):862,
    ("Hulla"):898,
    ("Turba"):562,
    ("Lignito"):742} 



#-------------------------------------
# Creación del objeto problema en PuLP
#-------------------------------------
#Crea el problema para cargarlo con la instancia 
problema=LpProblem("Extracción Minera",LpMinimize)

#-----------------------------
# Variables de Decisión
#-----------------------------
x=LpVariable.dicts('x',M,lowBound=0,cat='Continuous') #toneladas de carbón extraído de la zona i; aca se añade de una vez la naturaleza de las variables
y=LpVariable.dicts('y',M,cat='Binary') #1 si se decide explotar la zona i, 0 d.l.c. ; aca se añade de una vez la naturaleza 

#-----------------------------
# Función objetivo
#-----------------------------
#Crea la expresión de minimización de costos
problema+=lpSum(x[i]*c[i]+y[i]*q[i] for i in M), "Costos Totales"

#-----------------------------
# Restricciones
#-----------------------------
#sum(i in M |a_ij=1)x_i >= b_j forall j in K
for j in K:
    problema+= lpSum(x[i] for i in M if a[i,j]==1) >= b[j], "Mínimo toneladas de extracción del tipo de carbón "+j #se garantiza el mínimo de toneladas extraidas del tipo de carbón j

#x_i <= n_i*y_i forall i in M
for i in M:
    problema+= x[i] <= n[i]*y[i], "Maximo toneladas de extracción si se decide explotar la zona "+str(i)   #se garantiza el máximo de toneladas de carbón que se pueden extraer si se decide explotar la zona i

#-----------------------------
# Imprimir formato LP
#-----------------------------
#Escribe el problema en un archivo con formato LP 
problema.writeLP("ExtraccionMinera.lp")

#-----------------------------
# Invocar el optimizador
#-----------------------------
#Optimizar el modelo con CBC (default de PuLP)
problema.solve()

#-----------------------------
#    Imprimir resultados
#-----------------------------
#Imprimir estado final del optimizador
print("Estado (optimizador):", LpStatus[problema.status],end='\n')

#Valor óptimo del portafolio de Petroco    
print("\nExtracción Minera - Costos totales = $", round(value(problema.objective),2))
print()

ySol={i:y[i].value() for i in M if y[i].value()>0}
print(len(ySol))

#Imprimir variables de decisión
print("Extracción de las zonas")
print(" ","Antracita", "Hulla", "Turba", "Lignito",sep='\t')
for i in M:
    print(i,round(x[i].value(),2),round(x[i].value(),2),round(x[i].value(),2),round(x[i].value(),2),sep='\t')




###### Créditos

Desarrollo: Juan Felipe Rengifo M<br>
Fecha: 12/09/2020