from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    titles = 'hey leon'
    return render_template('index.html', titles=titles)


