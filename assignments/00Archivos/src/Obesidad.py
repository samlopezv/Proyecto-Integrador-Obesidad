from matplotlib import pyplot as plt
from matplotlib import numpy as np
from tabulate import tabulate

def sobrepeso_america(num):
    paises=[]
    sexes=[]
    male=[]
    porcentajemale=[]
    porcentaje = 0
    female=[]
    porcentajefemale=[]
    dato=[]
    matriz=[]
    tabla=[]

    with open ('/workspace/Proyecto-Integrador-Obesidad/assignments/00Archivos/data/Sobrepeso en América 2016.csv', 'r') as america:
       #Matrices para cada colmna
        for line in america:
            dato = line.split(',')
            paises.append(dato[0])
            sexes.append(dato[1])
            male.append(dato[2])
            female.append(dato[3])

    #Quitar los títulos de las matrices
    paises.pop(0)
    sexes.pop(0)
    male.pop(0)
    female.pop(0)

    #Operaciones de porcentajes entre las matrices
    for i in range (len(sexes)):
        porcentaje = ( float(male[i]) * float(sexes[i])) / ( float(male[i]) + float(female[i]))
        porcentajemale.append(porcentaje)
        porcentaje = ( float(female[i]) * float(sexes[i])) / ( float(male[i]) + float(female[i]))
        porcentajefemale.append(porcentaje)

    print('\n')
    print('Sobrepeso en países de América en 2016')
    print('\n')
    print('A continuación se muestran los países con sus respectivos porcentajes')
    print('\n')

    #Tabla
    for i in range (len(paises)):
        matriz.append (paises[i])
        matriz.append (str(round(float(sexes[i]))))
        matriz.append (str(round(porcentajemale[i])))
        matriz.append (str(round(porcentajefemale[i])))
        tabla.append(matriz)
        matriz=[]
    print (tabulate(tabla, headers=['País', 'Porcentaje ambos sexos %', 'Porcentaje hombres %', 'Porcentaje mujeres %']))
    
    print('\n')
    print('Ahora representaremos estos datos en la siguiente gráfica')
    #Código para la gráfica
    indice = np.arange(len(paises))
 
    #Creación de barras
    plt.bar(indice, porcentajemale, label='Hombres')
    plt.bar(indice, porcentajefemale, label='Mujeres',  bottom=porcentajemale)
 
    plt.xticks(indice, paises)
    plt.ylabel("Porcentaje")
    plt.xlabel("Paises")
    plt.title('Sobrepeso en América 2016')
    plt.legend()
    plt.savefig('grafico_america.png') 
    plt.show()

    #Regresar al menú
    print('\n')
    print('Volver al menú Enter')
    enter = input()
    print('IMC= 1     Gráficax=2    Sobrepeso en América 2016=3      Salir=4')
    numnuevo = int(input())
    return(numnuevo)

def grafica_mexico(num):


    print('\n')
    print('Volver al menú Enter')
    enter = input()
    print('IMC= 1     Gráficax=2    Sobrepeso en América 2016=3      Salir=4')
    numnuevo = int(input())
    return(numnuevo)
    return()

    

