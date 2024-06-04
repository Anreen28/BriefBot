from flask import Flask, render_template, request
from text_sum import summarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    summary = ""
    orignal_text = ""
    len_or = 0
    len_sum = 0
    if request.method=='POST':
        rawtext = request.form['rawtext']
        summary,orignal_text, len_or, len_sum=summarizer(rawtext)

    return render_template('summary.html', summary =summary, orignal_text=orignal_text, len_or=len_or, len_sum=len_sum)    


if __name__ == "__main__":
    app.run(debug=True)
