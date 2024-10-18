import pytest
from projeto import calcular_imc, classificar_imc
 
 #------TESTES DE SUCESSO------
@pytest.mark.parametrize("pessoa", [
    {"nome": "pessoa1", "peso": 50, "altura": 1.60, "imc": 19.53},  
    {"nome": "pessoa2", "peso": 70, "altura": 1.75, "imc": 22.86},  
    {"nome": "pessoa3", "peso": 80  , "altura": 1.70, "imc": 27.68},  
    {"nome": "pessoa4", "peso": 30  , "altura": 1.70, "imc": 10.38},  
    {"nome": "pessoa5", "peso": 90  , "altura": 1.70, "imc": 31.14},  
])
def test_calcular_imc_sucesso(pessoa):
    peso = pessoa["peso"]
    altura = pessoa["altura"]
    assert calcular_imc(peso,altura) == pessoa["imc"]
    if "Peso normal" in classificar_imc(pessoa["imc"]):
        assert classificar_imc(pessoa["imc"]) == "Peso normal"
    elif "Sobrepreso" in classificar_imc(pessoa["imc"]):
        assert classificar_imc(pessoa["imc"]) == "Sobrepeso"
    elif "Abaixo do peso" in classificar_imc(pessoa["imc"]):
        assert classificar_imc(pessoa["imc"]) == "Abaixo do peso"
    elif "Obesidade grau 1" in classificar_imc(pessoa["imc"]):
        assert classificar_imc(pessoa["imc"]) == "Obesidade grau 1"

#------TESTES DE FALHA------
@pytest.mark.parametrize("peso, altura", [
    (85, 0),       # Altura zero
])
def test_calcular_imc_falha(peso, altura):
    with pytest.raises(ZeroDivisionError):
        calcular_imc(peso, altura)

@pytest.mark.parametrize("imc", [
    (-5),   # IMC negativo (inválido)
])
def test_classificar_imc_falha(imc):
    assert classificar_imc(imc) == "Abaixo do peso"
