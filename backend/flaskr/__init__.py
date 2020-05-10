import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

# Initialization of global variables
QUESTIONS_PER_PAGE = 10
ERROR_400_MESSAGE = "Bad request"
ERROR_404_MESSAGE = "Resource not found"
ERROR_405_MESSAGE = "Method not found"
ERROR_422_MESSAGE = "Uprocessable"

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  Set up CORS. Allowed '*' for origins.
  '''
  cors = CORS(app, resources ={r"/": {"origins":"*"}})

  '''
  Used the after_request decorator to set Access-Control-Allow.
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, PATCH, DELETE, OPTIONS')
    return response


  '''
  GET /categories

  Endpoint to handle GET requests for all available categories.

  Returns:
      - list of categories
      - success value
      - total number of categories
  '''
  @app.route('/categories', methods=['GET'])
  def retrive_categories():

    selection = Category.query.all()
    categories = {}

    for category in selection:
      categories[category.id] = category.type
      
    if categories is None or len(categories) == 0:
      abort(404)
    else:
      return jsonify({
        'success': True,
        'categories': categories,
        'total_categories': len(categories)
      })

  ''' Helper Method for pagination. '''

  def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page-1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

  '''
  GET /questions

  Endpoint to handle GET requests for questions, including pagination (every 10 questions). 
  
  Returns:
      - list of categories
      - current category (always None)
      - list of questions
      - success value
      - total number of questions
  '''
  @app.route('/questions', methods=['GET'])
  def retrive_questions():

    # Querying all the questions in the order of their IDs
    selection = Question.query.order_by(Question.id).all()
    current_questions = paginate_questions(request, selection)

    if current_questions is None or len(current_questions) == 0:
      abort(404)
    else:
      categories_selction = Category.query.all()
      categories = {}

      for category in categories_selction:
        categories[category.id] = category.type

      return jsonify({
        'success': True,
        'questions': current_questions,
        'total_questions': len(selection),
        'current_category': None,
        'categories': categories
      })

  
  '''
  DELETE /questions/<int:question_id>
  
  Endpoint to DELETE question using a question ID.

  Returns:
      - list of categories
      - current category (always None)
      - deleted question id
      - list of questions
      - success value
      - total number of questions
  '''
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      # Querying for the Question with ID equal to question_id
      question = Question.query.filter(Question.id == question_id).one_or_none()
      
      if question is None:
        abort(404) # Not Found
      
      question.delete()
      # Update UI with updated set of questions
      questions_selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, questions_selection)

      # Querying for all the categories available
      categories_selection = Category.query.order_by(Category.type).all()
      categories = [category.format() for category in categories_selection]

      return jsonify({
        'success': True,
        'deleted': question_id,
        'questions': current_questions,
        'total_questions': len(questions_selection),
        'current_category': None,
        'categories': categories
      })

    except:
      abort(422) # Unprocessable Entity

  
  '''
  POST /questions

  Endpoint to POST a new question. 
  
  Requires:
      - question text
      - answer text
      - category
      - difficulty score.

  Returns:
      - list of categories
      - created question id
      - current category
      - list of questions
      - success value
      - total number of questions
  '''
  # Endpoint [POST] to get questions based on a Search Term is also included in the same method -  create_question()
  @app.route('/questions', methods=['POST'])
  def create_question():
    body = request.get_json()
    
    if body is None:
      abort(422) # Unprocessable Entity
    else:
      new_question = body.get('question', None)
      new_answer = body.get('answer', None)
      new_category = body.get('category', None)
      new_difficulty_score = body.get('difficulty', None)
      search = body.get('searchTerm', None)

      try:
        if search:
          questions_selection = Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(search))).all()
          current_questions = paginate_questions(request, questions_selection)

          return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(questions_selection),
            'current_category': None
          })
        else:
          question = Question(new_question, new_answer, new_category, new_difficulty_score)
          question.insert()

          questions_selection = Question.query.order_by(Question.id).all()
          current_questions = paginate_questions(request, questions_selection)

          categories_selection = Category.query.all()
          categories = {}

          for category in categories_selection:
            categories[category.id] = category.type

          return jsonify({
            'success': True,
            'created': question.id,
            'questions': current_questions,
            'total_questions': len(questions_selection),
            'current_category': question.category,
            'categories': categories
          })
      except:
        abort(422) # Unprocessable Entity


  '''
  POST /questions

  Endpoint to get questions based on a search term ( search term is the substring of the question ).

  Returns:
      - current category (always None)
      - list of categories
      - list of questions
      - success value
      - total number of questions

  Refer create_question() method.
  '''


  '''
  GET categories/<int:category_id>/questions

  Endpoint to get questions based on category.
  
  Returns:
      - current category
      - list of questions
      - success value
      - total number of questions
  '''
  @app.route('/categories/<int:category_id>/questions', methods=['GET'])
  def get_questions_based_on_category(category_id):
    try:
      # Check if category with 'category_id' is available and return the response.
      category = Category.query.filter(Category.id == category_id).one_or_none()
      
      if category is None:
        abort(404)
      else:
        questions_selection = Question.query.order_by(Question.id).filter(Question.category == category_id).all()
        questions_with_category_id = paginate_questions(request, questions_selection)
      
        return jsonify({
          'success': True,
          'questions': questions_with_category_id,
          'total_questions': len(questions_selection),
          'current_category': category.type
          })
    except:
      abort(404)
      

  '''
  POST /quizzes

  Endpoint to get questions to play the quiz.

  Requires:
      - list of previous question ids, list can be empty while starting the game
      - quiz category

  Returns:
      - previousQuestions
      - a random question (that is not one of the previous questions)
      - success value
  '''
  @app.route('/quizzes', methods=['POST'])
  def play_quiz():
    body = request.get_json() # Get the body of the request

    if body is None:
      abort(422) # Unprocessable Entity
    else:
      try:
        # Get the data in the body of the request
        previous_questions = body.get('previous_questions', None)
        quiz_category_response = body.get('quiz_category', None)

        if quiz_category_response['type'] == 'ALL' and quiz_category_response['id'] == 0:
          
          
          # Query the questions in all the Categories
          questions_of_quiz_category = Question.query.order_by(Question.id).all()
          formated_questions = paginate_questions(request, questions_of_quiz_category)

        else:  
          # Get the `quiz_category_id`
          quiz_category_id = quiz_category_response['id']

          # Query the questions in the Category with `quiz_category_id`
          questions_of_quiz_category = Category.query.get(quiz_category_id).questions
          formated_questions = paginate_questions(request, questions_of_quiz_category)

        # Initialization
        question_ids = []
        random_question_id = 0
        new_random_question = None
       
        ## Edge case: If the length of `previous_questions` is equal to the len `formated_questions`
        # return the response with `question` & `previousQuestions` as None.
        if len(previous_questions) == len(formated_questions):
          return jsonify({
          'success': True,
          'question': new_random_question,
          'previousQuestions': None
          })
        
        # Generate a list of questions ids in `question_ids`
        for question in formated_questions:
          question_ids.append(question.get('id'))

        if len(previous_questions) == 0:
          # Generate a random question id from the full list of `question_ids` and append it to the `previous_questions`
          random_question_id = random.choice(question_ids)
          previous_questions.append(random_question_id)

        else:
          # Eliminate the previous question id's from the full list of `question_ids`
          for id in previous_questions:
            if id in question_ids:
              question_ids.remove(id)

          # Generate a random question id from `question_ids` list
          random_question_id = random.choice(question_ids)

        # Looping through `formated_questions` to get the question with id `random_question_id`
        for question in formated_questions:
          if question.get('id') == random_question_id:
            new_random_question = question

        return jsonify({
          'success': True,
          'question': new_random_question,
          'previousQuestions': previous_questions
        })
      except:
        abort(422) # Unprocessable Entity

  ''' Error handlers for all the expected errors '''

  ''' ERROR 404 '''
  @app.errorhandler(404)
  def resource_not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message': ERROR_404_MESSAGE,
      'error_message': str(error)
    }), 404

  ''' ERROR 422 '''
  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message': ERROR_422_MESSAGE,
      'error_message': str(error)
    }), 422

  ''' ERROR 405 '''
  @app.errorhandler(405)
  def method_not_allowed(error):
    return jsonify({
      'success': False,
      'error': 405,
      'message': ERROR_405_MESSAGE,
      'error_message': str(error)
    }), 405
  
  return app

    