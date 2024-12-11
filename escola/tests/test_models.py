from django.test import TestCase
from escola.models import Estudante
from escola.models import Curso
from escola.models import Matricula


class ModelEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome='Teste de Modelo',
            email='test@email.com',
            cpf='08324665811',
            data_nascimento='2023-02-02',
            celular='11 99999-9999'
        )
        
    def test_verifica_atributos_de_estudante(self):
        """ Teste que verifica os atributos do modelo de Estudante """
        self.assertEqual(self.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.estudante.email, 'test@email.com')
        self.assertEqual(self.estudante.cpf, '08324665811')
        self.assertEqual(self.estudante.data_nascimento, '2023-02-02')
        self.assertEqual(self.estudante.celular, '11 99999-9999')
        
        
class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'POO03',
            descricao = 'Terceiro curso de Programaçao Orientada a Objetos',
            nivel = 'I'
        )
    
    def test_verifica_atributos_de_cursos(self):
        self.assertEqual(self.curso.codigo, 'POO03')
        self.assertEqual(self.curso.descricao, 'Terceiro curso de Programaçao Orientada a Objetos')
        self.assertEqual(self.curso.nivel, 'I')
        
class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome = 'Teste Modelo Matricula',
            email='testemodelomatricula@gmail.com',
            cpf='91546870040',
            data_nascimento='2003-02-02',
            celular='86 99999-9999'
        )
        self.curso_matricula = Curso.objects.create(
            codigo='CTMM',descricao='Curso Teste Modelo Matricula',nivel='B'
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante_matricula,
            curso=self.curso_matricula,
            periodo='M'
        )
    
    def test_verifica_atributos_de_matricula(self):
        """Teste que verifica os atributos do modelo de Matricula"""
        self.assertEqual(self.matricula.estudante.nome, 'Teste Modelo Matricula')
        self.assertEqual(self.matricula.curso.descricao, 'Curso Teste Modelo Matricula')
        self.assertEqual(self.matricula.periodo, 'M')