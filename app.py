from atexit import register
import flask_login
from flask import Flask, render_template, session, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user

from User import User
from db import DB

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = DB()
login_manager = LoginManager()
login_manager.init_app(app)


# TODO
# Setup DB connections
# Setup HTML forms
# CSS?
# Handle POST requests
# Create views for all interactions
# ...

@login_manager.user_loader
def load_user(username):
    return User(username)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")


@app.route('/', methods=["GET"])
def index():
    if 'username' not in session:
        print("IMPLEMENT USERS")
    return render_template('index.html')


@app.route('/reception', methods=["GET"])
@login_required
def receptionist_portal():
    return render_template('reception.html')


@app.route('/users', methods=["GET"])
def show_users():
    if flask_login.current_user.role != "Patient" and flask_login.current_user.role != "ResponsibleUser":
        return render_template('patients.html', users=db.query('SELECT * FROM "User";')) #TODO NEED TO SPECIFY PATIENTS
    else:
        return redirect("/index")


@app.route('/reception/users/<int:id>', methods=["GET", "POST"])
def receptionist_edit(id):
    if request.method == 'POST':
        # Do the same as register redoing values as per form.
        print("NOT IMPLEMENTED YET...")
    else:
        # THIS NEEDS TO SPECIFY PATIENTS
        return render_template('editpatient.html', user=db.query('SELECT * FROM "User" WHERE "id"=' + str(id) + ';')[0])


@app.route('/records/users/<int:id>', methods=["GET", "POST"])
def records(id):
    if request.method == 'POST':
        # Do the same as register redoing values as per form.
        print("NOT IMPLEMENTED YET...")
    else:
        try:
            return render_template('records.html', record=db.query('SELECT * FROM "Records" WHERE "patient"=' + str(id) + ';')[0])
        except IndexError as e:
            return render_template('records.html', record='NA')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        try:
            actual_pass = db.query("SELECT password FROM \"User\" WHERE username LIKE '" + username + "';").pop()[0]
            if password == actual_pass:
                login_user(load_user(username), remember=True)
                print(flask_login.current_user.id)  # Print Current User's username
                return redirect("/reception")
            else:
                print("INVALID PASSWORD")

        except IndexError as e:
            print("NO SUCH USER")

    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username-field")
        password = request.form.get("password-field")
        first_name = request.form.get("firstName-field")
        last_name = request.form.get("lastName-field")
        middle_name = request.form.get("middleName-field")
        street_number = request.form.get("houseNumber-field", 0)
        apt_number = request.form.get("unitNumber-field", 0)
        street_name = request.form.get("street-field")
        zip_code = request.form.get("street-field")
        city = request.form.get("city-field")
        province = request.form.get("province-field")
        gender = request.form.get("gender-field")
        ssn = request.form.get("ssn-field")
        dob = request.form.get("dateOfBirth-field")
        phone = request.form.get("phoneNumber-field")

        try:
            db.query('INSERT INTO public."User" (username, password, first_name, middle_name, last_name, street_number, street_name, apt_number, city, province, zip_code, gender, ssn, phone, date_of_birth) VALUES' +
                     str((username, password, first_name, middle_name, last_name, street_number, street_name, apt_number, city, province, zip_code, gender, ssn, phone, dob)) + ';')

        except IndexError as e:
            print("FORM ERROR")

    return render_template('register.html')


if __name__ == '__main__':
    app.run()
