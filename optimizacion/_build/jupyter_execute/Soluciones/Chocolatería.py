# Chocolatería Solución

## Enunciado

La chocolatería Perla Caribe es un pequeño emprendimiento que fabrica y comercializa chocolates artesanales con cacao de distintas variedades comprado directamente a agricultores locales. Actualmente producen dos tipos de chocolates: chocolate oscuro y chocolate blanco. Una unidad de cualquier tipo de chocolate pesa 60g. Una unidad de chocolate oscuro se vende a 7,000 COP y una unidad de chocolate blanco se vende a 6,000 COP. Los costos asociados a materia prima, mano de obra y demás costos operacionales equivalen a 3,500 COP por cada unidad de chocolate oscuro y 2,000 COP por cada unidad de chocolate blanco. 

La producción de estos chocolates requiere de dos ingredientes en común: manteca de cacao y azúcar. Por cada unidad de chocolate oscuro se requiere 6g de manteca de cacao y 21 g de azúcar. Por cada unidad de chocolate blanco se requiere 22g de manteca de cacao y 18g de azúcar. Cada semana, la chocolatería Perla Caribe tiene disponible 12kg de manteca de cacao y 20kg de azúcar. La demanda de chocolate oscuro es ilimitada, pero a lo sumo le demandan 315 unidades de chocolate blanco por semana.

La chocolatería Perla Caribe quiere maximizar su utilidad (ingresos menos costos). Formule un modelo matemático que represente la situación y que les permita cumplir con su objetivo. 

## Formulación

**a.** Escriba término a término la(s) variable(s) de decisión que utilizará en el modelo. 

\begin{align*}
x_1: \text{unidades de chocolate oscuro producidos cada semana} \\
x_2: \text{unidades de chocolate blanco producidos cada semana}
\end{align*}


**b.** Escriba término a término la(s) restricción(es) lineal(es) y descríbala(s)

Restricciones asociadas a la disponibilidad de recursos: 

\begin{align*}
6x_1 + 22x_2 \leq 12,000\\
21x_1 + 18x_2 \leq 20,000
\end{align*}

Restricciones asociadas a la demanda de productos: 

\begin{align*}
x_1 \leq 10,000
\end{align*}

Restricciones asociadas a tipo de variables: 

\begin{align*}
x_1 \geq 0\\
x_2 \geq 0
\end{align*}

**c.** Escriba término a término la función objetivo que maximiza la utilidad.

$$
\text{maximizar }  (\$7,000 - \$3,500)x_1 + (\$6,000-\$2,000)x_2
$$

## Formulación matemática

**Variables de decisión:**

- $x_1$: unidades de chocolate oscuro producidos cada semana
- $x_2$: unidades de chocolate blanco producidos cada semana


**Modelo:**

$$
\text{maximizar }  \$3,500x_1 + \$4,000x_2 \text{ (1)} 
$$

Sujeto a,
\begin{align*}
6x_1 + 22x_2 &\leq 12,000; &(2)\\
21x_1 + 18x_2 &\leq 20,000; &(3)\\
x_2 &\leq 10,000; &(4)\\
x_1 &\geq 0; &(5)\\
x_2 & \geq 0. &(6)
\end{align*}

La función objetivo (1) maximiza las utilidades. Las restricciones (2) y (3) describen que se debe respetar la disponibilidad de manteca de cacao y azúcar, respectivamente. La restricción (4) garantiza no se sobrepase la demanda máxima de chocolate blanco. La restricciones (5) y (6) describen la naturaleza de la variables $x_1$ y $x_2$, respectivamente. 

## Implementación

**e.** Resuelva el modelo planteado utilizando la librería de PulP en Python. ¿Cuál es la solución
óptima del problema? 

#se importa la libreria de PulP
import pulp as lp

#-------------------------------------
# Creación del objeto problema en PuLP
#-------------------------------------
problema = lp.LpProblem("Perla",       #Nombre
                        lp.LpMaximize) #Sentido de la optimización

#-----------------------------
# Variables de Decisión
#-----------------------------
#Unidades de chocolate oscuro producidas cada semana
x_1 = lp.LpVariable("C_oscuro",            #Nombre
                    lowBound = 0,          #Cota inferior
                    upBound = None,        #Cota superior
                    cat = lp.LpContinuous) #Tipo de variable
#Unidades de chocolate blanco producidas cada semana
x_2 = lp.LpVariable("C_blanco",            #Nombre
                    lowBound = 0,          #Cota inferior
                    upBound = None,        #Cota superior
                    cat = lp.LpContinuous) #Tipo de variable

#-----------------------------
# Función objetivo
#-----------------------------
#(1) Crea la expresión de maximización de utilidades 
problema += 3500*x_1 + 4000*x_2, "Utilidades Totales"

#-----------------------------
# Restricciones
#-----------------------------
#(2) Respeta la disponibilidad de manteca de cacao 
problema += 6*x_1 + 22*x_2 <= 12000, "Manteca_cacao"
#(3) Respeta la disponibilidad de azucar
problema += 21*x_1 +18*x_2 <= 20000, "Azucar"
#(4) Garantiza que la producción no sobrepase a lo demandado
problema += x_2 <= 315, "Demanda"

#-----------------------------
# Imprimir formato LP
#-----------------------------
#Escribe el problema en un archivo con formato LP 
problema.writeLP("Perla.lp")

#-----------------------------
# Invocar el optimizador
#-----------------------------
#Optimizar el modelo con CBC (default de PuLP)
problema.solve()

#-----------------------------
#    Imprimir resultados
#-----------------------------
#Imprimir estado final del optimizador
print("Estado (optimizador):", lp.LpStatus[problema.status],end='\n')
#Imprimir el valor de la función objetivo
print("\nFunción objetivo = $", round(lp.value(problema.objective),2))
#Imprimir el valor de las variables
print("Fabricar ",x_1.value(),"\t unidades de chocolate oscuro")
print("Fabricar ",x_2.value(),"\t unidades de chocolate blanco")

## Créditos

Equipo Principios de Optimización<br>
Instancias: Alfaima Solano<br>
Fecha: 30/09/2020