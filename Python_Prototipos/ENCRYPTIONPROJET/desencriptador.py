#1 ler a chave do file

chave = ''
with open('chi.ch', 'rb') as file:
    chave = file.read()

#2 lendo o dado/ficheiro encriptado da variavel dado_encriptado

dado_encriptado = ''
with open('exemplar CV.txt', 'rb') as file:
    dado_encriptado = file.read()

#3 Desemcriptamos o dado/ficheiro com o metodo Fernet mas antes atribuimos a chave au metodo

from cryptography.fernet import Fernet
f = Fernet(chave)

#Desencriptando o ficheiro com_o metodo Fernet.decrypt dentro da variavel dedo_desencriptado que nos criamos
#tribuimos a variavel dado_encriptado como argumento ao metodo f.decrypt()

dado_desencriptado = f.decrypt((dado_encriptado))
print('Ficheiro Desencriptado com Sucesso\nAbaixo os ficheiro encriptado e desencriptados')
print('Ficheiro encriptado\n',dado_encriptado.decode())
print('Ficheiro desencriptado\n',dado_desencriptado.decode())