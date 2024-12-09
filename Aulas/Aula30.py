"""
CONSTANTES = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61 # Velocidade atual do carro
local_carro = 99 # Local em que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

inicio_range_radar_1 = LOCAL_1 - RADAR_RANGE
fim_range_radar_1 = LOCAL_1 + RADAR_RANGE

if (velocidade > RADAR_1):
    print("O carro passou da velocidade limite")

if (local_carro >= inicio_range_radar_1 and \
    local_carro <= fim_range_radar_1):
      print("Carrou passou no radar 1")

if local_carro >= inicio_range_radar_1 and \
    local_carro <= fim_range_radar_1 and \
    velocidade > RADAR_1:
        print("O carro foi multado no radar 1")