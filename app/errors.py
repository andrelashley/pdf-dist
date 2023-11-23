from flask import jsonify
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({ "Not Found": 404 })

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({ "Something went wrong": 500 })