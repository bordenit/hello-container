from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Greetings from the Flask Web Server, client request was successul!"

@app.route('/skills')
def skill():
    return "I am very skilled in DevSecOps, and Prisma Cloud!"

@app.route('/weaknesses')
def weakness():
    return "I have no weaknesses that I can't overcome!"

@app.route('/finalthought')
def finalthought():
    return "I admit my flaws, and admit this app is not the best, but we basically just made our own fly by night API! Woot woot!\nStarting cleanup now!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)