#1 Vamos gerar a chave simetrica o metodo Fernet.generate_key

from cryptography.fernet import  Fernet
chave = Fernet.generate_key()

#2 criamos um ficheiro chi.ch e atribuimos a variavel geradora de chaves Fernet.generate_key

with open('chi.ch', 'wb') as file:
    file.write(chave)