
#Relaciones peso volumen

def rel_peso_vol(Va,Vw,Vs,Vv,Wa,Ww,Ws,W,V):
    pe_agua=1000
    Pe_m=W/V
    Pe_sol=Ws/Vs
    Sm=Pe_m/pe_agua
    Ss=Pe_sol/pe_agua
    return [Pe_m,Pe_sol,Sm,Ss]

def imp_rel_peso_vol(valores):
    relaciones=["Peso especifico de la masa del suelo                 :","Peso especifico de la fase solida del suelo          :",
                "Peso especifico relativo de la masa del suelo        :","Peso especifico relativo de la fase solida del suelo :"]
    print("\nLos valores son:\n")
    for i in range(4):
        print("{}{}".format(relaciones[i],valores[i]))
    return 0

