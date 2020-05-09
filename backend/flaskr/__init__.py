import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

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
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  DONE
  '''
  cors = CORS(app, resources ={r"/": {"origins":"*"}})

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow. DONE
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, PATCH, DELETE, OPTIONS')
    return response


  '''
  @TODO: DONE
  Create an endpoint to handle GET requests 
  for all available categories.
  '''

  @app.route('/categories', methods=['GET'])
  def retrive_categories():

    selection = Category.query.order_by(Category.type).all()
    categories = [category.format() for category in selection]

    if categories is None or len(categories) == 0:
      abort(404)
    else:
      return jsonify({
        'success': True,
        'categories': categories,
        'total_categories': len(categories)
      })


  '''
  @TODO: DONE
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''

  ''' Helper Method for pagination. '''

  def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page-1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

  @app.route('/questions', methods=['GET'])
  def retrive_questions():

    selection = Question.query.order_by(Question.id).all()
    current_questions = paginate_questions(request, selection)

    if current_questions is None or len(current_questions) == 0:
      abort(404)
    else:
      categories_selction = Category.query.order_by(Category.type).all()
      categories = [category.format() for category in categories_selction]

      return jsonify({
        'success': True,
        'questions': current_questions,
        'total_questions': len(selection),
        'current_category': None,
        'categories': categories
      })

  
  '''
  @TODO: DONE
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''

  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id == question_id).one_or_none()
      
      if question is None:
        abort(404) # Not Found
      
      question.delete()
      # Update UI with updated set of questions
      questions_selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, questions_selection)

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
  @TODO: Done
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.
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

          categories_selction = Category.query.order_by(Category.type).all()
          categories = [category.format() for category in categories_selction]

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
  @TODO: Done
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  # Endpoint [POST] to get questions based on a Search Term is also included in the above method -  create_question()


  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
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
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  @app.route('/quizzes', methods=['POST'])
  def play_quiz():
    body = request.get_json()
    print(body)

    if body is None:
      print('body is none')
      abort(422) # Unprocessable Entity
    else:
      previous_questions = body.get('previous_questions', None)
      quiz_category = body.get('quiz_category', None)

      questions_of_quiz_category = Category.query.get(quiz_category).questions
      for question in questions_of_quiz_category:
        print(question.format(), '\n')

      return jsonify({
        'success': True,
        'question': body        
      })

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''

  @app.errorhandler(404)
  def resource_not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message': ERROR_404_MESSAGE,
      'error_message': str(error)
    }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message': ERROR_422_MESSAGE,
      'error_message': str(error)
    }), 422

  @app.errorhandler(405)
  def method_not_allowed(error):
    return jsonify({
      'success': False,
      'error': 405,
      'message': ERROR_405_MESSAGE,
      'error_message': str(error)
    }), 405
  
  return app

    