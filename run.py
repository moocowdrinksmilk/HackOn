from app import app, setWebHook

from app import routes #ensures that routes are loaded

if __name__ == "__main__":
    setWebHook()
    app.run(threaded=True)