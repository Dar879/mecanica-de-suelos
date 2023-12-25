"""Esta funcion almacena las propiedades fisicas del solido 
"""
def ingreso_datos():
    datos=[]
    for i in ["Volumen de aire en m3: ","Volumen de agua en m3: ","Volumen de solidos en m3: ",
              "Volumend de vacios en m3: ","Peso de aire en kg: ","Peso de agua en kg: ",
              "Peso de solidos en kg: ","Peso tota en kg: ","Volumen total en m: "]:
        try: 
            datos.append(float(input("Ingrese el valor de {}".format(i))))
        except ValueError:
            datos.append(None)
            
    return list(datos)


def prop_fisicas(vol_aire=None,vol_agua=None,vol_solid=None,
                 vol_vacio=None,peso_aire=None,peso_agua=None,
                 peso_solid=None,peso_total=None,vol_total=None):
    Va=vol_aire
    Vw=vol_agua
    Vs=vol_solid
    Vv=vol_vacio
    Wa=peso_aire
    Ww=peso_agua
    Ws=peso_solid
    W=peso_total
    V=vol_total
    return [Va,Vw,Vs,Vv,Wa,Ww,Ws,W,V]

print(prop_fisicas(1.1,2,3,4,5,6,7,8,9))

def imprimir_datos(Va,Vw,Vs,Vv,Wa,Ww,Ws,W,V):
    print("\nLas propiedades fisicas del solido son:\n\n",
          "Volumen de aire    {} m3\n".format(Va),
          "Volumen de agua    {} m3\n".format(Vw),
          "Volumen de solidos {} m3\n".format(Vs),
          "Volumen de vacios  {} m3\n".format(Vv),
          "Peso del aire      {} kg\n".format(Wa),
          "Peso del agua      {} kg\n".format(Ww),
          "Peso de solidos    {} kg\n".format(Ws),
          "Peso de total      {} kg\n".format(W),
          "Volumen de total   {} kg\n".format(V))
    return 0

