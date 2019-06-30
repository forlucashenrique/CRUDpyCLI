import pymysql
import funcoes_adicionais as fa


class Crud:

    def __init__(self):
        self.db = pymysql.connect('localhost', 'boson-mysql', 'mysql', 'cadastro')
        self.cursor = self.db.cursor()
    
    def close(self):
        self.db.close()

    def select(self, opcao):
        if opcao == 1:
            idcurso = int(input('Informe o ID do curso: '))
            sql = f'SELECT * FROM cursos WHERE idcurso = {idcurso}'
        elif opcao == 2:
            nome = str(input('Informe o nome do curso: '))
            sql = f"SELECT * FROM cursos WHERE nome LIKE '{nome}%'"
        elif opcao == 3:
            descricao = str(input('Descrição do curso: '))
            sql = f"SELECT * FROM cursos WHERE descricao like '{descricao}%'"
        elif opcao == 4:
            ano = int(input('Informe o ano: '))
            sql = f'SELECT * FROM cursos WHERE ano = {ano}'
        elif opcao == 5:
            sql = 'SELECT * FROM cursos;'

        fa.menu_de_cabecalho()
        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()
            for registro in registros:
                idcurso = registro[0]
                nome = registro[1]
                descricao = registro[2][:30]
                carga = registro[3]
                total_aulas = registro[4]
                ano = registro[5]
                print(f'{idcurso:<5}{nome:<20}{descricao:<35}{carga:<10}{total_aulas:<20}{ano:<5}')
        except:
            print('Alguma coisa deu errado')
        input("\nAperte ENTER para continuar...")


    def insert(self):
        idcurso = int(self.consulta_id_curso()[-1][0]) + 1
        nome = str(input('Nome do curso: ')).capitalize().strip()
        descricao = str(input('Descrição: ')).capitalize().strip()
        carga = int(input('Carga horária: '))
        totaulas = int(input('Total de aulas: '))
        ano = int(input('Ano de criação: '))

        sql = f"""
            INSERT INTO cursos (idcurso, nome, descricao, carga, totaulas, ano)
            VALUES ({idcurso}, '{nome}', '{descricao}', {carga}, {totaulas}, {ano});
        """
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
    
    def update(self, campo, dado, idcurso):
        sql = f"""
            UPDATE cursos SET {campo} = '{dado}' WHERE idcurso = {idcurso};
        """
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
    
    def delete(self, idcurso):

        fa.consulta_todos_os_cursos()
        sql = f"""
            DELETE FROM cursos WHERE idcurso = {idcurso};
        """
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print('Curso apagado com sucesso!')
        except:
            self.db.rollback()
        

    def consulta_id_curso(self):
        sql = 'SELECT idcurso FROM cursos ORDER BY idcurso' # retorna o último registro 

        self.cursor.execute(sql)
        resultados = self.cursor.fetchall()
        return resultados

    

