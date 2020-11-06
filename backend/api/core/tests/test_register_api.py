from django.test import TestCase, Client

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
        response = request.post('/api/register/create',
        {
            'title':'2ª Frase efeito',
            'text':'Everybody has a plan until the first punch in the face'
        })

        self.assertEqual(200,response.status_code)

    