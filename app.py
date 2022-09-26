from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, make_response
from flask_session import Session
from flask_ngrok import run_with_ngrok
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from main import DynamicDeposit

from helpers import apology, format_price, login_required

# Configure application
app = Flask(__name__)
run_with_ngrok(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
#app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show portfolio of stocks"""

    # list of dictionaries and ordered by number
    client_contrats = db.execute(
        "SELECT number, subject, price, date FROM contracts WHERE client_id = ? ORDER BY date", session['client_id']
    )

    if request.method == 'POST':

        available = []

        t = request.form.get('date')
        s = request.form.get('price')
        #d1 = 
        # Day/mounth/year
        print(t)
        #t = [int(i) for i in t.split("-")]
        #print(datetime.date(t[0], t[1], t[2]))

        if client_contrats:
            for contract in client_contrats:
                perc = DynamicDeposit(contract['date'].split('-')[::-1], s, 1000000000).calc(t)
                uprice = int(s)
                parsed_dict = dict(
                    number = contract['number'],
                    subject = contract['subject'],
                    price = format_price(contract['price']),
                    contract_date = contract['date'],
                    user_date = t,
                    user_price = format(uprice, ','),
                    percentage = perc,
                    our_price = format((perc * uprice)//1, ',')
                )
                # add contract to list of current contracts
                available.append(parsed_dict)

        return render_template("calculated.html", contracts = available)

    else:
        # list of all contracts that company currently possess
        current_contracts = []

        # parse contracts
        if client_contrats:
            for contract in client_contrats:
                parsed_dict = dict(
                    number = contract['number'],
                    subject = contract['subject'],
                    price = format_price(contract['price']),
                    date = contract['date']
                )
                # add contract to list of current contracts
                current_contracts.append(parsed_dict)

        return render_template("index.html", contracts = current_contracts)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        if not request.form.get("code"):
            
            if request.form.get("code") == '':
                flash("must provide authentification code")
                return render_template("login.html")

            # Ensure username was submitted
            if not request.form.get("inn"):
                flash("must provide inn")
                return render_template("login.html")
                #return apology("must provide username", 400)

            # Ensure password was submitted
            elif not request.form.get("password"):
                flash("must provide password")
                return render_template("login.html")

            # Query database for username
            rows = db.execute("SELECT * FROM clients WHERE inn = ?", request.form.get("inn"))

            # Ensure username exists and password is correct
            if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
                flash("invalid inn and/or password")
                return render_template("login.html")

            # Remember which user has logged in
            resp = make_response(render_template("authentification.html"))
            resp.set_cookie('id', str(rows[0]["id"]))

            # Redirect user to home page
            return resp
        
        else:
            if request.form.get("code") != '1234':
                flash("wrong authentification code")
                return render_template("login.html")

            id = request.cookies.get('id')
            if id:
                session["client_id"] = id;
                resp = make_response()
                resp.set_cookie('id', '', expires=0)
                return redirect("/")
            else:
                return render_template("authentification.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # route via 'post' user clicked on the registration button
    if request.method == "POST":

        # render apology if username input field is blank
        if not request.form.get("inn"):
            flash("inn field can't be blank")
            return render_template("register.html")

        if not request.form.get("email"):
            flash("email field can't be blank")
            return render_template("register.html")

        # render apology if either password or confirmation field is blank
        if not request.form.get("password") or not request.form.get("confirmation"):
            flash("password field can't be blank")
            return render_template("register.html")

        # query database for username
        inn_db_query = db.execute("SELECT inn FROM clients WHERE inn = ?", request.form.get("inn"))

        # registrate user
        if len(inn_db_query) == 0:
            # insert new user into db, storing username and hash of the user's password
            if request.form.get("password") == request.form.get("confirmation"):
                db.execute("INSERT INTO clients (inn, email, hash) VALUES (?,?,?)", request.form.get(
                    "inn"), request.form.get("email") ,generate_password_hash(request.form.get("password")))
            # render apology if password confirmation dosen't match
            else:
                flash("passwords don't match")
                return render_template("register.html")
        # render apology if username is aready exists
        else:
            flash("inn is already exists")
            return render_template("register.html")

        # redirect users so they can login themselves
        return redirect("/")

    # route via 'get', by clicking on link or redirect
    else:
        return render_template("register.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)


if __name__ == "__main__":
    app.run()