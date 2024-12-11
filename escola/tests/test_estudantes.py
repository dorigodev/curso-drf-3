from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        #self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.usuario = User.objects.get(username = 'admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante_01 = Estudante.objects.get(pk=2)
        self.estudante_01 = Estudante.objects.get(pk=2)

        # self.estudante_01 = Estudante.objects.create(
        #     # nome='Teste de Estudante 1',
        #     # email='test1@email.com',
        #     # cpf='08324665811',
        #     # data_nascimento='2023-01-01',
        #     # celular='11 99999-9999'
        # )
        # self.estudante_02 = Estudante.objects.create(
        #     nome='Teste de Estudante 2',
        #     email='test2@email.com',
        #     cpf='62333546093',
        #     data_nascimento='2023-02-02',
        #     celular='11 11111-1111'
        # )
        
    def test_requisicao_get_para_listar_estudante(self):
        """ teste requisição GET
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
            
    def test_requisicao_get_para_listar_um_estudante(self):
        """ teste requisição GET para um estudante
        """
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(instance = dados_estudante).data
        self.assertEqual(response.data, dados_estudante_serializados)
        
    def test_requisicao_post_para_criar_um_estudante(self):
        dados = {
            'nome':'Teste',
            'email':'teste@email.com',
            'cpf':'88477573042',
            'data_nascimento':'2023-05-05',
            'celular':'11 55555-1111'
        }

        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_requisicao_delete_um_estudante(self):
        """Teste de requisição DELETE"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_requisicao_put_um_estudante(self):
        """Teste de requisição PUT para um estudante"""
        dados = {
            'nome':'teste',
            'email':'testeput@gmail.com',
            'cpf':'42370866071',
            'data_nascimento':'2003-05-09',
            'celular':'11 88888-6666'
        }
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

