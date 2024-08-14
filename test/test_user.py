import os
import unittest
from flask import current_app
from app import create_app, db
from app.models import User, UserData
from app.repositories import UserRepository

class UserTestCase(unittest.TestCase):
    """
    Test UserRepository
    Aplicamos principios como DRY (Don't Repeat Yourself) y KISS (Keep It Simple, Stupid).
    YAGNI (You Aren't Gonna Need It) y SOLID (Single Responsibility Principle).
    """
    
    def setUp(self):
        self.USERNAME_PRUEBA = 'pabloprats'
        self.EMAIL_PRUEBA = 'test@test.com'
        self.PASSWORD_PRUEBA = '123456'
        self.FIRSTNAME_PRUEBA = 'Pablo'
        self.LASTNAME_PRUEBA = 'Prats'
        self.PHONE_PRUEBA = '54260123456789'
        self.ADDRESS_PRUEBA = 'Address 1234'
        
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.user_repository = UserRepository()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_creation(self):
        user = self.__get_user()
        saved_user = self.user_repository.save(user)
        
        self.assertIsNotNone(saved_user.id)
        self.assertEqual(saved_user.email, self.EMAIL_PRUEBA)
        self.assertEqual(saved_user.name, self.USERNAME_PRUEBA)

    def test_user_update(self):
        user = self.__get_user()
        saved_user = self.user_repository.save(user)
        
        saved_user.name = "Pablo Actualizado"
        updated_user = self.user_repository.update(saved_user, saved_user.id)

        self.assertEqual(updated_user.name, "Pablo Actualizado")

    def test_user_deletion(self):
        user = self.__get_user()
        saved_user = self.user_repository.save(user)
        
        self.user_repository.delete(saved_user)
        deleted_user = self.user_repository.find(saved_user.id)
        
        self.assertIsNone(deleted_user)

    def test_find_user(self):
        user = self.__get_user()
        saved_user = self.user_repository.save(user)
        
        found_user = self.user_repository.find(saved_user.id)
        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.id, saved_user.id)

    def __get_user(self):
        data = UserData(
            firstname=self.FIRSTNAME_PRUEBA,
            lastname=self.LASTNAME_PRUEBA,
            phone=self.PHONE_PRUEBA,
            address=self.ADDRESS_PRUEBA,
        )
        user = User(
            name=self.USERNAME_PRUEBA,
            email=self.EMAIL_PRUEBA,
            password=self.PASSWORD_PRUEBA,
            data=data,
        )
        return user

if __name__ == '__main__':
    unittest.main()
