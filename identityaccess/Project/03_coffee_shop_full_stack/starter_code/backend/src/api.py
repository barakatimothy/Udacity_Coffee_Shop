from ast import main
import os
from turtle import title
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)



db_drop_and_create_all()

# ROUTES

@app.route('/drinks',methods = ['GET'])
def get_drinks():
    coffee_Shop_Drinks={ 
       'success':True,
       'id': self.id ,
       'title':self.title,
        'recipe': short_recipe }
    print ('Debugger', coffee_Shop_Drinks)
    return jsonify(coffee_Shop_Drinks,200)

@app.errorhandler(401)
def unauth_handler(error):
    return 'Unauthorized!', 401    

@app.route('/drinks-detail',methods =['GET'])
def getLong_drinks():
  detailedDrinks ={
     'id':self.id,
     'title':self.title,
     'recipe':json(self.recipe)
    }
  print('debugger',detailedDrinks)
  return jsonify (detailedDrinks,200)


@app.route('/drinks',methods =['POST'])
def post_drinks():
    newdrinks ={
     'id':self.id,
     'title':self.title,
     'recipe':json(self.recipe)
    }
    print('debugger',newdrinks)
    return jsonify('success',newdrinks,200)


@app.route('/drinks/<id>',methods =['PATCH'])
def modify_drinks():
  modified_Drinks ={
     'id':self.id,
     'title':self.title,
     'recipe':json(self.recipe)
    }
  print('debugger',modified_Drinks)
  return jsonify (modified_Drinks,200)


@app.route('/drinks/<id>',methods =['DELETE'])
def modify_drinks():
  remove_Drinks ={
     'id':self.id,
     'title':self.title,
     'recipe':json(self.recipe)
    }
  print('debugger',remove_Drinks)
  return jsonify (remove_Drinks,200)

# Error Handling


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


# get 
@app.errorhandler(404)
def resnotFound(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404
'''
@TODO implement error handler for 404
    error handler should conform to general task above
'''
#get long
@app.errorhandler(404)
def resnotFound(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


#patch
@app.errorhandler(404)
def resnotFound(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404

#delete
@app.errorhandler(404)
def resnotFound(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


