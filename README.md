# Trivia App

This project allows you to play a game called <b>Udacitrivia</b>, where you can see/answer a set of questions under 6 categories. You can play a quiz by pressing the Play option.

#### This is the 2nd project built as part of API Development and Documentation lesson in the Full Stack Web Developer Nanodegree Program at Udacity.

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/).

### You can do the following in this project
1. <b>Display questions -</b> both all questions and by category. Questions would show the question, category and difficulty rating by default and can show/hide the answer. 
2. <b>Delete questions.</b>
3. <b>Add questions</b> and require that they include question and answer text.
4. <b>Search for questions</b> based on a text query string.
5. <b>Play the quiz game</b>, randomizing either all questions or within a specific category. 

This Trivia App project will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others. 


## Get Started

### Pre-requisite and Local Development

1. Python
2. pip
3. Node
4. Flask

### .gitignore file

- Take a look at the [.gitignore file](https://github.com/kavinraju/Trivia-App/blob/master/.gitignore).
- `keystore.py` file consists of the database password `database_password` used in [models.py](https://github.com/kavinraju/Trivia-App/blob/master/backend/models.py) and [test_flaskr.py](https://github.com/kavinraju/Trivia-App/blob/master/backend/test_flaskr.py).
- `trivia-project-fsnd` is the `python venv` name for this project. For this project it is used for installing the `backend` packages.
- `trivia-frontend` is the `python venv` name for the `frontend` application. Packages of the `frontend` application are installed here.
- You can either choose to have the same `python venv` or different for the `frontend` & `backend` applications.

### Backend

From the [`./backend`](./backend/README.md) directory run `pip install -r requirements.txt`. All the required packages are included in this file. To run the application run the following commands.<br>
<b>For Linux:</b>
```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
<b>For Windows:</b>
```bash
set FLASK_APP=flaskr
set FLASK_ENV=development
python -m flask run
```
<br>Create a database `trivia` in PostgreSQL using the following commands.<br>
<b>For Linux:</b>
```bash
createdb trivia
```
<b>For Windows:</b>
```bash
create database trivia;
```
Run the following commands from [`./backend`](./backend/README.md) directory to run the Migration Script to create the required tables:
```bash
python -m flask db init
python -m flask db migrate
python -m flask db upgrade
```
By default, the backend will run on `localhost:5000`

### Frontend

The [`./frontend`](./frontend/README.md) directory contains the complete React frontend to consume the data from the Flask server and from the same directory, run the following commands to start the client:
```bash
npm install // only once to install dependencies
npm start
```
By default, the frontend will run on `localhost:3000`

### Tests

In order to run test, navigate to the [`./backend`](./backend/README.md) directory and, run the following commands.<br>
<b>For Linux:</b>
```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
<b>For Windows:</b>
```bash
drop database trivia_test;
create database trivia_test;
psql trivia_test < trivia.psql -U user_name_of_db
python test_flaskr.py
```
<b>NOTE:</b>
Don't forget to uncomment the test for the endpoint <b>DELETE `/questions/<int:question_id>`</b> while running endpoint test for the first time and comment it while running the test for other endpoints. It is available under the comment `## TEST 4 ##` in [test_flaskr.py](https://github.com/kavinraju/Trivia-App/blob/master/backend/test_flaskr.py) file.


# API Reference
## Get Started
- <b>Base URL:</b> At present this app is not hosted as a base URL anywhere and can only be run locally. By default the backend is hosted at `http://127.0.0.1:5000/` which is set as a proxy in the frontend configuration.
- <b>Authentication:</b> This version of the application does not require authentication or API keys.

## Endpoints

### GET `/categories`
   
<ul>
  <li><b>Genral:</b></li>
    <ul>
          <li>Returns
             <ul>
               <li>list of categories</li>
               <li>success value</li>
               <li>total number of categories</li>
             </ul>          
         </li>
    </ul>
  <li><b>Sample:</b> curl -X GET http://localhost:5000/categories </li>
  <li>Success <b>Test</b> `TEST-1` is available at <a href="https://github.com/kavinraju/Trivia-App/blob/master/backend/test_flaskr.py">test_flaskr.py</a> file.</li>
</ul>
    
```json
{
  "categories": [
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }, 
    {
      "id": 0, 
      "type": "tech"
    }
  ], 
  "success": true, 
  "total_categories": 7
}
```
<b>NOTE:</b>
If required do add a category with `ID = 0` using SQL command. Since [trivia.sql](https://github.com/kavinraju/Trivia-App/blob/master/backend/trivia.psql) doesn't add a category with `ID = 0` there will be some error in the front-end part while rendering the views.
<b>Command to insert a record:</b>
```sql
INSERT INTO categories (id, type) VALUES(0, 'tech'); // categories is the table name
```

### GET `/questions`
<ul>
  <li><b>Genral:</b></li>
    <ul>
         <li>Returns
           <ul>
             <li>list of categories</li>
             <li>current category (always None)</li>
             <li>list of questions</li>
             <li>success value</li>
             <li>total number of questions</li>
           </ul>          
         </li>
      <li>Results are paginated in groups of 10. Include a request argument to choose page number starting from 1, if not mentioned anything, page number defaults to 1.</li>
    </ul>
  <li><b>Sample:</b> curl -X GET http://localhost:5000/questions</li>
  <li>Both success `TEST 2` and error `TEST 3` <b>Test</b>s are available at <a href="https://github.com/kavinraju/Trivia-App/blob/master/backend/test_flaskr.py">test_flaskr.py</a> file.</li>
</ul>
    
```json
{
  "categories": [
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }, 
    {
      "id": 0, 
      "type": "tech"
    }
  ], 
  "current_category": null, 
  "questions": [
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ], 
  "success": true, 
  "total_questions": 31
}
```

### DELETE  `/questions/<int:question_id>`
<ul>
  <li><b>Genral:</b></li>
    <ul>
         <li>Returns
           <ul>
             <li>list of categories</li>
             <li>current category (always None)</li>
             <li>deleted question id</li>
             <li>list of questions</li>
             <li>success value</li>
             <li>total number of questions</li>
           </ul>          
         </li>
    </ul>
  <li><b>Sample:</b> curl -X DELETE http://localhost:5000/questions/5</li>
  <li>Both success `TEST 4` and error `TEST 5` <b>Test</b>s are available at <a href="https://github.com/kavinraju/Trivia-App/blob/master/backend/test_flaskr.py">test_flaskr.py</a> file.</li>
</ul>
    
```json
{
  "categories": [
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 6,
      "type": "Sports"
    },
    {
      "id": 0,
      "type": "tech"
    }
  ],
  "current_category": null,
  "deleted": 5,
  "questions": [
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ],
  "success": true,
  "total_questions": 30
}
```
### POST `/questions` To create a question
<ul>
  <li><b>Genral:</b></li>
    <ul>
         <li>Returns
           <ul>
             <li>list of categories</li>
             <li>created question id</li>
             <li>current category</li>
             <li>list of questions</li>
             <li>success value</li>
             <li>total number of questions</li>
           </ul>          
         </li>
    </ul>
  <li><b>Sample:</b> curl -X POST http://localhost:5000/questions -H "Content-Type: application/json" -d "{ \"question\":\"La Giaconda is better known as what?\",\"answer\":\"Mona Lisa\",\"category\":\"2\",\"difficulty\":\"3\"}"</li>
  <li>Both success `TEST 6` and error `TEST 7` <b>Test</b>s are available at <a href="https://github.com/kavinraju/Trivia-App/blob/master/backend/test_flaskr.py">test_flaskr.py</a> file.</li>
</ul>
    
```json
{
  "categories": [
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 6,
      "type": "Sports"
    },
    {
      "id": 0,
      "type": "tech"
    }
  ],
  "created": 42,
  "current_category": 2,
  "questions": [
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ],
  "success": true,
  "total_questions": 31
}
```

### POST `/questions` To search for a question
<ul>
  <li><b>Genral:</b></li>
    <ul>
         <li>Returns
           <ul>
             <li>current category (always None)</li>
             <li>list of categories</li>
             <li>list of questions</li>
             <li>success value</li>
             <li>total number of questions</li>
           </ul>          
         </li>
    </ul>
  <li><b>Sample:</b> curl -X POST http://localhost:5000/questions -H "Content-Type: application/json" -d "{ \"searchTerm\":\"what is\"}"</li>
  <li>Both success `TEST 8` and error `TEST 9` <b>Test</b>s are available at <a href="https://github.com/kavinraju/Trivia-App/blob/master/backend/test_flaskr.py">test_flaskr.py</a> file.</li>
   
</ul>
    
```json
{
  "current_category": null,
  "questions": [
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    }
  ],
  "success": true,
  "total_questions": 2
}
```

### POST `/quizzes` To play quiz game
<ul>
  <li><b>Genral:</b></li>
    <ul>      
        <li>Requires
            <ul>
             <li>list of previous question ids, list can be empty while starting the game</li>
             <li>quiz category</li>
           </ul>      
        </li>
         <li>Returns
           <ul>
             <li>previousQuestions</li>
             <li>a random question</li>
             <li>success value</li>
           </ul>          
        </li>
    </ul>
    <li><b>Sample:</b></li>
</ul>
<b>Resquest Data:</b>
<p>Before 1st Question:</p>

```json
{
   "previous_questions":[],
   "quiz_category":{
      "type":{
         "id":2,
         "type":"Art"
      },
      "id":"0"
   }
}
```

<p>After 1st Question:</p>

```json
{
   "previous_questions":[40],
   "quiz_category":{
      "type":{
         "id":2,
         "type":"Art"
      },
      "id":"0"
   }
}
```

<p>After 2nd Question:</p>

```json
{
   "previous_questions":[ 40, 42 ],
   "quiz_category":{
      "type":{
         "id":2,
         "type":"Art"
      },
      "id":"0"
   }
}
```

<p>After 3rd Question:</p>

```json
{
   "previous_questions":[ 40, 42, 16 ],
   "quiz_category":{
      "type":{
         "id":2,
         "type":"Art"
      },
      "id":"0"
   }
}
```   

<p>After 4th Question:</p>

```json
{
   "previous_questions":[ 40, 42, 16, 41 ],
   "quiz_category":{
      "type":{
         "id":2,
         "type":"Art"
      },
      "id":"0"
   }
}
```

<p>After 5th Question:</p>

```json
{
   "previous_questions":[ 40, 42, 16, 41, 19 ],
   "quiz_category":{
      "type":{
         "id":2,
         "type":"Art"
      },
      "id":"0"
   }
}
```


### GET   `categories/<int:category_id>/questions`
<ul>
  <li><b>Genral:</b></li>
    <ul>
         <li>Returns
           <ul>
             <li>current category</li>
             <li>list of questions</li>
             <li>success value</li>
             <li>total number of questions</li>
           </ul>          
         </li>
         <li>Results are paginated in groups of 10. Include a request argument to choose page number starting from 1, if not mentioned anything, page number defaults to 1.</li>
    </ul>
  <li><b>Sample:</b> curl -X GET http://localhost:5000/categories/3/questions</li>
  <li>Both success `TEST 10` and error `TEST 11` <b>Test</b>s are available at <a href="https://github.com/kavinraju/Trivia-App/blob/master/backend/test_flaskr.py">test_flaskr.py</a> file.</li>
</ul>
    
```json
{
  "current_category": "Geography",
  "questions": [
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 3
}
```

## Error Handling
Errors are returned as JSON objects in the following format:
```json
{
  "error": 404, 
  "error_message": "404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.", 
  "message": "Resource not found", 
  "success": false
}
```
This API will return three error types when requests fail:
<ul>
  <li><b>404</b> Resource not found</li>
  <li><b>405</b> Method not found</li>
  <li><b>422</b> Uprocessable Entity</li>
</ul>

## Authors
- Kavin Raju S, Completed this project
- Starter code from Udacity [Full Stack Web Developer Nanodegree program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044).

## Acknowledgements
The awesome [Udacity](https://udacity.com/) Team!
