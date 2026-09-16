#Consumo de agua
# Felipe Stabile Martins


# apartamento
# casa 
# comercial

#Entrada
print( )
print ("Programa de calculo de consumo de agua")
print ( )

tipo_imovel = input("digitar o tipo (comercial, casa ou apartamento): ")

#Processamento

if tipo_imovel == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")
    print(  )
elif tipo_imovel == "apartamento" or tipo_imovel == "casa":
    consumo_mensal = float(input("Digite o consumo mensal de agua em m³: "))
    if tipo_imovel == "apartamento" and consumo_mensal < 10:
        print("Consumo econômico excelente controle de agua!")
    elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo_mensal <= 25:
        print("Consumo moderado dentro do padrão residencial")
    else:
        print("Consumo excessivo adote medidas de economia e verifique vazamentos.")
    print ( )
else: 
    print("Imovel desconhecido")
    print( )