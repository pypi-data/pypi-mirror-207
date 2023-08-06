# aws_flask_lambda_swagger_ui

## Installation

Install the package using pip:

```sh
pip install aws-flask-lambda-swagger-ui
```

## Usage

```python
from flask import Flask
from aws_flask_lambda_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = '/aws/test/docs' 
API_URL = 'https://petstore.swagger.io/v2/swagger.json' 

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  
    API_URL,
    config={  
        'app_name': "AWS Lambda application"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)

```
