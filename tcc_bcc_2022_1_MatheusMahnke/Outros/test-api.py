from flask import Flask, render_template, Response, request

app = Flask(__name__)


@app.route('/')
def index():
    return "healthy"


@app.route('/test-parameters')
def test_parameters():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    print(param1)
    print(param2)
    return "healthy"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
