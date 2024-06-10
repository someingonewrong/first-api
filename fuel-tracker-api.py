from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/New_Entry')
def New_Input():
    return render_template('New_Entry.html')

@app.route('/Import_CSV')
def CSV_Import():
    return render_template('Import_CSV.html')

@app.route('/View_Data')
def View_Data():
    return render_template('View_Data.html')

@app.route('/SQL_Query')
def SQL_Query():
    return render_template('SQL_Query.html')