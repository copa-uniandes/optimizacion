\* OptiJuice *\
Maximize
Ingresos_Totales: 10000 x_('Colombiano',_'Guayaba')
 + 10000 x_('Colombiano',_'Níspero') + 10000 x_('Colombiano',_'Piña')
 + 10000 x_('Colombiano',_'Zapote') + 8000 x_('Light',_'Guayaba')
 + 8000 x_('Light',_'Níspero') + 8000 x_('Light',_'Piña')
 + 8000 x_('Light',_'Zapote') + 6000 x_('Mañanero',_'Guayaba')
 + 6000 x_('Mañanero',_'Níspero') + 6000 x_('Mañanero',_'Piña')
 + 6000 x_('Mañanero',_'Zapote') + 7000 x_('Refrescante',_'Guayaba')
 + 7000 x_('Refrescante',_'Níspero') + 7000 x_('Refrescante',_'Piña')
 + 7000 x_('Refrescante',_'Zapote') + 9000 x_('Saludable',_'Guayaba')
 + 9000 x_('Saludable',_'Níspero') + 9000 x_('Saludable',_'Piña')
 + 9000 x_('Saludable',_'Zapote') + 5000 x_('Tropical',_'Guayaba')
 + 5000 x_('Tropical',_'Níspero') + 5000 x_('Tropical',_'Piña')
 + 5000 x_('Tropical',_'Zapote')
Subject To
Demanda_mínima_jugo_Colombiano: x_('Colombiano',_'Guayaba')
 + x_('Colombiano',_'Níspero') + x_('Colombiano',_'Piña')
 + x_('Colombiano',_'Zapote') <= 1035
Demanda_mínima_jugo_Light: x_('Light',_'Guayaba') + x_('Light',_'Níspero')
 + x_('Light',_'Piña') + x_('Light',_'Zapote') <= 1353
Demanda_mínima_jugo_Mañanero: x_('Mañanero',_'Guayaba')
 + x_('Mañanero',_'Níspero') + x_('Mañanero',_'Piña')
 + x_('Mañanero',_'Zapote') <= 1865
Demanda_mínima_jugo_Refrescante: x_('Refrescante',_'Guayaba')
 + x_('Refrescante',_'Níspero') + x_('Refrescante',_'Piña')
 + x_('Refrescante',_'Zapote') <= 2231
Demanda_mínima_jugo_Saludable: x_('Saludable',_'Guayaba')
 + x_('Saludable',_'Níspero') + x_('Saludable',_'Piña')
 + x_('Saludable',_'Zapote') <= 1200
Demanda_mínima_jugo_Tropical: x_('Tropical',_'Guayaba')
 + x_('Tropical',_'Níspero') + x_('Tropical',_'Piña')
 + x_('Tropical',_'Zapote') <= 925
Máximo_fruta_Guayaba__jugo_Colombiano: 0.12 x_('Colombiano',_'Guayaba')
 - 0.88 x_('Colombiano',_'Níspero') - 0.88 x_('Colombiano',_'Piña')
 - 0.88 x_('Colombiano',_'Zapote') <= 0
Máximo_fruta_Guayaba__jugo_Light: 0.45 x_('Light',_'Guayaba')
 - 0.55 x_('Light',_'Níspero') - 0.55 x_('Light',_'Piña')
 - 0.55 x_('Light',_'Zapote') <= 0
Máximo_fruta_Guayaba__jugo_Mañanero: 0.39 x_('Mañanero',_'Guayaba')
 - 0.61 x_('Mañanero',_'Níspero') - 0.61 x_('Mañanero',_'Piña')
 - 0.61 x_('Mañanero',_'Zapote') <= 0
Máximo_fruta_Guayaba__jugo_Refrescante: 0.15 x_('Refrescante',_'Guayaba')
 - 0.85 x_('Refrescante',_'Níspero') - 0.85 x_('Refrescante',_'Piña')
 - 0.85 x_('Refrescante',_'Zapote') <= 0
Máximo_fruta_Guayaba__jugo_Saludable: 0.17 x_('Saludable',_'Guayaba')
 - 0.83 x_('Saludable',_'Níspero') - 0.83 x_('Saludable',_'Piña')
 - 0.83 x_('Saludable',_'Zapote') <= 0
Máximo_fruta_Guayaba__jugo_Tropical: 0.24 x_('Tropical',_'Guayaba')
 - 0.76 x_('Tropical',_'Níspero') - 0.76 x_('Tropical',_'Piña')
 - 0.76 x_('Tropical',_'Zapote') <= 0
