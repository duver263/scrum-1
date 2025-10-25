

temperatura_celsius = 25.7

grados_fahrenheit = (temperatura_celsius * 9/5) + 32

kelvin = temperatura_celsius + 273.15

print(f"{temperatura_celsius} en °C equivalen a {grados_fahrenheit} °F\n"\
      f"y {temperatura_celsius} en °C equivalen a {kelvin} K")


temp_caldera = 20.8

presion_caldera = 64.4

operador_presente = True

alarma_critica = False

if(temp_caldera > 100.0 and presion_caldera > 103.0):
    alarma_critica = True
    print(f"La alarma critica esta en: {alarma_critica}")
elif(temp_caldera > 105.0 and operador_presente == False):
    alarma_critica = True
    print(f"La alarma critica esta en: {alarma_critica}")
else:
    print(f"La alarma critica esta en: {alarma_critica}")