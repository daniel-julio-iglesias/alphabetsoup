#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Run the entire test suite with
# the following command
# (venv) $ python tests.py
from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User
from app.mainapp import MainApp


class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))


class MainAppCase(unittest.TestCase):
    def test_has_message(self):
        message = "Hello, World!"
        letters = 'startHelloWorldfoospamh'
        cooking = MainApp(message, letters)
        self.assertTrue(cooking.has_message())

if __name__ == '__main__':
    unittest.main(verbosity=2)
