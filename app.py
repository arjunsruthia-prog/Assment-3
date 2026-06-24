from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mark', methods=['POST'])
def mark():
    name = request.form['name']

    with open("attendance.txt", "a") as file:
        file.write(name + "\n")

    return f"{name} marked successfully!"

if __name__ == '__main__':
    app.run(debug=True)