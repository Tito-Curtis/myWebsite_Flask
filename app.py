from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/edu')
def edu():
    return render_template('edu.html')
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry, the page you requested is not availabe"
@app.route('/nav')
def nav_bar():
    return render_template('nav_bar.html')
@app.route('/contact')
def contact():
     return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')