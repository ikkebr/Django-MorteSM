from django.test import TestCase

class BaseTests(TestCase):
    def setUp(self):
        self.c = Client()
        
    def teste_raiz_retorna_200(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def teste_raiz_nomeada_index_retorna_200(self):
        response = self.c.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def teste_raiz_usa_template_base(self):
        response = self.c.get('/')
        self.assertTemplateUsed(response, "mapa.html")
