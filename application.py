from flask import Flask

application = Flask(__name__)

@application.route('/')
def home():
    return "Hello, AWS Elastic Beanstalk!"

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port=5000)
