\* Inventarios *\
Maximize
OBJ: - 6.9 I_1 - 8.8 I_10 - 9.2 I_11 - 8.4 I_12 - 7.2 I_2 - 8 I_3 - 8.9 I_4
 - 9 I_5 - 7.8 I_6 - 6.7 I_7 - 7.3 I_8 - 7.8 I_9 - 172.8 x_1 - 178.3 x_10
 - 173.4 x_11 - 168.8 x_12 - 178.7 x_2 - 174.6 x_3 - 181.4 x_4 - 183 x_5
 - 177.7 x_6 - 182.8 x_7 - 186.8 x_8 - 181.8 x_9
Subject To
Inventario_en_la_semana_1: I_1 - x_1 = -83000
Inventario_en_la_semana_10: I_10 - I_9 - x_10 = -97987
Inventario_en_la_semana_11: - I_10 + I_11 - x_11 = -78390
Inventario_en_la_semana_12: - I_11 + I_12 - x_12 = -94068
Inventario_en_la_semana_2: - I_1 + I_2 - x_2 = -99750
Inventario_en_la_semana_3: - I_2 + I_3 - x_3 = -104738
Inventario_en_la_semana_4: - I_3 + I_4 - x_4 = -109974
Inventario_en_la_semana_5: - I_4 + I_5 - x_5 = -109974
Inventario_en_la_semana_6: - I_5 + I_6 - x_6 = -109974
Inventario_en_la_semana_7: - I_6 + I_7 - x_7 = -120972
Inventario_en_la_semana_8: - I_7 + I_8 - x_8 = -120972
Inventario_en_la_semana_9: - I_8 + I_9 - x_9 = -108875
Límite_inferior_de_producción_en_la_semana_1: x_1 >= 85000
Límite_inferior_de_producción_en_la_semana_10: x_10 >= 85000
Límite_inferior_de_producción_en_la_semana_11: x_11 >= 85000
Límite_inferior_de_producción_en_la_semana_12: x_12 >= 85000
Límite_inferior_de_producción_en_la_semana_2: x_2 >= 85000
Límite_inferior_de_producción_en_la_semana_3: x_3 >= 85000
Límite_inferior_de_producción_en_la_semana_4: x_4 >= 85000
Límite_inferior_de_producción_en_la_semana_5: x_5 >= 85000
Límite_inferior_de_producción_en_la_semana_6: x_6 >= 85000
Límite_inferior_de_producción_en_la_semana_7: x_7 >= 85000
Límite_inferior_de_producción_en_la_semana_8: x_8 >= 85000
Límite_inferior_de_producción_en_la_semana_9: x_9 >= 85000
Límite_superior_de_producción_en_la_semana_1: x_1 <= 110000
Límite_superior_de_producción_en_la_semana_10: x_10 <= 110000
Límite_superior_de_producción_en_la_semana_11: x_11 <= 110000
Límite_superior_de_producción_en_la_semana_12: x_12 <= 110000
Límite_superior_de_producción_en_la_semana_2: x_2 <= 110000
Límite_superior_de_producción_en_la_semana_3: x_3 <= 110000
Límite_superior_de_producción_en_la_semana_4: x_4 <= 110000
Límite_superior_de_producción_en_la_semana_5: x_5 <= 110000
Límite_superior_de_producción_en_la_semana_6: x_6 <= 110000
Límite_superior_de_producción_en_la_semana_7: x_7 <= 110000
Límite_superior_de_producción_en_la_semana_8: x_8 <= 110000
Límite_superior_de_producción_en_la_semana_9: x_9 <= 110000
End
