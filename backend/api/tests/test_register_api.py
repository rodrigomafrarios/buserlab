from django.test import TestCase, Client
from django.utils import timezone
import json

class RegisterTestCase(TestCase):
    def test_register_list(self):

        request = Client()
        response = request.get('/api/register/list',{},True)
        
        # assert status_code
        self.assertEqual(200,response.status_code)

        # assert content-type
        self.assertEqual(response['content-type'], 'application/json')
    
    def test_register_create(self):
        
        request = Client()

        #load object
        data = {'title':'2ª Frase efeito','text':'Everybody has a plan until the first punch in the face'}

        #insert
        response = request.post('/api/register/create/',data)
        
        #assert status_code 
        self.assertEqual(200, response.status_code)

        # assert content-type
        self.assertEqual(response['content-type'], 'application/json')
    
    def test_register_update(self):

        request = Client()

        #load object
        data = {
            'id':1,
            'title':'2ª Frase efeito',
            'text':'[UPDATE]Everybody has a plan until the first punch in the face'
        }
        
        #update
        response = request.post('/api/register/update/' + str(data['id']),data)
        
        #assert status_code 
        self.assertEqual(200, response.status_code)

        # assert content-type
        self.assertEqual(response['content-type'], 'application/json')

    def test_register_remove(self):
    
        request = Client()

        #load object
        data = {
            'id':1
        }
        
        #remove
        response = request.delete('/api/register/remove/' + str(data['id']))
        
        #assert status_code 
        self.assertEqual(200, response.status_code)

        # assert content-type
        self.assertEqual(response['content-type'], 'application/json')

    