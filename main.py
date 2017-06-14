from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
    <html>
        <head>
            <style>
                form{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            <form action="/" method="POST">
                <label>Rotate by:
                 <input type="text" name="rot" value="0">
                </label> 
                <textarea name="text"></textarea>
                <input type="submit" value="Submit Query">
            </form>        
        </body>
    </html> 
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    t = str(request.form["text"])
    r = int(request.form["rot"])
    rotated_string = rotate_string(t,r)
    result = "<h1>" + rotated_string + "</h1>"
    return result

app.run()
