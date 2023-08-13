import os,socket
from flask import Flask,render_template
app = Flask(__name__)

color=os.environ.get('APP_COLOR')

@app.route("/")
def main():

    hostname = socket.gethostname()
    return render_template("hello.html",color=color,hostname=hostname)

if __name__=="__main__":
    app.run(host="0.0.0.0",port="8080")