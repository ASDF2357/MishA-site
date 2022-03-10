from flask import Flask, escape, render_template

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     s = '''
#         <html>
#             <body>
#                 <h1>Здесь HTML разметка</h1>
#                 <p>Немного тектса тут и там</p>
#             </body>
#         </html>'''
#     return s


# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % ((escape(username)+" ")*10)


@app.route('/main')
def show_main():
    return render_template("Main.html")


@app.route('/about')
def show_about():
    return render_template("About.html")


@app.route('/shop_list')
def show_shop_list():
    return render_template("ShopList.html")


@app.route('/pencil')
def show_pencil():
    return render_template("Pencil.html")


if __name__ == '__main__':
    app.run(debug=True)
