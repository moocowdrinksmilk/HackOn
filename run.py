from app.config import PORT
from app import app, context


if __name__ == "__main__":
    app.run(threaded=True)