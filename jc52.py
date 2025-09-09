nome = input("digite seu nome  :")
peso= float(input("digite seu peso em quilograma:"))
altura=float(input("digite sua altura:"))

imc=peso/(altura*altura)


if imc<=18.5:
    print("abaixo do peso")
    
elif imc>=18.5 and imc <24.9:
    print("peso normal")

elif imc >=25.0 and imc<=29.9:
    print("sobrepeso")

elif imc >=30.0 and imc <=34.9:
    print("obesidade 1ºgrau")
     
elif imc>=35.0 and imc <=39.9:
    print("obesidade 2ºgrau")

elif imc >=40.0:
    print("obesidade 3ºgrau")
     
print(nome + 'tem imv igual a'+str(imc))