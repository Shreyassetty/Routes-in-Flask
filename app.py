from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/about')
def about():
    return "This is the About page."

@app.route('/goodbye')
def goodbye():
    return "Goodbye, see you soon!"



if __name__ == '__main__':
    app.run(debug=True)
