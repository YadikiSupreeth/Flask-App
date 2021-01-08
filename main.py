from flask import Flask

app= Flask(__name__) 

@app.route('/')
def routePage():
    return "First Python Flask App Published in Azure"



if(__name__ == "__main__"): # Only run the app when this file is directly called
    app.run() # start the app
