from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    assert request.args.get('name'), "Name parameter is missing"

    name = request.args.get('name', 'Guest')
    return render_template_string('Hello, ' + name + '!')

@app.route('/eval', methods=['POST'])
def evaluate():
    expression = request.form.get('expression')
    result = eval(expression)
    return f'Ressult: {result}'

@app.route('/unsafe_deserialization')
def unsafe_deserialization():
    import pickle
    data = request.args.get('data').encode()
    obj = pickle.loads(data)
    return str(obj)

if __name__ == '__main__':
    app.run(debug=True)
