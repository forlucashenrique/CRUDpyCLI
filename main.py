import funcoes_adicionais as fa
from crud import Crud


def run():
    
    db = Crud()
    while True:
        fa.limpa_tela()
        fa.menu_principal()
        opcao = int(input('Opção: '))
        if opcao == 1:
            fa.menu_cadastro()
            db.insert()
        elif opcao == 2:
            colunas = ['nome', 'descricao', 'carga', 'totaulas', 'ano']
            fa.menu_atualizar()
            idcurso = int(input('\nDigite o ID do curso que deseja atualizar: '))
            fa.menu_update()
            campo = str(input('Escolha um campo para alteração: '))
            if campo in '345':
                novo_valor = int(input('Novo valor: '))
            else:
                novo_valor = str(input('Novo valor: ')).capitalize().strip()
            campo = int(campo) - 1
            db.update(campo=colunas[campo], dado=novo_valor, idcurso=idcurso)


        elif opcao == 3:
            fa.menu_excluir()
            idcurso = int(input('\nDigite o ID do curso que deseja deletar: '))
            db.delete(idcurso)
        elif opcao == 4:
            while True:
                fa.menu_consulta()
                opcao_de_consulta = int(input('Opção: '))
                if opcao_de_consulta > 5 or opcao_de_consulta < 1:
                    print('Opção incorreta!')
                    input('Aperte ENTER para tentar novamente...')
                    continue

                db.select(opcao_de_consulta)
                break
        elif opcao == 5:
            break
    db.close()


if __name__ == '__main__':
    run()