Máximo_fruta_Níspero__jugo_Colombiano: - 0.63 x_('Colombiano',_'Guayaba')
 + 0.37 x_('Colombiano',_'Níspero') - 0.63 x_('Colombiano',_'Piña')
 - 0.63 x_('Colombiano',_'Zapote') <= 0
Máximo_fruta_Níspero__jugo_Light: - 0.82 x_('Light',_'Guayaba')
 + 0.18 x_('Light',_'Níspero') - 0.82 x_('Light',_'Piña')
 - 0.82 x_('Light',_'Zapote') <= 0
Máximo_fruta_Níspero__jugo_Mañanero: - 0.28 x_('Mañanero',_'Guayaba')
 + 0.72 x_('Mañanero',_'Níspero') - 0.28 x_('Mañanero',_'Piña')
 - 0.28 x_('Mañanero',_'Zapote') <= 0
Máximo_fruta_Níspero__jugo_Refrescante: - 0.73 x_('Refrescante',_'Guayaba')
 + 0.27 x_('Refrescante',_'Níspero') - 0.73 x_('Refrescante',_'Piña')
 - 0.73 x_('Refrescante',_'Zapote') <= 0
Máximo_fruta_Níspero__jugo_Saludable: - 0.66 x_('Saludable',_'Guayaba')
 + 0.34 x_('Saludable',_'Níspero') - 0.66 x_('Saludable',_'Piña')
 - 0.66 x_('Saludable',_'Zapote') <= 0
Máximo_fruta_Níspero__jugo_Tropical: - 0.69 x_('Tropical',_'Guayaba')
 + 0.31 x_('Tropical',_'Níspero') - 0.69 x_('Tropical',_'Piña')
 - 0.69 x_('Tropical',_'Zapote') <= 0
Máximo_fruta_Piña__jugo_Colombiano: - 0.82 x_('Colombiano',_'Guayaba')
 - 0.82 x_('Colombiano',_'Níspero') + 0.18 x_('Colombiano',_'Piña')
 - 0.82 x_('Colombiano',_'Zapote') <= 0
Máximo_fruta_Piña__jugo_Light: - 0.5 x_('Light',_'Guayaba')
 - 0.5 x_('Light',_'Níspero') + 0.5 x_('Light',_'Piña')
 - 0.5 x_('Light',_'Zapote') <= 0
Máximo_fruta_Piña__jugo_Mañanero: - 0.81 x_('Mañanero',_'Guayaba')
 - 0.81 x_('Mañanero',_'Níspero') + 0.19 x_('Mañanero',_'Piña')
 - 0.81 x_('Mañanero',_'Zapote') <= 0
Máximo_fruta_Piña__jugo_Refrescante: - 0.6 x_('Refrescante',_'Guayaba')
 - 0.6 x_('Refrescante',_'Níspero') + 0.4 x_('Refrescante',_'Piña')
 - 0.6 x_('Refrescante',_'Zapote') <= 0
Máximo_fruta_Piña__jugo_Saludable: - 0.95 x_('Saludable',_'Guayaba')
 - 0.95 x_('Saludable',_'Níspero') + 0.05 x_('Saludable',_'Piña')
 - 0.95 x_('Saludable',_'Zapote') <= 0
Máximo_fruta_Piña__jugo_Tropical: - 0.92 x_('Tropical',_'Guayaba')
 - 0.92 x_('Tropical',_'Níspero') + 0.08 x_('Tropical',_'Piña')
 - 0.92 x_('Tropical',_'Zapote') <= 0
Máximo_fruta_Zapote__jugo_Colombiano: - 0.98 x_('Colombiano',_'Guayaba')
 - 0.98 x_('Colombiano',_'Níspero') - 0.98 x_('Colombiano',_'Piña')
 + 0.02 x_('Colombiano',_'Zapote') <= 0
Máximo_fruta_Zapote__jugo_Light: - 0.91 x_('Light',_'Guayaba')
 - 0.91 x_('Light',_'Níspero') - 0.91 x_('Light',_'Piña')
 + 0.09 x_('Light',_'Zapote') <= 0
Máximo_fruta_Zapote__jugo_Mañanero: - 0.94 x_('Mañanero',_'Guayaba')
 - 0.94 x_('Mañanero',_'Níspero') - 0.94 x_('Mañanero',_'Piña')
 + 0.06 x_('Mañanero',_'Zapote') <= 0
