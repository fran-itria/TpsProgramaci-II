import time
from calendar import isleap


def anio_bisiesto(anio):
    return isleap(anio)


def calcular_dias_mes(mes, anio_bisiesto):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes == 4:
        return 30
    elif mes == 2:
        return 29 if anio_bisiesto else 28
    else:
        return 0


def calcular_equivalente_en_dias(anio_comienzo, anio_fin):
    dias = 0
    for a in range(anio_comienzo, anio_fin):
        dias += 366 if anio_bisiesto(a) else 365

    hora_local = time.localtime(time.time())
    for m in range(1, hora_local.tm_mon):
        dias += calcular_dias_mes(m, anio_bisiesto(hora_local.tm_year))
    dias += hora_local.tm_mday

    return dias
