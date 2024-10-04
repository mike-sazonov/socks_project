from django.test import TestCase
from .models import Socks


class TestSocksPage(TestCase):

    def setUp(self):
        Socks.objects.create(article='women_summer', name='жен_летний', price=1)
        Socks.objects.create(article='men_summer', name='муж_летний', price=1, gender='Мужской')
        Socks.objects.create(article='child_summer', name='дет_летний', price=1, gender='Детский')
        Socks.objects.create(article='unisex_summer', name='уни_летний', price=1, gender='Унисекс')
        Socks.objects.create(article='women_winter', name='жен_зимний', season='Зима', price=1)
        Socks.objects.create(article='men_winter', name='муж_зимний', season='Зима', price=1, gender='Мужской')
        Socks.objects.create(article='child_winter', name='дет_зимний', season='Зима', price=1, gender='Детский')
        Socks.objects.create(article='unisex_winter', name='уни_зимний', season='Зима', price=1, gender='Унисекс')

    def test_menu(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_delivery(self):
        response = self.client.get('/delivery/')
        self.assertEqual(response.status_code, 200)

    def test_contacts(self):
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)

    def test_catalog(self):
        response = self.client.get('/socks/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_filter_all_gender_all_season(self):
        response = self.client.get('/socks/?gender=Не+выбран')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode().count('class="card text-center shadow h-100"'), 8)

    def test_catalog_filter_all_gender_all_season_in_checkbox(self):
        response = self.client.get('/socks/?winter=on&summer=on&gender=Не+выбран')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode().count('class="card text-center shadow h-100"'), 8)

    def test_catalog_filter_all_gender_summer(self):
        response = self.client.get('/socks/?summer=on&gender=Не+выбран')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode().count('class="card text-center shadow h-100"'), 4)
        self.assertEqual(response.content.decode().count('летний'), 4)

    def test_catalog_filter_all_gender_winter(self):
        response = self.client.get('/socks/?winter=on&gender=Не+выбран')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode().count('class="card text-center shadow h-100"'), 4)
        self.assertEqual(response.content.decode().count('зимний'), 4)

    def test_catalog_filter_women_all_season(self):
        response = self.client.get('/socks/?gender=Женский')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode().count('class="card text-center shadow h-100"'), 2)
        self.assertEqual(response.content.decode().count('жен_летний'), 1)
        self.assertEqual(response.content.decode().count('жен_зимний'), 1)

    def test_catalog_filter_men_all_season(self):
        response = self.client.get('/socks/?gender=Мужской')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode().count('class="card text-center shadow h-100"'), 2)
        self.assertEqual(response.content.decode().count('муж_летний'), 1)
        self.assertEqual(response.content.decode().count('муж_зимний'), 1)

    def test_catalog_filter_child_all_season(self):
        response = self.client.get('/socks/?gender=Детский')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode().count('class="card text-center shadow h-100"'), 2)
        self.assertEqual(response.content.decode().count('дет_летний'), 1)
        self.assertEqual(response.content.decode().count('дет_зимний'), 1)

    def test_catalog_filter_unisex_all_season(self):
        response = self.client.get('/socks/?gender=Унисекс')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode().count('class="card text-center shadow h-100"'), 2)
        self.assertEqual(response.content.decode().count('уни_летний'), 1)
        self.assertEqual(response.content.decode().count('уни_зимний'), 1)

    def test_catalog_filter_women_summer(self):
        response = self.client.get('/socks/?summer=on&gender=Женский')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode().count('class="card text-center shadow h-100"'), 1)
        self.assertEqual(response.content.decode().count('жен_летний'), 1)

    def test_catalog_filter_men_summer(self):
        response = self.client.get('/socks/?summer=on&gender=Мужской')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode().count('class="card text-center shadow h-100"'), 1)
        self.assertEqual(response.content.decode().count('муж_летний'), 1)

    def test_catalog_filter_child_summer(self):
        response = self.client.get('/socks/?summer=on&gender=Детский')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode().count('class="card text-center shadow h-100"'), 1)
        self.assertEqual(response.content.decode().count('дет_летний'), 1)

    def test_catalog_filter_unisex_summer(self):
        response = self.client.get('/socks/?summer=on&gender=Унисекс')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode().count('class="card text-center shadow h-100"'), 1)
        self.assertEqual(response.content.decode().count('уни_летний'), 1)

    def test_catalog_filter_women_winter(self):
        response = self.client.get('/socks/?winter=on&gender=Женский')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode().count('class="card text-center shadow h-100"'), 1)
        self.assertEqual(response.content.decode().count('жен_зимний'), 1)

    def test_catalog_filter_men_winter(self):
        response = self.client.get('/socks/?winter=on&gender=Мужской')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode().count('class="card text-center shadow h-100"'), 1)
        self.assertEqual(response.content.decode().count('муж_зимний'), 1)

    def test_catalog_filter_child_winter(self):
        response = self.client.get('/socks/?winter=on&gender=Детский')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode().count('class="card text-center shadow h-100"'), 1)
        self.assertEqual(response.content.decode().count('дет_зимний'), 1)

    def test_catalog_filter_unisex_winter(self):
        response = self.client.get('/socks/?winter=on&gender=Унисекс')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode().count('class="card text-center shadow h-100"'), 1)
        self.assertEqual(response.content.decode().count('уни_зимний'), 1)


class SocksModelTestCase(TestCase):

    def setUp(self):
        self.sock = Socks.objects.create(article='test', price=1)
        Socks.objects.create(article='new_sock', price=2)
        Socks.objects.create(article='sock', price=3)

    def test_socks_creation(self):
        self.assertEqual(self.sock.name, 'Носки')

    def test_socks_str(self):
        self.assertEqual(str(self.sock), 'test Женский 1')

    def test_socks_count(self):
        self.assertEqual(Socks.objects.count(), 3)

