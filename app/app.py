from flask import Flask, render_template, request, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input-text']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        flash('Input: {}, Time: {}'.format(input_text, timestamp))
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
