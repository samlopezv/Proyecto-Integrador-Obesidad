def lectura_nombres():
    nombres=[]
    ap_pats=[]
    ap_mats=[]

    for i in range(5):
        print("Lectura de nombres a grabar en archivo")
        print("--------------------------------------")
        print("Alumno->", i+1)

        nombre = input("Nombre:")
        ap_pat = input("Apellido Paterno:")
        ap_mat = input("Apellido Materno:")

        nombres.append(nombre)
        ap_pats.append(ap_pat)
        ap_mats.append(ap_mat)

    print("Todos los nombres=", nombres)
    print("Todos los apellidos paternos=", ap_pats)
    print("Todos los apellidos maternos=", ap_mats)

    return nombres, ap_pats, ap_mats

def grabar_datos():
    nombres, ap_pats, ap_mats = lectura_nombres()

    print("Grabando datos ...")
    print("------------------")

    print("Todos los nombres y apellidos con zip= ", list(zip(nombres, ap_pats, ap_mats)))

    with open('/workspace/ej-Archivos/assignments/00Archivos/data/personas.csv', 'w') as f:
        f.write("NOMBRE,APELLIDO PATERNO,APELLIDO MATERNO\n")  
        for nombre, ap_pat, ap_mat in zip(nombres, ap_pats, ap_mats):
            print("Grabando ..." + nombre+"," + ap_pat + "," + ap_mat)
            f.write(nombre+"," + ap_pat + "," + ap_mat + "\n")

def main():
    grabar_datos()

if __name__=='__main__':
    main()