Máximo_fruta_Zapote__jugo_Refrescante: - 0.78 x_('Refrescante',_'Guayaba')
 - 0.78 x_('Refrescante',_'Níspero') - 0.78 x_('Refrescante',_'Piña')
 + 0.22 x_('Refrescante',_'Zapote') <= 0
Máximo_fruta_Zapote__jugo_Saludable: - 0.87 x_('Saludable',_'Guayaba')
 - 0.87 x_('Saludable',_'Níspero') - 0.87 x_('Saludable',_'Piña')
 + 0.13 x_('Saludable',_'Zapote') <= 0
Máximo_fruta_Zapote__jugo_Tropical: - 0.56 x_('Tropical',_'Guayaba')
 - 0.56 x_('Tropical',_'Níspero') - 0.56 x_('Tropical',_'Piña')
 + 0.44 x_('Tropical',_'Zapote') <= 0
Mínimo_fruta_Guayaba__jugo_Colombiano: 0.95 x_('Colombiano',_'Guayaba')
 - 0.05 x_('Colombiano',_'Níspero') - 0.05 x_('Colombiano',_'Piña')
 - 0.05 x_('Colombiano',_'Zapote') >= 0
Mínimo_fruta_Guayaba__jugo_Light: 0.81 x_('Light',_'Guayaba')
 - 0.19 x_('Light',_'Níspero') - 0.19 x_('Light',_'Piña')
 - 0.19 x_('Light',_'Zapote') >= 0
Mínimo_fruta_Guayaba__jugo_Mañanero: 0.69 x_('Mañanero',_'Guayaba')
 - 0.31 x_('Mañanero',_'Níspero') - 0.31 x_('Mañanero',_'Piña')
 - 0.31 x_('Mañanero',_'Zapote') >= 0
Mínimo_fruta_Guayaba__jugo_Refrescante: 0.5 x_('Refrescante',_'Guayaba')
 - 0.5 x_('Refrescante',_'Níspero') - 0.5 x_('Refrescante',_'Piña')
 - 0.5 x_('Refrescante',_'Zapote') >= 0
Mínimo_fruta_Guayaba__jugo_Saludable: 0.73 x_('Saludable',_'Guayaba')
 - 0.27 x_('Saludable',_'Níspero') - 0.27 x_('Saludable',_'Piña')
 - 0.27 x_('Saludable',_'Zapote') >= 0
Mínimo_fruta_Guayaba__jugo_Tropical: 0.7 x_('Tropical',_'Guayaba')
 - 0.3 x_('Tropical',_'Níspero') - 0.3 x_('Tropical',_'Piña')
 - 0.3 x_('Tropical',_'Zapote') >= 0
Mínimo_fruta_Níspero__jugo_Colombiano: - 0.15 x_('Colombiano',_'Guayaba')
 + 0.85 x_('Colombiano',_'Níspero') - 0.15 x_('Colombiano',_'Piña')
 - 0.15 x_('Colombiano',_'Zapote') >= 0
Mínimo_fruta_Níspero__jugo_Light: - 0.14 x_('Light',_'Guayaba')
 + 0.86 x_('Light',_'Níspero') - 0.14 x_('Light',_'Piña')
 - 0.14 x_('Light',_'Zapote') >= 0
Mínimo_fruta_Níspero__jugo_Mañanero: - 0.28 x_('Mañanero',_'Guayaba')
 + 0.72 x_('Mañanero',_'Níspero') - 0.28 x_('Mañanero',_'Piña')
 - 0.28 x_('Mañanero',_'Zapote') >= 0
Mínimo_fruta_Níspero__jugo_Refrescante: - 0.02 x_('Refrescante',_'Guayaba')
 + 0.98 x_('Refrescante',_'Níspero') - 0.02 x_('Refrescante',_'Piña')
 - 0.02 x_('Refrescante',_'Zapote') >= 0
Mínimo_fruta_Níspero__jugo_Saludable: - 0.12 x_('Saludable',_'Guayaba')
 + 0.88 x_('Saludable',_'Níspero') - 0.12 x_('Saludable',_'Piña')
 - 0.12 x_('Saludable',_'Zapote') >= 0
Mínimo_fruta_Níspero__jugo_Tropical: - 0.31 x_('Tropical',_'Guayaba')
 + 0.69 x_('Tropical',_'Níspero') - 0.31 x_('Tropical',_'Piña')
 - 0.31 x_('Tropical',_'Zapote') >= 0
Mínimo_fruta_Piña__jugo_Colombiano: - 0.11 x_('Colombiano',_'Guayaba')
 - 0.11 x_('Colombiano',_'Níspero') + 0.89 x_('Colombiano',_'Piña')
 - 0.11 x_('Colombiano',_'Zapote') >= 0
