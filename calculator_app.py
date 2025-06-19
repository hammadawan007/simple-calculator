from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            n1 = float(request.form['num1'])
            n2 = float(request.form['num2'])
            op = request.form['op']

            if op == '+':
                result = n1 + n2
            elif op == '-':
                result = n1 - n2
            elif op == '*':
                result = n1 * n2
            elif op == '/':
                if n2 == 0:
                    result = "Error: Division by zero"
                else:
                    result = n1 / n2
            else:
                result = "Invalid operation"
        except ValueError:
            result = "Invalid input, please enter numbers."

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000 , debug=True)
