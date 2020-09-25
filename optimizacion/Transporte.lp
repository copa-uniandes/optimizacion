\* Transporte *\
Minimize
Costos_Totales: 650 x_('Planta_1',_'Distribuidor_1')
 + 125 x_('Planta_1',_'Distribuidor_2')
 + 1200 x_('Planta_1',_'Distribuidor_3')
 + 340 x_('Planta_1',_'Distribuidor_4') + 150 x_('Planta_1',_'Distribuidor_5')
 + 260 x_('Planta_1',_'Distribuidor_6') + 350 x_('Planta_1',_'Distribuidor_7')
 + 800 x_('Planta_1',_'Distribuidor_8') + 250 x_('Planta_2',_'Distribuidor_1')
 + 200 x_('Planta_2',_'Distribuidor_2') + 250 x_('Planta_2',_'Distribuidor_3')
 + 600 x_('Planta_2',_'Distribuidor_4') + 150 x_('Planta_2',_'Distribuidor_5')
 + 950 x_('Planta_2',_'Distribuidor_6')
 + 1050 x_('Planta_2',_'Distribuidor_7')
 + 1000 x_('Planta_2',_'Distribuidor_8')
 + 600 x_('Planta_3',_'Distribuidor_1') + 350 x_('Planta_3',_'Distribuidor_2')
 + 400 x_('Planta_3',_'Distribuidor_3') + 260 x_('Planta_3',_'Distribuidor_4')
 + 150 x_('Planta_3',_'Distribuidor_5') + 300 x_('Planta_3',_'Distribuidor_6')
 + 450 x_('Planta_3',_'Distribuidor_7') + 600 x_('Planta_3',_'Distribuidor_8')
 + 450 x_('Planta_4',_'Distribuidor_1') + 800 x_('Planta_4',_'Distribuidor_2')
 + 650 x_('Planta_4',_'Distribuidor_3') + 250 x_('Planta_4',_'Distribuidor_4')
 + 340 x_('Planta_4',_'Distribuidor_5') + 700 x_('Planta_4',_'Distribuidor_6')
 + 600 x_('Planta_4',_'Distribuidor_7') + 620 x_('Planta_4',_'Distribuidor_8')
Subject To
Demanda_del_distribuidor_Distribuidor_1: x_('Planta_1',_'Distribuidor_1')
 + x_('Planta_2',_'Distribuidor_1') + x_('Planta_3',_'Distribuidor_1')
 + x_('Planta_4',_'Distribuidor_1') >= 930
Demanda_del_distribuidor_Distribuidor_2: x_('Planta_1',_'Distribuidor_2')
 + x_('Planta_2',_'Distribuidor_2') + x_('Planta_3',_'Distribuidor_2')
 + x_('Planta_4',_'Distribuidor_2') >= 600
Demanda_del_distribuidor_Distribuidor_3: x_('Planta_1',_'Distribuidor_3')
 + x_('Planta_2',_'Distribuidor_3') + x_('Planta_3',_'Distribuidor_3')
 + x_('Planta_4',_'Distribuidor_3') >= 460
Demanda_del_distribuidor_Distribuidor_4: x_('Planta_1',_'Distribuidor_4')
 + x_('Planta_2',_'Distribuidor_4') + x_('Planta_3',_'Distribuidor_4')
 + x_('Planta_4',_'Distribuidor_4') >= 610
Demanda_del_distribuidor_Distribuidor_5: x_('Planta_1',_'Distribuidor_5')
 + x_('Planta_2',_'Distribuidor_5') + x_('Planta_3',_'Distribuidor_5')
 + x_('Planta_4',_'Distribuidor_5') >= 830
Demanda_del_distribuidor_Distribuidor_6: x_('Planta_1',_'Distribuidor_6')
 + x_('Planta_2',_'Distribuidor_6') + x_('Planta_3',_'Distribuidor_6')
 + x_('Planta_4',_'Distribuidor_6') >= 460
Demanda_del_distribuidor_Distribuidor_7: x_('Planta_1',_'Distribuidor_7')
 + x_('Planta_2',_'Distribuidor_7') + x_('Planta_3',_'Distribuidor_7')
 + x_('Planta_4',_'Distribuidor_7') >= 640
Demanda_del_distribuidor_Distribuidor_8: x_('Planta_1',_'Distribuidor_8')
 + x_('Planta_2',_'Distribuidor_8') + x_('Planta_3',_'Distribuidor_8')
 + x_('Planta_4',_'Distribuidor_8') >= 240
Oferta_de_la_planta_Planta_1: x_('Planta_1',_'Distribuidor_1')
 + x_('Planta_1',_'Distribuidor_2') + x_('Planta_1',_'Distribuidor_3')
 + x_('Planta_1',_'Distribuidor_4') + x_('Planta_1',_'Distribuidor_5')
 + x_('Planta_1',_'Distribuidor_6') + x_('Planta_1',_'Distribuidor_7')
 + x_('Planta_1',_'Distribuidor_8') <= 1500
Oferta_de_la_planta_Planta_2: x_('Planta_2',_'Distribuidor_1')
 + x_('Planta_2',_'Distribuidor_2') + x_('Planta_2',_'Distribuidor_3')
 + x_('Planta_2',_'Distribuidor_4') + x_('Planta_2',_'Distribuidor_5')
 + x_('Planta_2',_'Distribuidor_6') + x_('Planta_2',_'Distribuidor_7')
 + x_('Planta_2',_'Distribuidor_8') <= 1200
Oferta_de_la_planta_Planta_3: x_('Planta_3',_'Distribuidor_1')
 + x_('Planta_3',_'Distribuidor_2') + x_('Planta_3',_'Distribuidor_3')
 + x_('Planta_3',_'Distribuidor_4') + x_('Planta_3',_'Distribuidor_5')
 + x_('Planta_3',_'Distribuidor_6') + x_('Planta_3',_'Distribuidor_7')
 + x_('Planta_3',_'Distribuidor_8') <= 1400
Oferta_de_la_planta_Planta_4: x_('Planta_4',_'Distribuidor_1')
 + x_('Planta_4',_'Distribuidor_2') + x_('Planta_4',_'Distribuidor_3')
 + x_('Planta_4',_'Distribuidor_4') + x_('Planta_4',_'Distribuidor_5')
 + x_('Planta_4',_'Distribuidor_6') + x_('Planta_4',_'Distribuidor_7')
 + x_('Planta_4',_'Distribuidor_8') <= 1000
End
