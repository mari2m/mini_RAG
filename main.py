from fastapi import FastAPI 
app=FastAPI()
#calling function through api 
#run as app server using uvicorn
#python -m uvicorn main:app --reload     url/welcome
@app.get("/welcome")
def welcome():
    return {
        "massage":"hello world"
    }

 