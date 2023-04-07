\* PlaneaciónMenús *\
Minimize
OBJ: 200 x_Banano + 450 x_Brócoli + 450 x_Calabacín + 2900 x_Cerdo
 + 600 x_Espinaca + 800 x_Guisantes + 650 x_Manzana + 570 x_Naranja
 + 500 x_Pepino + 550 x_Pera + 1420 x_Pollo + 4800 x_Res
Subject To
100_gramos_del_tipo_de_alimento_Carnes: x_Cerdo + x_Pollo + x_Res = 1
100_gramos_del_tipo_de_alimento_Frutas: x_Banano + x_Manzana + x_Naranja
 + x_Pera = 1
100_gramos_del_tipo_de_alimento_Verduras: x_Brócoli + x_Calabacín + x_Espinaca
 + x_Guisantes + x_Pepino = 1
Mínimo_aspecto_nutricional_Carbohidratos: 20.8 x_Banano + 4.9 x_Brócoli
 + 7.3 x_Calabacín + 1.5 x_Cerdo + 4.1 x_Espinaca + 18.2 x_Guisantes
 + 10.5 x_Manzana + 8.9 x_Naranja + 0.7 x_Pepino + 11.7 x_Pera + x_Pollo
 + 2 x_Res >= 25
Mínimo_aspecto_nutricional_Grasas: 0.3 x_Banano + 0.2 x_Brócoli
 + 0.1 x_Calabacín + 27 x_Cerdo + 0.3 x_Espinaca + 0.4 x_Guisantes
 + 2.7 x_Pepino + 0.1 x_Pera + 2 x_Pollo + 20 x_Res >= 5
Mínimo_aspecto_nutricional_Proteína: 1.2 x_Banano + 3.2 x_Brócoli
 + 4.2 x_Calabacín + 16 x_Cerdo + 2.5 x_Espinaca + 7.2 x_Guisantes
 + 0.3 x_Manzana + 0.8 x_Naranja + 0.15 x_Pepino + 0.4 x_Pera + 23 x_Pollo
 + 18 x_Res >= 17
Mínimo_aspecto_nutricional_Vitaminas: 35 x_Banano + 116 x_Brócoli
 + 21 x_Calabacín + 2 x_Cerdo + 52 x_Espinaca + 23 x_Guisantes + 5 x_Manzana
 + 50 x_Naranja + 9 x_Pepino + 12 x_Pera + 61 x_Pollo + 31 x_Res >= 100
End
