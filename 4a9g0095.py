from flask import Flask, request

app = Flask(__name__)

@app.route('/hello/')
#127.0.0.1:5000/hello/?university=stust&city=Tainan
def hello():
    university = request.args.get('university')
    city = request.args.get('city')
    return f"Hello,{university} {city}"

if __name__ == '__main__':
    app.run(debug=True)
