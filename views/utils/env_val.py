from dotenv import load_dotenv
import os

load_dotenv('.env')

database_pwd = os.environ.get("DATABASEKEY")