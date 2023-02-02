#Gerador de senhas fortes e unicas
import random
import string

def geraSenhaAleatoria():
    fonte_aleatoria = string.ascii_letters + string.digits + string.punctuation
    Senha = random.choice(string.ascii_lowercase)
    Senha += random.choice(string.ascii_uppercase)
    Senha += random.choice(string.digits)
    Senha += random.choice(string.punctuation)

    for i in range(6):
        Senha += random.choice(fonte_aleatoria)

    lista_senhas = list(Senha)
    random.SystemRandom().shuffle(lista_senhas)
    Senha = ''.join(lista_senhas)
    return Senha

print("A sua senha única e forte é:", geraSenhaAleatoria())