Mínimo_fruta_Piña__jugo_Light: - 0.36 x_('Light',_'Guayaba')
 - 0.36 x_('Light',_'Níspero') + 0.64 x_('Light',_'Piña')
 - 0.36 x_('Light',_'Zapote') >= 0
Mínimo_fruta_Piña__jugo_Mañanero: - 0.07 x_('Mañanero',_'Guayaba')
 - 0.07 x_('Mañanero',_'Níspero') + 0.93 x_('Mañanero',_'Piña')
 - 0.07 x_('Mañanero',_'Zapote') >= 0
Mínimo_fruta_Piña__jugo_Refrescante: - 0.46 x_('Refrescante',_'Guayaba')
 - 0.46 x_('Refrescante',_'Níspero') + 0.54 x_('Refrescante',_'Piña')
 - 0.46 x_('Refrescante',_'Zapote') >= 0
Mínimo_fruta_Piña__jugo_Saludable: - 0.32 x_('Saludable',_'Guayaba')
 - 0.32 x_('Saludable',_'Níspero') + 0.68 x_('Saludable',_'Piña')
 - 0.32 x_('Saludable',_'Zapote') >= 0
Mínimo_fruta_Piña__jugo_Tropical: - 0.18 x_('Tropical',_'Guayaba')
 - 0.18 x_('Tropical',_'Níspero') + 0.82 x_('Tropical',_'Piña')
 - 0.18 x_('Tropical',_'Zapote') >= 0
Mínimo_fruta_Zapote__jugo_Colombiano: - 0.18 x_('Colombiano',_'Guayaba')
 - 0.18 x_('Colombiano',_'Níspero') - 0.18 x_('Colombiano',_'Piña')
 + 0.82 x_('Colombiano',_'Zapote') >= 0
Mínimo_fruta_Zapote__jugo_Light: - 0.4 x_('Light',_'Guayaba')
 - 0.4 x_('Light',_'Níspero') - 0.4 x_('Light',_'Piña')
 + 0.6 x_('Light',_'Zapote') >= 0
Mínimo_fruta_Zapote__jugo_Mañanero: - 0.22 x_('Mañanero',_'Guayaba')
 - 0.22 x_('Mañanero',_'Níspero') - 0.22 x_('Mañanero',_'Piña')
 + 0.78 x_('Mañanero',_'Zapote') >= 0
Mínimo_fruta_Zapote__jugo_Refrescante: - 0.43 x_('Refrescante',_'Guayaba')
 - 0.43 x_('Refrescante',_'Níspero') - 0.43 x_('Refrescante',_'Piña')
 + 0.57 x_('Refrescante',_'Zapote') >= 0
Mínimo_fruta_Zapote__jugo_Saludable: - 0.13 x_('Saludable',_'Guayaba')
 - 0.13 x_('Saludable',_'Níspero') - 0.13 x_('Saludable',_'Piña')
 + 0.87 x_('Saludable',_'Zapote') >= 0
Mínimo_fruta_Zapote__jugo_Tropical: - 0.34 x_('Tropical',_'Guayaba')
 - 0.34 x_('Tropical',_'Níspero') - 0.34 x_('Tropical',_'Piña')
 + 0.66 x_('Tropical',_'Zapote') >= 0
límite_fruta_Guayaba: x_('Colombiano',_'Guayaba') + x_('Light',_'Guayaba')
 + x_('Mañanero',_'Guayaba') + x_('Refrescante',_'Guayaba')
 + x_('Saludable',_'Guayaba') + x_('Tropical',_'Guayaba') <= 1902
límite_fruta_Níspero: x_('Colombiano',_'Níspero') + x_('Light',_'Níspero')
 + x_('Mañanero',_'Níspero') + x_('Refrescante',_'Níspero')
 + x_('Saludable',_'Níspero') + x_('Tropical',_'Níspero') <= 2683
límite_fruta_Piña: x_('Colombiano',_'Piña') + x_('Light',_'Piña')
 + x_('Mañanero',_'Piña') + x_('Refrescante',_'Piña')
 + x_('Saludable',_'Piña') + x_('Tropical',_'Piña') <= 4318
límite_fruta_Zapote: x_('Colombiano',_'Zapote') + x_('Light',_'Zapote')
 + x_('Mañanero',_'Zapote') + x_('Refrescante',_'Zapote')
 + x_('Saludable',_'Zapote') + x_('Tropical',_'Zapote') <= 1111
End
