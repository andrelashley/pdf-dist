from flask import jsonify
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/users')
def users():
    # return jsonify({'pdfs': pdf_list})
    return jsonify({'username': 'andre'})