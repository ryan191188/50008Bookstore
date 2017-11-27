from django.test import TestCase

from .db import sql, page


class SQLTestCase(TestCase):
    fixtures = ('users.json',)

    users = (
        (1, 'admin'),
        (2, 'staff'),
        (3, 'test1'),
        (4, 'test2'),
        (5, 'test3'),
    )

    def test_single(self):
        result = sql('SELECT id FROM auth_user')
        self.assertEqual(result, tuple((d[0],) for d in self.users))

    def test_multi(self):
        result = sql('SELECT id, username FROM auth_user')
        self.assertEqual(result, self.users)

    def test_empty(self):
        result = sql('SELECT id FROM auth_user WHERE id = 0')
        self.assertEqual(result, ())

    def test_aggregate(self):
        result = sql('SELECT MAX(is_superuser) FROM auth_user')
        self.assertEqual(result, ((1,),))

    def test_param(self):
        result = sql('SELECT username FROM auth_user WHERE id = %s', 1)
        self.assertEqual(result, (('admin',),))

    def test_insert(self):
        q = """INSERT INTO auth_user (id, is_superuser, is_staff, is_active,
                date_joined, username, password, email, first_name, last_name)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        result = sql(q, 6, 0, 0, 1, '2017-11-11', 'test4', '', '', '', '')
        self.assertEqual(result, ())


class SQLPageTestCase(TestCase):

    def test_page_default(self):
        result = page()
        self.assertEqual(result, ' LIMIT 20 OFFSET 0')

    def test_page_three(self):
        result = page(page=3)
        self.assertEqual(result, ' LIMIT 20 OFFSET 40')

    def test_page_unlimited(self):
        result = page(per_page=0)
        self.assertEqual(result, '')

    def test_page_sort(self):
        result = page(per_page=0, sort=('id',))
        self.assertEqual(result, ' ORDER BY id')

    def test_page_sort_reverse(self):
        result = page(per_page=0, sort=('-id',))
        self.assertEqual(result, ' ORDER BY id DESC')

    def test_page_sort_multiple(self):
        result = page(per_page=0, sort=('id', 'a', 'b'))
        self.assertEqual(result, ' ORDER BY id, a, b')

    def test_page_sort_multiple_with_reverse(self):
        result = page(per_page=0, sort=('id', '-a'))
        self.assertEqual(result, ' ORDER BY id, a DESC')

    def test_page_sort_default(self):
        result = page(sort=('id',))
        self.assertEqual(result, ' ORDER BY id LIMIT 20 OFFSET 0')
