print("""
██████╗░██╗███████╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗██╗██████╗░░█████╗░
██╔══██╗██║██╔════╝████╗░██║██║░░░██║██╔════╝████╗░██║██║██╔══██╗██╔══██╗
██████╦╝██║█████╗░░██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║██║██║░░██║██║░░██║
██╔══██╗██║██╔══╝░░██║╚████║░╚████╔╝░██╔══╝░░██║╚████║██║██║░░██║██║░░██║
██████╦╝██║███████╗██║░╚███║░░╚██╔╝░░███████╗██║░╚███║██║██████╔╝╚█████╔╝
╚═════╝░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝╚═════╝░░╚════╝░""")




opcion=0
def menu():
    opcion_menu= int(input("╔═══════════════════════════════╗ \n"+
                        "║ 𝔐𝔢𝔫𝔲́                             ║ \n"+ 
                        "║                                  ║ \n"+
                        "║ 1) variaciones ordinarias        ║ \n"+
                        "║ 2) variaciones con repeticion    ║ \n"+
                        "║ 3) Permutacion ordinaria         ║ \n"+
                        "║ 4) Permutacion con repeticion    ║ \n"+
                        "║ 5) Combinacion Ordinaria         ║ \n"+
                        "║ 6) Combinacion con repeticion    ║ \n"+
                        "║ 0) Salir                         ║ \n"+
                        "║                                  ║ \n"+
                        "╚══════════════════════════════════╝ \n" ))
    return opcion_menu

def variacion_ordinaria():
    print ("aqui va operacion1  ")
def Variacion_con_Repeticion():
    print ("aqui va operacion 2 ")
def permutacion_Ordinaria():
    print ("aqui va operacion 3 ")
def permutacion_con_repeticion():
    print ("aqui va operacion 4 ")
def Convinacion_Ordinaria():
    print ("aqui va operacion 5  ")
def Convinacion_con_repeticion():
    print ("aqui va operacion 6 ")

while opcion != 6:
    opcion = menu()

    if opcion == 1:
        variacion_ordinaria()
    if opcion == 2:
        Variacion_con_Repeticion()
    if opcion == 3:
        permutacion_Ordinaria()
    if opcion == 4:
        permutacion_con_repeticion()
    if opcion == 5:
        Convinacion_Ordinaria()
    if opcion == 6:
        Convinacion_con_repeticion()
    if opcion == 0:
        break


