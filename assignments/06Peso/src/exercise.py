def main():
    #escribe tu código abajo de esta línea
    pesoInicial = float(input("Dame el peso inicial: "))
    pesoFinal = float(input("Dame el peso final: "))
    meses = float(input("Dame la cantidad de meses: "))
    porMes = (pesoInicial - pesoFinal) / meses
    print("Lo que debes bajar por mes es:", porMes)






if __name__ == '__main__':
    main()
