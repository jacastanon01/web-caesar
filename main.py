from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
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
        <form method="post">
            <label type=text>Rotate by:

                <input name="rot" type="text" value="0"> 
            </label>
            <textarea name="text"/> 
            </textarea>
            <input type="submit" value="Sumbit Query">
        </form>

        
    </body>
</html>
"""


@app.route('/')
def index():
    return form

@app.route('/', methods=['POST'])
def encrypt():
    rot_value = request.form['rot']
    rot_value = int(rot_value)
    texts = request.form['text']
    rotated = rotate_string(texts,rot_value)
    return "<h1>" + rotated + "</h1>"




app.run()