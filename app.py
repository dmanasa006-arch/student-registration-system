from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

CSV_FILE = "students.csv"

# Create CSV file if not exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["username", "password"])


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# User Type Page
@app.route("/user-type")
def user_type():
    return render_template("user_type.html")


# Register New User
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"].strip()
        password = request.form["password"].strip()

        # Save into CSV
        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, password])

        return render_template(
            "success.html",
            username=username,
            message="successfully has been registered"
        )

    return render_template("register.html")


# Login Existing User
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"].strip().lower()
        password = request.form["password"].strip()

        with open(CSV_FILE, "r") as file:

            reader = csv.reader(file)

            next(reader)

            for row in reader:

                if len(row) >= 2:

                    csv_username = row[0].strip().lower()
                    csv_password = row[1].strip()

                    if (
                        csv_username == username
                        and csv_password == password
                    ):

                        return render_template(
                            "success.html",
                            username=csv_username,
                            message="Welcome... back to IIT. "
                        )

        return render_template(
            "login.html",
            error="Invalid User ID or Password"
        )

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)