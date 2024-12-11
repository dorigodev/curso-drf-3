from django.test import TestCase
from escola.models import Estudante
from escola.models import Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']
    
    def test_carregamento_da_fixtures(self):
        estudante = Estudante.objects.get(cpf='89001648053')
        curso = Curso.objects.get(pk=1)
        self.assertEqual(estudante.celular, '29 96654-9200')
        self.assertEqual(curso.codigo, 'CPOO1')
