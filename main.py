from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/trending')
def trending():
    return render_template('trending.html')

@app.route('/popular')
def popular():
    return render_template('popular.html')

@app.route('/clothes')
def clothes():
    return render_template('clothes.html')

@app.route('/shoes')
def shoes():
    return render_template('shoes.html')

@app.route('/accessories')
def accessories():
    return render_template('accessories.html')

if __name__ == '__main__':
    app.run(debug=True)
