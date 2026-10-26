from flask import Blueprint, render_template, request

main = Blueprint("main", __name__)

@main.route("/", methods=["GET","POST"])
def home():

    message =""

    if request.method == "POST":
        username = request.form.get("username")
        if username == "Harini":
            message = f"Hello {username}, Collector Madam!"
        elif username == "Raji":
            message = f"Hello {username}, Developer!"   
        elif username == "Murugan":
            message = f"Hello {username}, IPS Sir!"
        elif username == "Kumaran":
            message = f"Hello {username}, Doctor Sir!"
        elif username == "Palani":
            message = f"Hello {username}, Doctor Sir!"
        else:
            message = f"Hello {username}, Welcome!"

    return render_template("index.html", message = message)
    