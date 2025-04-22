from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'blackberry-system2025'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        a = request.form['username']
        b = request.form['password']
        print(a, b)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
