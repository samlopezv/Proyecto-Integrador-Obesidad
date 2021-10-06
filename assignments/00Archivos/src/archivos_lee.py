def mostrar_nombres():
    nombres, ap_pats, ap_mats = leer_datos()
    
    print("Datos del archivo")
    print("-----------------")

    c = 1
    for nombre, ap_pat, ap_mat in zip(nombres, ap_pats, ap_mats):
        print("Alumno " + str(c) + "->"+ nombre + " " + ap_pat + " " + ap_mat)
        c += 1
    print("Listo ! Presiona <Enter> para terminar ....")
    input()

def leer_datos():

    nombres=[]
    ap_pats=[]
    ap_mats=[]

    print("Leyendo datos ...")
    print("------------------")

    with open('/workspace/ej-Archivos/assignments/00Archivos/data/personas.csv', 'r') as f:  
        for line in f:
            print("Leyendo..."+line)

            lista_line = line.split(",")
            
            nombres.append(lista_line[0])
            ap_pats.append(lista_line[1])
            ap_mats.append(lista_line[2])

    print("Todos los nombres=", nombres)
    print("Todos los apellidos paternos=", ap_pats)
    print("Todos los apellidos maternos=", ap_mats)

    print("Mostrando los datos como matriz:")
    print("================================")

    matriz_personas=[]
    total_personas=len(nombres)

    for renglon in range(total_personas):
        lista_persona=[nombres[renglon], ap_pats[renglon], ap_mats[renglon]]
        matriz_personas.append(lista_persona)
    
    print(matriz_personas)

    print("Fin de la lectura, presiona <Enter> para mostrar los datos ...")
    input()
    
    return nombres, ap_pats, ap_mats

def main():
    mostrar_nombres()

if __name__=='__main__':
    main()