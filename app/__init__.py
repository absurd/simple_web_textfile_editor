from flask import Flask, request, render_template, redirect
import pdb

FILE = 'foo.txt'

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def txt_edit(file=FILE):
    if request.method == 'POST':
        with open(FILE, 'wb') as f:
            f.write(request.form['txt_content'].replace('\r', ''))
        return redirect('/')
    else:
        with open(FILE, 'rb') as f:
            txt_content = f.read()
        return render_template('web_editor.html', txt_content=txt_content)
