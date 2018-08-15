from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
    <html>
        <head>
            <style>
                html, body{{
                  background: url('https://images.unsplash.com/photo-1514820402329-de527fdd2e6d?ixlib=rb-0.3.5&s=5c41456ea7b33814c0507de11c14ec9b&auto=format&fit=crop&w=1952&q=80') no-repeat center center fixed;
                  -moz-background-size: cover;
                  -o-background-size: cover;
                  background-size: cover;
                }}
                form{{
                    background-color: #eee;
                    background-color: #80A7AF;
                    padding: 20px;
                    margin: 5vh auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
                h1 {{
                    padding: 10vh 0 0 0;
                }}
                h1, p {{
                    font-family: verdana;
                    text-align: center;
                    color: white;
                }}
                input[type=submit] {{
                    background-color: white;
                    border: none;
                    padding: 10px 22px;
                }}
            </style>
        </head>
        <body>
            <h1>Caesar Cipher</h1>
            <p><strong>Encryption </strong>Enter a message and the number of letters to rotate the message by.</p>
            <p>Rotating a message by 13 to encrypt and then by 13 again will return the original message.</p>
            <form action="/" method="POST">
                <label>Rotate by:
                 <input type="text" name="rot" value="0">
                </label>
                <textarea name="text">{0}</textarea>
                <input type="submit" value="Submit Query">
            </form>
        </body>
    </html>
"""

@app.route("/")
def index():
    new_string = ""
    return form.format(new_string)

@app.route("/", methods=['POST'])
def encrypt():
    t = str(request.form["text"])
    r = int(request.form["rot"])
    rotated_string = rotate_string(t,r)
    result = "<h1>" + rotated_string + "</h1>"
    return form.format(rotated_string)

if __name__=="__main__":
    app.run()
