def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

def peso_ideal(altura, imc_desejado_min=18.5, imc_desejado_max=24.9):
    peso_minimo = imc_desejado_min * (altura ** 2)
    peso_maximo = imc_desejado_max * (altura ** 2)
    return round(peso_minimo, 2), round(peso_maximo, 2)

def obter_input_numerico(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
            else:
                return valor
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

def main():
    nome = input("Digite seu nome: ").capitalize()
    
    while True:
        print(f"\nCalculadora de IMC - Bem-vindo(a), {nome}!")
        
        peso = obter_input_numerico(f"{nome}, digite o seu peso (kg): ")
        altura = obter_input_numerico(f"{nome}, digite a sua altura (m): ")
        
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        
        print(f"\n{nome}, o seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
        
        peso_minimo, peso_maximo = peso_ideal(altura)
        print(f"Para a sua altura de {altura:.2f}m, o peso ideal está entre {peso_minimo:.2f}kg e {peso_maximo:.2f}kg.")
        
        continuar = input("\nDeseja calcular outro IMC? (s/n): ").lower()
        if continuar != 's':
            print(f"Saindo da calculadora. Até logo, {nome}!")
            break

if __name__ == "__main__":
    main()
