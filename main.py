#from fastapi import FastAPI 
#app=FastAPI()
#calling function through api 
#run as app server using uvicorn
#python -m uvicorn main:app --reload     url/"welcome"
#test in swagger or postman
#@app.get("/")
#def welcome():
#    return {
#        "massage":"hello world"
#   }

####manage main with base.py
#dotenv is a Python package that helps manage environment variables 
# by loading them from a .env file into your application's environment. 
# This is useful for keeping sensitive information (like API keys, database credentials, and secret tokens) 
# out of your code.
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv(".env")

from routes import base

app = FastAPI()

app.include_router(base.base_router)

 