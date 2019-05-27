from flask import request
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/g<username>')
def hello_g(username=None):
    print("username={}, {!r}".format(username, request))
    print("id={}".format(request.args.get('id', None)))	
    print("fid={}".format(request.args.get('fid', None)))	
    #print("username={}, keyword={}, id={}, headers[0]={}".format(
    #	username, request.args['keyword'], request.args['id'], request.headers[0])
    #)
    return "fixed"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
