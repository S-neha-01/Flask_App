from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Application Welcome, Sneha </title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            .container {
                text-align: center;
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333;
                margin: 0;
            }
            .message {
                color: #666;
                font-size: 18px;
                margin-top: 20px;
            }
            .badge {
                display: inline-block;
                background: #667eea;
                color: white;
                padding: 8px 16px;
                border-radius: 20px;
                margin-top: 20px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Flask Application</h1>
            <p class="message">This simple flask application deployed by Sneha for jenkins CICD pipeline.</p>
            <div class="badge">✓ Successfully Deployed</div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
