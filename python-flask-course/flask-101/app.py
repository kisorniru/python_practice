from flask import Flask

app = Flask(__name__)

@app.route('/')
def base():
	return "Welcome to your backend"

@app.route('/hello')
def send_hello():
	return "Hello World!"

if __name__ == "__main__":
	app.run(debug=True)