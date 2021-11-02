from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route('/calculator/<string:operation>/<int:value1>/<int:value2>')
def calculator(operation, value1, value2):
    ret = 0
    if operation == "add":
        ret = value1 + value2
    elif operation == "sub":
        ret = value1 - value2
    elif operation == "mul":
        ret = value1 * value2
    elif operation == "div":
        ret = value1 / value2

    return f'Operation {operation} with {value1} and {value2} is {ret}'

@app.route('/<notrail>')
def notrail(notrail):
    return "notrail"

@app.route('/<trail>/')
def trail(trail):
    return "trail"

@app.route('/information')
def information():
    users = [{'name':'John Smith', 'workplace':'School', 'userid':'10011'},
              {'name':'U.N. Owen', 'workplace':'DoA', 'userid':'10021'},
              {'name':'Guest', 'workplace':'None', 'userid':'10001'}]
    method = ''
    if request.method == 'GET':
        name = request.args.get("name", "Guest")
        workplace = request.args.get("workplace", "None")
        method = 'GET'
        
    elif request.method == 'POST':
        name = request.form['name']
        workplace = request.form['workplace']
        method = 'POST'

    for user in users:
        if user['name'] == name and user['workplace'] == workplace:
            return f'Hello, {name}#{user["userid"]} by {method}!'

    return 'Who are you?'