from flask import Flask

application = Flask(__name__)

@application.route('/')
def home():
    return """
    <html>
        <head>
            <title>Welcome to AWS Elastic Beanstalk</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    text-align: center;
                    padding: 50px;
                }
                .container {
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
                    display: inline-block;
                }
                h1 {
                    color: #333;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello, AWS Elastic Beanstalk!</h1>
                <p>Your Flask application is successfully deployed 🚀</p>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port=5000)
