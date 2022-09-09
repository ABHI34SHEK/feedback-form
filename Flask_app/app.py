from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] ='dc007a933a1fa9f7ec9d659a25c0423de03f0d8fb45f0db3'

messages = [{'title': 'Name',
             'content': 'Feedback'}
            ]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)
# ...

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['Name']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))
    return render_template('create.html')
if __name__ == '__main__':
   app.run(debug=True)