from dotenv import load_dotenv
import os

load_dotenv(".env")

envs = {
    "TEST_USER": os.getenv("TEST_USER"),
    "DATABASE_URL": os.getenv("DATABASE_URL"),
}
