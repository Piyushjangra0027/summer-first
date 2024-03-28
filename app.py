from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Variables to store the input data
mark1 = ""
mark2 = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    global mark1, mark2
    if request.method == 'POST':
        mark1 = request.form.get('mark1')
        mark2 = request.form.get('mark2')
        return 'Data submitted successfully!'
    else:
        return render_template('index.html')

@app.route('/get_marks', methods=['GET'])
def get_marks():
    global mark1, mark2
    return jsonify({'mark1': mark1, 'mark2': mark2})

print (mark1)


if __name__ == '__main__':
    app.run(debug=True)
