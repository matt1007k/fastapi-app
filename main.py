from fastapi import FastAPI
from pydantic import BaseModel

import config.envs
import os

app = FastAPI()


class User(BaseModel):
    id: str
    name: str
    age: int


@app.get("/")
def home():
    # test_user = os.environ["TEST_USER"]
    test_env = os.getenv("TEST_USER")
    print(test_env)
    return [User(id="One", name="Juan Maximo", age=23)]
