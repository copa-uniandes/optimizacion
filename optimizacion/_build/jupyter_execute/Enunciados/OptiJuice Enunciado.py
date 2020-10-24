#!/usr/bin/env python
# coding: utf-8

# # Producción de jugos

# ## Enunciado
# 
# OptiJuice es una empresa que produce jugos. Ellos han decidido producir un nuevo conjunto de jugos autóctonos ($K$). Los jugos son una mezcla de diferentes frutas tropicales ($R$) dentro de las que se encuentran la piña, la guayaba, el níspero y el zapote. Cada uno de los tipos de jugo se diferencia de los demás en la cantidad de litros de zumo que tiene de las distintas frutas. Es por esto que, para garantizar la calidad de los jugos es necesario que el jugo del tipo $k \in K$ contenga entre un $l_{ki}$% y un $u_{ki}$% de litros de zumo de la fruta $i \in R$. Para la producción de jugos, OptiJuice tiene disponibles $b_i$ litros de zumo de la fruta $i \in R$. La compañía espera una demanda mínima de $d_k$ litros y desea vender cada litro de jugo del tipo $k \in K$ a $p_k$ pesos. La información mencionada se presenta en las Tablas 1 a 4. 
# 
# Usted debe formular un programa lineal que le permita OptiJuice responder la siguiente pregunta: ¿Cuántos litros de zumo de cada fruta se deben mezclar para producir cada uno de los tipos de jugos, de manera que se cumplan las condiciones previamente expuestas y se maximicen los ingresos totales?

# <p style="text-align: center;"><b>Tabla 1. Mínimo porcentaje de las frutas en los jugos</b></p>
# 
# <table class="egt">
#     
#   <tr>  
#     <th>Mínimo porcentaje</th> 
#     <th colspan="5";style="text-align:center">Frutas</th>
#   </tr>
#     
#   <tr>
#     <th style="text-align:center">Jugos</th>
#     <td style="text-align:center"><i>Piña (%)</i></td>
#     <td style="text-align:center"><i>Guayaba (%)</i></td>
#     <td style="text-align:center"><i>Nispero (%)</i></td>
#     <td style="text-align:center"><i>Zapote (%)</i></td>
#   </tr>
# 
#   <tr>
#     <td style="text-align:left"><i>Saludable</i></td>
#     <td style="text-align:center">32</td>
#     <td style="text-align:center">27</td>
#     <td style="text-align:center">12</td>
#     <td style="text-align:center">13</td>
#   </tr>
#     
#   <tr>
#     <td style="text-align:left"><i>Tropical</i></td>
#     <td style="text-align:center">18</td>
#     <td style="text-align:center">30</td>
#     <td style="text-align:center">31</td>
#     <td style="text-align:center">34</td>
#   </tr>
#     
#   <tr>
#     <td style="text-align:left"><i>Mañanero</i></td>
#     <td style="text-align:center">7</td>
#     <td style="text-align:center">31</td>
#     <td style="text-align:center">28</td>
#     <td style="text-align:center">22</td>
#   </tr>
# 
#   <tr>
#     <td style="text-align:left"><i>Colombiano</i></td>
#     <td style="text-align:center">11</td>
#     <td style="text-align:center">5</td>
#     <td style="text-align:center">15</td>
#     <td style="text-align:center">18</td>
#   </tr>
#     
#   <tr>
#     <td style="text-align:left"><i>Refrescante</i></td>
#     <td style="text-align:center">46</td>
#     <td style="text-align:center">50</td>
#     <td style="text-align:center">2</td>
#     <td style="text-align:center">43</td>
#   </tr>
#     
#   <tr>
#     <td style="text-align:left"><i>Light</i></td>
#     <td style="text-align:center">36</td>
#     <td style="text-align:center">19</td>
#     <td style="text-align:center">14</td>
#     <td style="text-align:center">40</td>
#   </tr>
#     
# </table>

# <p style="text-align: center;"><b>Tabla 2. Máximo porcentaje de las frutas en los jugos</b></p>
# 
# <table class="egt">
#     
#   <tr>  
#     <th>Máximo porcentaje</th> 
#     <th colspan="5";style="text-align:center">Frutas</th>
#   </tr>
#     
#   <tr>
#     <th style="text-align:center">Jugos</th>
#     <td style="text-align:center"><i>Piña (%)</i></td>
#     <td style="text-align:center"><i>Guayaba (%)</i></td>
#     <td style="text-align:center"><i>Nispero (%)</i></td>
#     <td style="text-align:center"><i>Zapote (%)</i></td>
#   </tr>
# 
#   <tr>
#     <td style="text-align:left"><i>Saludable</i></td>
#     <td style="text-align:center">95</td>
#     <td style="text-align:center">83</td>
#     <td style="text-align:center">66</td>
#     <td style="text-align:center">87</td>
#   </tr>
#     
#   <tr>
#     <td style="text-align:left"><i>Tropical</i></td>
#     <td style="text-align:center">92</td>
#     <td style="text-align:center">76</td>
#     <td style="text-align:center">69</td>
#     <td style="text-align:center">56</td>
#   </tr>
#     
#   <tr>
#     <td style="text-align:left"><i>Mañanero</i></td>
#     <td style="text-align:center">81</td>
#     <td style="text-align:center">61</td>
#     <td style="text-align:center">28</td>
#     <td style="text-align:center">94</td>
#   </tr>
# 
#   <tr>
#     <td style="text-align:left"><i>Colombiano</i></td>
#     <td style="text-align:center">82</td>
#     <td style="text-align:center">88</td>
#     <td style="text-align:center">63</td>
#     <td style="text-align:center">98</td>
#   </tr>
#     
#   <tr>
#     <td style="text-align:left"><i>Refrescante</i></td>
#     <td style="text-align:center">60</td>
#     <td style="text-align:center">85</td>
#     <td style="text-align:center">73</td>
#     <td style="text-align:center">78</td>
#   </tr>
#     
#   <tr>
#     <td style="text-align:left"><i>Light</i></td>
#     <td style="text-align:center">50</td>
#     <td style="text-align:center">55</td>
#     <td style="text-align:center">82</td>
#     <td style="text-align:center">91</td>
#   </tr>
#     
# </table>

