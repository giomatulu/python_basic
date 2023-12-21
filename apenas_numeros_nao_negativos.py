def insereNumeroPositivo():
    numeroInserido = float(input("\n\nInsira um número não-negativo de sua escolha:"))
            
    while numeroInserido > 0:
        print("O número não-negativo inserido foi: " + str(numeroInserido))
        insereNumeroPositivo()
    else:
        print("ERRO: NÚMERO NEGATIVO INSERIDO. POR GENTILEZA INSERIR NUMERO NÃO NEGATIVO. ")
        exit()
        
insereNumeroPositivo()