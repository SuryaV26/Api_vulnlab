from fastapi import FastAPI, Response,HTTPException,status
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange 

app=FastAPI()

class Users(BaseModel):
    author: str
    book: str
    Genre: str

users_info=[
    {"id":1,"author":"George RR Martin","book":"A song of ice and fire","Genre":"Fantasy"},
    {"id":2,"author":"Fredrick Beckman","book":"A man called ove","Genre":"Casual"},
    {"id":3,"author":"James Rollins","book":"Map of bones","Genre":"flag{AP1_000x1}"}
    ]


def find_user(id):
    for i in users_info:
        if i['id']==id:
            return i

def find_index(id):
    for j,p in enumerate(users_info):
        if p['id']==id:
            return j


#Get all post
@app.get("/api/users")
def all_post():
    
    return {"data":users_info}


#Creating User
@app.post("/api/users")
def create(user:Users):
    user_dicti=user.model_dump()
    user_dicti['id']=randrange(0,20)
    users_info.append(user_dicti)
    return {"Status":user_dicti}

#Fetch user data
@app.get("/api/users/{id}")
def get_user(id:int):
    if id==3:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Cannot access this id")
    find=find_user(id)
    return {"details":find}


#Deleting user
@app.delete("/api/users/{id}")
def delete_user(id:int):
    
    index=find_index(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    users_info.pop(index)
    return "Deleted"
