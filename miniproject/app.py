from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)
DATA_FILE = 'config.json'

def load_config():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_config(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        updated_data = request.form.to_dict()
        save_config(updated_data)
        return redirect('/')  # reload to show updated values
    data = load_config()
    return render_template('form.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
