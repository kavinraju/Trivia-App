# Full Stack API Final Project This project is built as part of Full Stack Developer Nanodegree Program at Udacity.

## Full Stack Trivia

This project allows you to play a game called <b>Udacitrivia</b>, where there will be a set of questions under 6 categories. You can play a quiz by pressing the Play option.

### You can do the following in this project
1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others. 


## Get Started

### Pre-requisite and Local Development

1. Python
2. pip
3. Node
4. Flask

### Backend

From the [`./backend/`](./backend/README.md) directory run `pip install -r requirements.txt`. All the required packages are included in this file. To run the application run the following commands.<br>
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
Create a database `trivia` in PostgreSQL using the following commands.<br>
<b>For Linux:</b>
```bash
createdb trivia
```
<b>For Windows:</b>
```bash
create database trivia;
```
Run the following commands from [`./backend/`](./backend/README.md) directory to run the Migration Script to create the required tables:
```bash
python -m flask db init
python -m flask db migrate
python -m flask db upgrade
```
By default,the backend will run on localhost:5000

### Frontend

The [`./frontend/`](./frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server and from the same directory, run the following commands to start the client:
```bash
npm install // only once to install dependencies
npm start
```
By default,the frontend will run on localhost:3000

### Tests
In order to run test navigate to the [`./backend/`](./backend/README.md) directory and run the following commands.<br>
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
Don't forget to uncomment the test for the endpoint <b>DELETE '/questions/<int:question_id>'</b> while running your test for the first time and comment it while running the test for other endpoints. It is available at ## TEST 4 ## in [test_flaskr.py](https://github.com/kavinraju/Trivia-App/blob/master/backend/test_flaskr.py) file.
