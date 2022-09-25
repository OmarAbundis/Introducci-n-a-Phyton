#Código ejecutado en Raspberry pi3
#es código para pyton

# se importan funciones de la biblioteca SMBus
from smbus2 import SMBus
# se importan funciones de la biblioteca MLX90614
from mlx90614 import MLX90614

bus = SMBus(1)
sensor = MLX90614(bus, address = 0x5A)
print ("Temperatura ambiente: ",sensor.get_amb_temp())
print ("Temperatura de persona u objeto: ",sensor.get_obj_temp())
bus.close()

# url de referencia
# https://github.com/sightsdev/PyMLX90614