from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse
import datetime

app = Flask(__name__)
api = Api(app)

todos = {}
id = 0 #initalizing counter for a new todo's self generated id

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in todos:
        abort(404, message=f"Todo {todo_id} does not exisit")

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, help='title of the todo')
parser.add_argument('due_date', type=str, default='')
parser.add_argument('completed', type=bool, default=False)

class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return todos[todo_id]
    
    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del todos[todo_id]
        return '', 204

    def put(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        todo = todos[todo_id]
        args = parser.parse_args()
        current_time = datetime.datetime.now()
        date_string = f"{current_time.month}/{current_time.day}/{current_time.year}"
        if args.title is not None:
            todo['title'] = args['title']
        if args.due_date is not None:
            todo['due_date'] = args['due_date']
        if args['completed']:
            todo['completed'] = True
            todo['completed_date'] = date_string
        todo['last_updated_date'] = date_string
        todos[todo_id] = todo
        return todo, 201

class TodoList(Resource):
    def get(self):
        return todos

    def post(self):
        global id
        id += 1
        args = parser.parse_args()
        todo_id = str(id)
        current_time = datetime.datetime.now()
        date_string = f"{current_time.month}/{current_time.day}/{current_time.year}"
        todos[todo_id] = {
            'title': args['title'],
            'created_date': date_string,
            'last_updated_date': date_string,
            'due_date': args['due_date'],
            'completed': args['completed']
            }
        return todos[todo_id], 201

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True)