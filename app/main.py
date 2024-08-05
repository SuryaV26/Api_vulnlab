from fastapi import FastAPI, Header, Response,HTTPException,status
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange 
import psycopg2
from psycopg2.extras import RealDictCursor

app=FastAPI()

class Users(BaseModel):
    id: int
    name: str
    


#DB connection:
try:
    conn=psycopg2.connect(host='localhost',database='apilab',user='postgres',password='chola',cursor_factory=RealDictCursor)
    cursor=conn.cursor()
    print("connection successfull")

except Exception as error:
    print("Connection Failed")
    print("Error:",error)




#Api Routes:

#Get all post
@app.get("/api/users")
def all_post():
    cursor.execute("""select id,name from users where id!=7""")
    dis=cursor.fetchall()

    
    return {"data":dis}


#Fetch user data
@app.get("/api/users/{id}")
def get_user(id: int, authorization: str = Header(None)):
    cursor.execute("""SELECT id, name,is_admin,flag  FROM users WHERE id=%s""" , (str(id),))
    post = cursor.fetchone()
    
    if id == 7:
        if authorization != "admin": 
            raise HTTPException(
                status_code=401,
                detail="Invalid authentication credentials for accessing user with id 7"
            )
        cursor.execute("""SELECT id, name,flag,is_admin FROM users WHERE id=%s""", (str(id),))
        f = cursor.fetchone()
        return {"data": f}
    
    return {"data": post}


#Deleting user
