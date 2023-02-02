#Senha sem repetir caracteres
import random;
import string

for i in range(1):
        resultadoSTR = ''.join(random.sample(string.ascii_letters, 12))
        print("A senha aleatória sem repetir caracteres é:", resultadoSTR)