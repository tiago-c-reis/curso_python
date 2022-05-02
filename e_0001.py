# Python - Exercícios do Curso de Python Completo para Iniciantes
#
# video: https://www.youtube.com/watch?v=GZoqIWX-v6k&list=PLCI9CZ6VUaFkB2mRRHue3z_xzqbAHtpHS
#
# code: 00001
#

nome = 'Marie Curie'

# (a) Indique o primeiro e último caracter
primeiro_caracter = nome[0]
ultimo_caracter = nome[-1]

print(f'{primeiro_caracter =  }')
print(f'{ultimo_caracter =  }')
print()     # criar uma linha vazia entre as respostas

# (b) Indique todos os caracteres de índice par
resposta = nome[::2]

print(f'{resposta = }')
print()

# (c) Revera a variável nome
resposta = nome[::-1]
print(f'{resposta = }')
print()

# (d) Faça a alteração de 'Marie Curie' para 'Pierre Curier'
resposta = nome.replace('Marie', 'Piere')
print(f'{resposta = }')
print()
