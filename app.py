from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# TODO
# Setup DB connections
# Setup HTML forms
# CSS?
# Handle POST requests
# Create views for all interactions
# ...

@app.route('/', methods=["GET"])
def index():
    if 'username' not in session:
        print("IMPLEMENT USERS")
    return render_template('index.html')


@app.route('/reception', methods=["GET"])
def receptionist_portal():
    return render_template('reception.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Connect to db and check credentials
        correct_creds = True
        if correct_creds:
            session['username'] = request.form['username']

            return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
