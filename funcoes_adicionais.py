import os
from crud import Crud

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def consulta_todos_os_cursos():
    db = Crud()
    sql = 'SELECT * FROM cursos;'
    db.cursor.execute(sql)
    registros = db.cursor.fetchall()
    for registro in registros:
        idcurso = registro[0]
        nome = registro[1]
        descricao = registro[2][:30]
        carga = registro[3]
        total_aulas = registro[4]
        ano = registro[5]
        print(f'{idcurso:<5}{nome:<20}{descricao:<35}{carga:<10}{total_aulas:<20}{ano:<5}')
    db.close()


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


def menu_cadastro():
    limpa_tela()
    print('=' * 30)
    print('CADASTRO DE CURSOS'.center(30))
    print('=' * 30)
    