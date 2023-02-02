#Senha pode repetir caracteres
import random;
import string;

def geraString(lenght):
    #Função para gerar a senha aleatória
    resultadoStr = ''.join(random.choice(string.ascii_letters) for i in range(lenght))
    print("A senha aleatória com", lenght, "caracteres é:", resultadoStr)

#Define a quantidade de caracteres
geraString(14)


