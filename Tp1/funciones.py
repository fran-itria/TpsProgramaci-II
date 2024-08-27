from calendar import isleap

def anio_bisiesto(anio):
    return isleap(anio)

def calcular_dias_mes(mes, anio_bisiesto):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if anio_bisiesto else 28
    
def calcular_edad_en_dias(hora_local, anio_comienzo, anio_fin):
    dias = 0
    for a in range(anio_comienzo, anio_fin):
        if anio_bisiesto(a):
            dias = dias + 366
        else:
            dias = dias + 365
    for m in range(1, hora_local.tm_mon):
        dias = dias + calcular_dias_mes(m, anio_bisiesto(hora_local.tm_year))
    dias = dias + hora_local.tm_mday
    return dias