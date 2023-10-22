from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # Vulnerability 1: Use of assert statement
    assert request.args.get('name'), "Name parameter is missing"

    # Vulnerability 2: Use of "render_template_string" can lead to Jinja2 Template Injection if user input is passed
    name = request.args.get('name', 'Guest')
    return render_template_string('Hello, ' + name + '!')

@app.route('/eval', methods=['POST'])
def evaluate():
    # Vulnerability 3: Use of "eval"
    expression = request.form.get('expression')
    result = eval(expression)
    return f'Result: {result}'

@app.route('/unsafe_deserialization')
def unsafe_deserialization():
    import pickle
    # Vulnerability 4: Use of "pickle.loads" for deserialization which can be unsafe
    data = request.args.get('data').encode()
    obj = pickle.loads(data)
    return str(obj)

if __name__ == '__main__':
    # Vulnerability 5: Flask app running without setting debug=False in production
    app.run(debug=True)
