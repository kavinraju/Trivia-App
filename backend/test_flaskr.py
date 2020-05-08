import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category

""" keystore consists of all the passwords required for the backend """
from keystore import database_password

ERROR_400_MESSAGE = "Bad request"
ERROR_404_MESSAGE = "Resource not found"
ERROR_405_MESSAGE = "Method not found"
ERROR_422_MESSAGE = "Uprocessable"

class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        username = "postgres"
        password = database_password
        database_name = "trivia_test"
        database_path = "postgresql://{}:{}@{}/{}".format(username, password, 'localhost:5432', database_name)

        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = database_name
        self.database_path = database_path
        setup_db(self.app, self.database_path)

        self.new_question = {
            'question': 'La Giaconda is better known as what?',
            'answer': 'Mona Lisa',
            'category': 2,
            'difficulty': 3
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    """ Test for the endpoint 
    GET '/categories'
    """
    ## TEST 1 ##
    # Success Test
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['categories']))
        self.assertTrue(data['total_categories'])
    
    """ # Error Test
    def test_404_no_categories_available(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], ERROR_404_MESSAGE) """


    """ Test for the endpoint 
    GET '/questions'
    """
    ## TEST 2 ##
    # Success Test
    def test_get_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(len(data['categories']))
        self.assertTrue(data['total_questions'])
    
    ## TEST 3 ##
    # Error Test
    def test_404_sent_request_beyond_valid_page(self):
        res = self.client().get('/questions?page=10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], ERROR_404_MESSAGE)


    """ Test for the endpoint 
    DELETE '/questions/<int:question_id>'
    
    Don't forget to comment the TEST 4 while running the other tests. It might throw error frequently once
    it has delelte the question with 'question_id'.
    """
    
    ## TEST 4 ##
    # Success Test
    # def test_delete_question(self):
        
    #     # Update the Question number to be deleted
    #     question_id = 17

    #     res = self.client().delete('/questions/' + str(question_id))
    #     data = json.loads(res.data)
    #     question = Question.query.filter(Question.id == question_id).one_or_none()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(question, None)
    #     self.assertEqual(data['deleted'], question_id)
    #     self.assertTrue(data['total_questions'])
    #     self.assertTrue(len(data['questions']))
    #     self.assertTrue(len(data['categories']))

    ## TEST 5 ##
    # Error Test
    def test_422_if_question_does_not_exist(self):

        # Update the Question number to be deleted
        question_id = 10000

        res = self.client().delete('/questions/' + str(question_id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422) 
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], ERROR_422_MESSAGE)


    """ Test for the endpoint 
    POST '/questions'
    """
    ## TEST 6 ##
    # Success Test
    def test_create_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(len(data['categories']))

    # Error Test
    def test_405_if_question_creation_not_allowed(self):
        res = self.client().post('/questions/1000', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], ERROR_405_MESSAGE)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()