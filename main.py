from flask import Flask, escape

app = Flask(__name__)


@app.route('/')
def hello_world():
    s = '''
        <html>
            <body>
                <h1>Здесь HTML разметка</h1>
                <p>Немного тектса тут и там</p>
            </body>
        </html>'''
    return s
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % ((escape(username)+" ")*10)


if __name__ == '__main__':
    app.run(debug=True)
