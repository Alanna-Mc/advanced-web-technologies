
from flask import Flask, url_for
app = Flask(__name__)

@app.route ("/")
def home():
    css_url = url_for('static', filename='css/style.css')
    return f"""
    <html>
    <head>
        <title>Home Page with CSS</title>
        <link rel="stylesheet" href="{css_url}">
    </head>
    <body>
        <h1>Welcome to the Home Page!</h1>
        <p>This page is styled with CSS from the static/css folder.</p>
    </body>
    </html>
    """

@app.route('/hello/')
def hello_world():
    return "Hello Napier!!! :D"

@app.route('/static-example/img')
def static_example_img():
  start = '<img src="'
  url = url_for('static', filename='vmask.jpg')
  end = '">'
  return start+url+end, 200

@app.route("/goodbye/")
def goodbye():
  return "Goodbye Everyone :-^"

@app.route('/force404')
def force404():
  abort(404)

@app.errorhandler(404)
def page_not_found(error):
  return "Couldn't find the page you requested.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
