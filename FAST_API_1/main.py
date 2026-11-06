from fastapi import FastAPI , APIRouter, Form
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer
app=FastAPI()
oauth_scheme=OAuth2PasswordBearer(token_url="auth/token")
router=APIRouter("/users")
class Book(BaseModel):
    id : int
    Book_name : str
    author : str
    price : float


@app.get("/user/{userid}")
async def get_url(userid:int):

    return {"message":"Hi {userid} welcome to book store"}
@app.post("/item/")
async def create_item(book : Book):
    message = "this book is available..!"
    return message
@app.router("/")
def call_user():
    return {"message":"this is a router call..."}


#handle the data from the user
@app.post("/login")
async def get_data(user_name: str=Form(),password: str =Form()):
    return {"user name":user_name}  

#app.include_router(router)





if __name__=="__main__":
    import uvicorn
    uvicorn.run(app)