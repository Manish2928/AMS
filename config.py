import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-me")
    WTF_CSRF_ENABLED = True

    # If you later switch to SQLAlchemy, you can add SQLALCHEMY_* here