# <p style="text-align: center;"><b>Tabla 3. Litros disponibles de cada fruta</b></p>
# 
# <table class="egt">
#     
#   <tr>  
#     <th style="text-align:center">Frutas</th> 
#     <th style="text-align:center">Litros disponibles</th>
#   </tr>
#     
#   <tr>
#     <td style="text-align:center"><i>Piña</i></td>
#     <td style="text-align:center">4,318</td>
#   </tr>
#     
#   <tr>
#     <td style="text-align:center"><i>Guayaba</i></td>
#     <td style="text-align:center">1,902</td>
#   </tr>
#     
#   <tr>
#     <td style="text-align:center"><i>Nispero</i></td>
#     <td style="text-align:center">2,683</td>
#   </tr>
#     
#   <tr>
#     <td style="text-align:center"><i>Zapote</i></td>
#     <td style="text-align:center">1,111</td>
#   </tr>
#     
# </table>

# <p style="text-align: center;"><b>Tabla 4. Demanda mínima y precio de cada jugo</b></p>
# 
# <table class="egt">
#     
#   <tr>  
#     <th style="text-align:center">Jugos</th> 
#     <th style="text-align:center">Demanda mínima</th>
#     <th style="text-align:center">Precio</th>
#   </tr>
#     
#   <tr>
#     <td style="text-align:center"><i>Saludable</i></td>
#     <td style="text-align:center">1,200</td>
#     <td style="text-align:center">9,000</td>
#   </tr>
#     
#   <tr>
#     <td style="text-align:center"><i>Tropical</i></td>
#     <td style="text-align:center">925</td>
#     <td style="text-align:center">5,000</td>
#   </tr>
#     
#   <tr>
#     <td style="text-align:center"><i>Mañanero</i></td>
#     <td style="text-align:center">1,865</td>
#     <td style="text-align:center">6,000</td>
#   </tr>
#     
#   <tr>
#     <td style="text-align:center"><i>Colombiano</i></td>
#     <td style="text-align:center">1,035</td>
#     <td style="text-align:center">10,000</td>
#   </tr>
#     
#   <tr>
#     <td style="text-align:center"><i>Refrescante</i></td>
#     <td style="text-align:center">2,231</td>
#     <td style="text-align:center">7,000</td>
#   </tr>
#     
#   <tr>
#     <td style="text-align:center"><i>Light</i></td>
#     <td style="text-align:center">1,353</td>
#     <td style="text-align:center">8,000</td>
#   </tr>
#     
# </table>

# Usted debe formular un programa lineal que le permita OptiJuice responder la siguiente pregunta: ¿Cuántos litros de zumo de cada fruta se deben mezclar para producir cada uno de los tipos de jugos, de manera que se cumplan las condiciones previamente expuestas y se maximicen los ingresos totales?

# ## Formulación
# 
# **a.** Describa la(s) variable(s) de decisión que utilizará en el modelo. 
# 

# 
# **b.** Escriba la(s) restricción(es) lineal(es) que describe(n) que el jugo del tipo $k\in K$ debe contener entre un $l_{ki}$% y un $u_{ki}$% de litros de zumo de la fruta $i\in R$. 
# 

# **c.** Escriba la(s) restricción(es) que describe(n) que OptiJuice puede utilizar máximo $b_i$ litros de zumo de la fruta $i\in R$. 
# 

# **d.** Escriba la(s) restricción(es) que describe(n) que OptiJuice desea cumplir con la demanda mínima de $d_k$ litros jugo del tipo $k\in K$. 
# 

# **e.** Escriba la(s) restricción(es) que describe(n) matemáticamente el tipo de variable(s) que está utilizando dentro del modelo. 
# 

# **f.** Escriba la función objetivo que maximiza los ingresos totales.
# 

# ## Implementación
# 
# **g.** Resuelva el modelo planteado utilizando la librería de PulP en Python. ¿Cuál es la solución
# óptima del problema? 

# In[ ]:





# ## Créditos
# 
# Equipo Principios de Optimización<br>
# Instancias: Juan Felipe Rengifo M, Camilo Aguilar<br>
# Fecha: 05/09/2020

# 
# ```{toctree}
# :hidden:
# :titlesonly:
# 
# 
# ../Soluciones/OptiJuice
# ```
# 
