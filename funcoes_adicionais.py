import os
from crud import Crud

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_de_cabecalho():
    limpa_tela()
    print(f'{"Id":<5}', end='')
    print(f'{"Nome":<20}', end='')
    print(f'{"Descrição":<35}', end='')
    print(f'{"Carga":<10}', end='')
    print(f'{"Total de Aulas":<20}', end='')
    print(f'{"Ano":<5}')
    print('=' * 100)


def menu_principal():
    print('=' * 30)
    print('GERENCIAMENTO DE CURSOS'.center(30))
    print('=' * 30)

    print("""
CADASTRAR -> [1]
ATUALIZAR -> [2]
DELETAR   -> [3]
CONSULTAR -> [4]
SAIR      -> [5]
    """)


def menu_consulta():
    limpa_tela()
    print('=' * 30)
    print('CONSULTA DE CURSOS'.center(30))
    print('=' * 30)

    print('[1] ->  Por ID')
    print('[2] ->  Por Nome')
    print('[3] ->  Por Descrição')
    print('[4] ->  Por Ano')
    print('[5] ->  CONSULTAR TODOS')
    print()    

def menu_update():
    limpa_tela()
    print('=' * 30)
    print('ATUALIZAÇÃO DE CURSOS'.center(30))
    print('=' * 30)

    print('[1] -> NOME')
    print('[2] -> DESCRIÇÃO')
    print('[3] -> CARGA HORÁRIA')
    print('[4] -> TOTAL DE AULAS')
    print('[5] -> ANO')
    print()

def menu_cadastro():
    limpa_tela()
    print('=' * 30)
    print('CADASTRO DE CURSOS'.center(30))
    print('=' * 30)


def menu_excluir():
    limpa_tela()
    print('=' * 50)
    print('EXCLUSÃO DE CURSOS'.center(50))
    print('=' * 50)


def menu_atualizar():
    limpa_tela()
    print('=' * 50)
    print('ATUALIZAÇÃO DE CURSOS'.center(50))
    print('=' * 50)