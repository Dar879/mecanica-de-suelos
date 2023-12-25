from prop_fisicas import prop_fisicas,imprimir_datos,ingreso_datos
from rel_peso_volumen import imp_rel_peso_vol,rel_peso_vol



def emsamblador():
    datos=prop_fisicas(*ingreso_datos())
    imprimir_datos(*datos)
    imp_rel_peso_vol(rel_peso_vol(*datos))
    return 0

emsamblador()
