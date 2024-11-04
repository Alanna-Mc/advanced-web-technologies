
from flask import Flask, url_for, request
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

@app.route("/hello/")
def hello():
  name = request.args.get("name","")
  if name == "":
    return "No paramater supplied"
  else:
    return "Hello %s" % name

@app.route('/helloworld/')
def hello_world():
    return "Hello Napier!!! :D"

@app.route("/display")
def display():
  return "<img src='" + url_for('static', filename='uploads/file.png')+"'/>"

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

@app.route("/account", methods=['GET', 'POST'])
def account():
  if request.method == 'POST':
    print (request.form)
    name = request.form["name"]
    return "hello %s" % name
  else:
   page = """
   <html><body>
     <form action= "" method="post" name="form">
       <label for="name">Name:</label>
       <input type = "text" name ="name" id="submit"/>
       <input type="submit" name="submit" id="submit"/>
     </form>
     </body><html>"""
   return page

@app.route("/upload/", methods=["POST", "GET"])
def account2():
  if request.method == "POST":
    f = request.files["datafile"]
    f.save("static/uploads/file.png")
    return "file Uploaded"
  else:
    page= """
    <html>
      <body>
        <form action="" method="post" name="form" enctype="multipart/form-data">
          <input type="file" name="datafile" />
          <input type="submit" name="submit" id="submit"/>
       </form>
      </body>
    </html>
    """
    return page, 200

@app.route("/entername/<name>")
def entername(name):
  return "Hello %s" % name

@app.route("/add/<int:first>/<int:second>")
def add(first, second):
  return str(first+second)

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=5001, debug=True)
