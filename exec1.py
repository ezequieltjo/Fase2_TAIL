"""
    Exercício 1 - Fase 2
"""
lista = []

def create_list():
    print(f'Criando lista...')
    lista = []
    return lista


def check_empty():
    if len(lista) == 0:
        return print(f'Lista vazia.')
    else:
        return print(f'Lista contém dados.')


def append():
    lista.append(input())


def pop():
    print(f'{lista.pop(0)}')
    

create_list()
check_empty()

print(f'Digite as frases para adicionar a lista: ')

for n in range(5):    
    append()


print(f'OK! Printando...')

for n in range(5): 
    pop()



