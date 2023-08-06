# aws_flask_lambda

## Installation

Install the package using pip:

```sh
pip install aws-flask-lambda
```

## Usage

```python
from aws_flask_lambda import FlaskLambda
from flask import request, jsonify

app = FlaskLambda(__name__)


@app.route('/greet', methods=['GET', 'POST'])
def greet():
    name = request.form.get('name', 'World')
    message = f'Hello, {name}!'
    return (
        jsonify({'message': message}),
        200,
        {'Content-Type': 'application/json'}
    )


if __name__ == '__main__':
    app.run(debug=True)

```
