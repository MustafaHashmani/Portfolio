from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__, template_folder="templates")


@app.route("/")
def my_home():
    return render_template("index.html")


# dynamic rendering
@app.route("/<string:page_name>")
# for every page name, render that page
def html_page(page_name):
    return render_template(page_name)


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            # convert data from form to a dictionary
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "did not save to database"
    else:
        return "something went wrong"


def write_to_file(data):
    """Writes the email,subject and message to a txt file"""
    with open("./database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    """Writes the email,subject and message to a csv file"""
    with open("./database.csv", mode="a", newline="") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=",")
        csv_writer.writerow([email, subject, message])
