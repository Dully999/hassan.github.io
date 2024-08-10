#1 Leitura da chave que esta no ficheiro criado chi.ch que esta na variavel chave

chave = ''
with open('chi.ch', 'rb') as file:
    chave = file.read()
#2 Fazemos a litura do dado/ficheiro a encriptar

dado = ''
with open('exemplar CV.txt', 'rb') as file:
    dado = file.read()

#3 Encriptando o dado/ficheiro cim o metodo fernet.encript(dado)

from cryptography.fernet import Fernet

f = Fernet(chave)

dado_encriptado = f.encrypt(dado)

#4 Salvamos o dado/ficheiro encriptado em uma variavel dado_encriptado

with open('exemplar CV.txt', 'wb')as file:
    file.write(dado_encriptado)
    print('Ficheiro encriptado com sucesso \naqui esta o ficheiro:')
    print(dado_encriptado)