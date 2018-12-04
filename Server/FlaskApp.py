from flask import Flask, request
import subprocess
import time
import codecs
import os
app = Flask(__name__)

def store_file(text, ctime):
    if not os.path.exists("../To_Be_Clean"):
        os.mkdir("../To_Be_Clean")
    if not os.path.exists("../To_Be_Clean/"+ctime):
        os.mkdir("../To_Be_Clean/"+ctime)
    if not os.path.exists("../To_Be_Clean/"+ctime+"/my_news"):
        os.mkdir("../To_Be_Clean/"+ctime+"/my_news")
    with codecs.open("../To_Be_Clean/"+ctime+"/my_news/1",'w', encoding='utf-8') as fp:
        fp.write(text)

def open_sum(ctime):
    with codecs.open("../To_Be_Clean/"+ctime+"/summarizations/output/1",'r', encoding='utf-8') as fp:
        return fp.read()
    
@app.route("/")
def hello():
    return '<form action="/echo" method="GET"><input name="text"><input type="submit" value="Text To Summarize (Has to be encoded in UTF-8)"></form>'
    
@app.route("/echo")
def echo(): 
    file_text = request.args.get('text', '')
    ctime = str(int(round(time.time() * 1000)))
    runstring = "./run.sh " + str(ctime)
    store_file(file_text, ctime)
    p1 = subprocess.Popen([runstring], shell=True, executable="/bin/bash")
    p1.wait()
    my_sum = open_sum(ctime)
    subprocess.call("./clean.sh " + ctime, shell=True)
    return my_sum

    
    
if __name__ == "__main__":
    app.run()

