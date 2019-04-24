# TODOs API

This is a Flask API to create todos.  No persitance storage is used.  Once the server shuts down, the todolist disappears.

## Running the API locally

* Git clone this repo to your PC and CD into the project dir

* Install the dependencies
    ```
    $pipenv install
    ```

* Start a PIPENV shell
    ```
    $ pipenv shell
    ```
* Run the tests
    ```
    $ pytest
    ```
* Run the API
    ```
    $ flask run
    ```

## Using the API's endpoints

### GET '/todos'

* Returns all the todos
    ex.
    {
        "1": {
            "title": "Write README.MD",
            "created_date": "4/24/2019",
            "last_updated_date": "4/24/2019",
            "due_date": "",
            "completed": false
        },
        "2": {
            "title": "Write integrating tests for all endpoings.",
            "created_date": "4/24/2019",
            "last_updated_date": "4/24/2019",
            "due_date": "",
            "completed": false
        }
    }

### POST '/todos'

* Creates a todo
* args:
    title (string, required): the task needing to be todone
    due_date (string, eg. "MM/DD/YYYY", optional): the due date of the task

### GET '/todos/<TODO_ID>'

* Returns one TODO.  If invalid TODO_ID is provided, 404 error is return

### DELETE '/todos/<TODO_ID>'

* Removes a todo

### PUT '/todos/<TODO_ID>'

* Updates a todo.  If invalid TODO_ID is provided, 404 error is return.  

```
$ curl http://localhost:5000/todos/1 -d "completed=True" -X PUT -v
```

    {
        "1": {
            "title": "Write README.MD",
            "created_date": "4/23/2019",
            "last_updated_date": "4/24/2019",
            "due_date": "",
            "completed": true,
            "completed_date": "4/24/2019"
        },
        "2": {
            "title": "Write integrating tests for all endpoints.",
            "created_date": "4/24/2019",
            "last_updated_date": "4/24/2019",
            "due_date": "",
            "completed": false
        }
    }