def imc(nombre, num):
    #Pide datos para calcular el IMC
    print('\n')
    print('Calculadora de IMC')
    peso = float(input('Ingresa tu peso en kg: '))
    estatura = float(input('Ingresa tu estatura en metros: '))
    imc = round(peso/ estatura**2,1)
    print(f'{nombre} tu IMC es de {imc}')

    #Tipos de peso
    if imc < 18.5 :
        a=[]
        print('Lo que significa que tienes un bajo peso')
        print('\n')
        print ("Te arrojaremos unas ciertas recomendaciones de la nutriologa Claudia Villalobos: ")
        print ('1-. Intenta aumentar tu masa muscular para ellos requires aumentar tu indice calórico')
        print ('Para esto, aumenta tu ingesta de carbohidratos y proteinas')
        print ('2-. Realiza actividad física con peso y realiza cardio pero no excesivo')
        print ('3-. Asesorate con tu nutriolog@ para que se enfoque en tu caso')
        print ('Nota:')
        print ('Recuerda que tu IMC no simboliza al 100% tu estado de salud, ya que depende mucho tus metas a llegar')
        print('Por lo que lo mas recomendable es medirse y asistir con el o la nutriolog@')

    elif imc < 25:
        print('Lo que significa que tienes un peso saludable')
        print ("Te arrojaremos unas ciertas recomendaciones de la nutriologa Claudia Villalobos: ")
        print ('Sigue asi! Manten tu dieta equilbada y balanceada, realiza minimamente 30 minutos de actividad física diaria')
        print ('En caso de dudas específicas consulta con tu nutriolog@')
        print ('Nota:')
        print ('Recuerda que tu IMC no simboliza al 100% tu estado de salud, ya que depende mucho tus metas a llegar')
        print('Por lo que lo mas recomendable es medirse y asistir con el o la nutriolog@')

    elif imc < 30:
        print('Lo que significa que tienes sobrepeso')
        print ('No te alarmes, es totalmente manejable :)')
        print ("Te arrojaremos unas ciertas recomendaciones de la nutriologa Claudia Villalobos: ")
        print ('1-. Evita comidad fritas y con exceso de harina')
        print ('2-. Evade grasas saturadas')
        print ('3-. Busca cambiar to comida diaria por aliemntos mas sanos. EJEMPLO: ')
        print ('TORTILLAS DE NOPAL, HARINA DE AVENA, ENDULZANTES ARTIFICIALES, ETC')
        print ('4-. Realiza actividad física minimamente 45 minutos diarios')
        print ('5-. Agrega a tu día a día frutas y verduras, proteínas y grasas saludables.')
        print ('6-. Recuerda que todo en exceso es dañino asi que mante un control de tu ingesta calórica')
        print ('En caso de dudas específicas consulta con tu nutriolog@')
        print ('Nota:')
        print ('Recuerda que tu IMC no simboliza al 100% tu estado de salud, ya que depende mucho tus metas a llegar')
        print('Por lo que lo mas recomendable es medirse y asistir con el o la nutriolog@')

    elif imc < 35:
        print('Lo que significa que tienes obesidad I')
        print ('En estos casos, se recomienda ir de urgencia con un especilsta')
        print ('De esta manera se otorga un buen diagóstico y se trata respectivo caso')
        print ("Te arrojaremos unas ciertas recomendaciones de la nutriologa Claudia Villalobos: ")
        print ('Por nuestra parte, lo mas conveniente es: ')
        print ('1-. Indicarle ir al nutriólogo')
        print ('2-. Dismunir el indice calórico')
        print ('3-. Busca cambiar to comida diaria por aliemntos mas sanos. EJEMPLO: ')
        print ('TORTILLAS DE NOPAL, HARINA DE AVENA, ENDULZANTES ARTIFICIALES, ETC')
        print ('4-. Comprar la despensa de su casa junto a un especialista')
        print ('5-. Realizar actividad física e ir aumentando la intensidad progresivamente ')
        print ('6-. Si esta en sus posibilidades aplicar por una cirugía inidcada por el especialta, tomarla')
        print ('7-. Seguir todas las recomendaciones dadas y las de su nutriologo')
        print ('8-. Agrega a tu día a día frutas y verduras, proteínas y grasas saludables.')
        print ('9-. Recuerda que todo en exceso es dañino asi que mante un control de tu ingesta calórica')
        print ('En caso de dudas específicas consulta con tu nutriolog@')
        print ('Nota:')
        print ('Recuerda que tu IMC no simboliza al 100% tu estado de salud, ya que depende mucho tus metas a llegar')
        print ('Por lo que lo mas recomendable es medirse y asistir con el o la nutriolog@')

    elif imc < 40:
        print('Lo que significa que tienes obesidad II')
        print ('En estos casos, se recomienda ir de urgencia con un especilsta')
        print ('De esta manera se otorga un buen diagóstico y se trata respectivo caso')
        print ("Te arrojaremos unas ciertas recomendaciones de la nutriologa Claudia Villalobos: ")
        print ('Por nuestra parte, lo mas conveniente es: ')
        print ('1-. Indicarle ir al nutriólogo')
        print ('2-. Dismunir el indice calórico')
        print ('3-. Busca cambiar to comida diaria por aliemntos mas sanos. EJEMPLO: ')
        print ('TORTILLAS DE NOPAL, HARINA DE AVENA, ENDULZANTES ARTIFICIALES, ETC')
        print ('4-. Comprar la despensa de su casa junto a un especialista')
        print ('5-. Realizar actividad física e ir aumentando la intensidad progresivamente ')
        print ('6-. Si esta en sus posibilidades aplicar por una cirugía inidcada por el especialta, tomarla')
        print ('7-. Seguir todas las recomendaciones dadas y las de su nutriologo')
        print ('8-. Agrega a tu día a día frutas y verduras, proteínas y grasas saludables.')
        print ('9-. Recuerda que todo en exceso es dañino asi que mante un control de tu ingesta calórica')
        print ('En caso de dudas específicas consulta con tu nutriolog@')
        print ('Nota:')
        print ('Recuerda que tu IMC no simboliza al 100% tu estado de salud, ya que depende mucho tus metas a llegar')
        print ('Por lo que lo mas recomendable es medirse y asistir con el o la nutriolog@')

    elif imc < 50:
        print('Lo que significa que tienes obesidad III')
        print ('En estos casos, se recomienda ir de urgencia con un especilsta')
        print ('De esta manera se otorga un buen diagóstico y se trata respectivo caso')
        print ("Te arrojaremos unas ciertas recomendaciones de la nutriologa Claudia Villalobos: ")
        print ('Por nuestra parte, lo mas conveniente es: ')
        print ('1-. Indicarle ir al nutriólogo')
        print ('2-. Dismunir el indice calórico')
        print ('3-. Busca cambiar to comida diaria por aliemntos mas sanos. EJEMPLO: ')
        print ('TORTILLAS DE NOPAL, HARINA DE AVENA, ENDULZANTES ARTIFICIALES, ETC')
        print ('4-. Comprar la despensa de su casa junto a un especialista')
        print ('5-. Realizar actividad física e ir aumentando la intensidad progresivamente ')
        print ('6-. Si esta en sus posibilidades aplicar por una cirugía inidcada por el especialta, tomarla')
        print ('7-. Seguir todas las recomendaciones dadas y las de su nutriologo')
        print ('8-. Agrega a tu día a día frutas y verduras, proteínas y grasas saludables.')
        print ('9-. Recuerda que todo en exceso es dañino asi que mante un control de tu ingesta calórica')
        print ('En caso de dudas específicas consulta con tu nutriolog@')
        print ('Nota:')
        print ('Recuerda que tu IMC no simboliza al 100% tu estado de salud, ya que depende mucho tus metas a llegar')
        print ('Por lo que lo mas recomendable es medirse y asistir con el o la nutriolog@')
    else:
        print('Lo que significa que tienes obesidad IV')
        print ('En estos casos, se recomienda ir de urgencia con un especilsta')
        print ('De esta manera se otorga un buen diagóstico y se trata respectivo caso')
        print ("Te arrojaremos unas ciertas recomendaciones de la nutriologa Claudia Villalobos: ")
        print ('Por nuestra parte, lo mas conveniente es: ')
        print ('1-. Indicarle ir al nutriólogo')
        print ('2-. Dismunir el indice calórico')
        print ('3-. Busca cambiar to comida diaria por aliemntos mas sanos. EJEMPLO: ')
        print ('TORTILLAS DE NOPAL, HARINA DE AVENA, ENDULZANTES ARTIFICIALES, ETC')
        print ('4-. Comprar la despensa de su casa junto a un especialista')
        print ('5-. Realizar actividad física e ir aumentando la intensidad progresivamente ')
        print ('6-. Si esta en sus posibilidades aplicar por una cirugía inidcada por el especialta, tomarla')
        print ('7-. Seguir todas las recomendaciones dadas y las de su nutriologo')
        print ('8-. Agrega a tu día a día frutas y verduras, proteínas y grasas saludables.')
        print ('9-. Recuerda que todo en exceso es dañino asi que mante un control de tu ingesta calórica')
        print ('En caso de dudas específicas consulta con tu nutriolog@')
        print ('Nota:')
        print ('Recuerda que tu IMC no simboliza al 100% tu estado de salud, ya que depende mucho tus metas a llegar')
        print ('Por lo que lo mas recomendable es medirse y asistir con el o la nutriolog@')
    print('\n')
    print('Volver al menú Enter')
    enter = input()
    print('IMC= 1     Gráficax=2    Sobrepeso en América 2016=3      Salir=4')
    numnuevo = int(input())
    return(nombre, numnuevo)


def main():
    #Ingreso al código
    nombre = (input('Ingresa tu nombre: '))
    print('\n')
    print(f'¡Hola {nombre}! ¿qué deseas conocer?')
    print('IMC= 1     Gráficax=2        Sobrepeso en América 2016=3    Salir=4')
    num = int(input())

    #Para que se pueda escojer a dónde ir
    while num != 4:
        if num == 1:
            variableimc = imc(nombre, num)
            num = variableimc[1]
        elif num == 2:
            g = grafica_mexico(num)
            num = g
        elif num == 3:
            g = sobrepeso_america(num)
            num = g
        else:
            print('Favor de ingresar un dato válido')
            num = int(input())
            if num != 1 or num !=2 or num !=3 or num != 4:
                num = num
            else:
                num = 5
            while num == 5:
                print('Favor de ingresar un dato válido')
                num = int(input())
                
    print('\n')   
    print('Gracias por tu visita')



if __name__=='__main__':
    main()
