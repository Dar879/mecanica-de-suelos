import tkinter as tk

def datos():
    try:
        vol_aire = float(vol_aire_label.get())
        vol_agua = float(vol_agua_label.get())
        vol_sol = float(vol_sol_label.get())
        vol_vv = float(vol_vv_label.get())
        pes_air = float(pes_air_label.get())
        pes_agua = float(pes_agua_label.get())
        pes_sol = float(pes_sol_label.get())
        pes_tot = float(pes_tot_label.get())
        vol_tot = float(vol_tot_label.get())
    except ValueError:
        result_label1.config(text="Ingresa valores numéricos válidos")

    pe_agua=1000
    Pe_m=pes_tot/vol_tot
    Pe_sol=pes_sol/vol_sol
    Sm=Pe_m/pe_agua
    Ss=Pe_sol/pe_agua
    
    valores= [Pe_m,Pe_sol,Sm,Ss]    
    relaciones=["Peso especifico de la masa del suelo                 :","Peso especifico de la fase solida del suelo          :",
                "Peso especifico relativo de la masa del suelo        :","Peso especifico relativo de la fase solida del suelo :"]
    print("\nLos valores son:\n")
    result_label1.config(text="{}{}".format(relaciones[0],valores[0]))
    result_label2.config(text="{}{}".format(relaciones[1],valores[1]))
    result_label3.config(text="{}{}".format(relaciones[2],valores[2]))
    result_label4.config(text="{}{}".format(relaciones[3],valores[3]))
       

    return 0


# Configuración de la interfaz
root = tk.Tk()
root.title("Calculadora de relaciones volumetricas y gravimetricas ")

# Widgets
vol_aire_label = tk.Label(root, text="Volumen de aire en m3: ")
vol_aire_label.pack()

vol_aire_label = tk.Entry(root)
vol_aire_label.pack()

vol_agua_label = tk.Label(root, text="Volumen de agua en m3: ")
vol_agua_label.pack()

vol_agua_label = tk.Entry(root)
vol_agua_label.pack()

vol_sol_label = tk.Label(root, text="Volumen de solidos en m3: ")
vol_sol_label.pack()

vol_sol_label = tk.Entry(root)
vol_sol_label.pack()

vol_vv_label = tk.Label(root, text="Volumend de vacios en m3: ")
vol_vv_label.pack()

vol_vv_label = tk.Entry(root)
vol_vv_label.pack()

pes_air_label = tk.Label(root, text="Peso de aire en kg: ")
pes_air_label.pack()

pes_air_label = tk.Entry(root)
pes_air_label.pack()

pes_agua_label = tk.Label(root, text="Peso de agua en kg: ")
pes_agua_label.pack()

pes_agua_label = tk.Entry(root)
pes_agua_label.pack()

pes_sol_label = tk.Label(root, text="Peso de solidos en kg: ")
pes_sol_label.pack()

pes_sol_label = tk.Entry(root)
pes_sol_label.pack()

pes_tot_label = tk.Label(root, text="Peso tota en kg: ")
pes_tot_label.pack()

pes_tot_label = tk.Entry(root)
pes_tot_label.pack()

vol_tot_label = tk.Label(root, text="Volumen total en m: ")
vol_tot_label.pack()

vol_tot_label = tk.Entry(root)
vol_tot_label.pack()

calculate_button = tk.Button(root, text="Calcular relaciones de peso y volumen", command=datos)
calculate_button.pack()

result_label1 = tk.Label(root, text="")
result_label1.pack()
result_label2 = tk.Label(root, text="")
result_label2.pack()
result_label3 = tk.Label(root, text="")
result_label3.pack()
result_label4 = tk.Label(root, text="")
result_label4.pack()


# Iniciar la aplicación
root.mainloop()
