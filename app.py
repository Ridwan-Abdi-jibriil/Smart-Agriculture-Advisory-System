from flask import Flask, render_template, request, redirect, session
from google import genai
from tenacity import retry, stop_after_attempt, wait_exponential
import mysql.connector
import markdown

app = Flask(__name__)
app.secret_key = "smart_agriculture_secret"

# GEMINI
client = genai.Client(
    api_key="AIzaSyATQ7Uy0UDFZjQJzXZMuM1Qcq34B9TQul8"
)

MODEL = "gemini-flash-lite-latest"


# MYSQL CONNECTION
def get_db_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="smart_agriculture"
    )

    return conn


# GEMINI RETRY
@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=2, max=10)
)
def generate_response(prompt):

    return client.models.generate_content(
        model=MODEL,
        contents=prompt
    )


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT * FROM users
            WHERE email=%s AND password=%s
            """,
            (email, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            session["user_id"] = user["id"]
            session["fullname"] = user["fullname"]

            return redirect("/dashboard")

    return render_template("login.html")


# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users(fullname, email, password)
            VALUES(%s, %s, %s)
            """,
            (fullname, email, password)
        )

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")


# LOGOUT
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


# HOME PAGE
@app.route("/")
def home():

    if "user_id" not in session:
        return redirect("/login")

    return render_template("index.html")


# RECOMMENDATION
@app.route("/recommend", methods=["POST"])
def recommend():

    if "user_id" not in session:
        return redirect("/login")

    soil = request.form["soil"]
    weather = request.form["weather"]
    rainfall = request.form["rainfall"]
    temperature = request.form["temperature"]
    location = request.form["location"]

    if soil == "Other":
        soil = request.form["custom_soil"]

    prompt = f"""
    Give farming recommendations for:

    Soil Type: {soil}
    Weather: {weather}
    Rainfall: {rainfall}
    Temperature: {temperature}
    Location: {location}

    Provide:
    1. Best crop
    2. Fertilizer recommendation
    3. Irrigation advice
    4. Planting period
    5. Disease risk
    """

    try:

        response = generate_response(prompt)

        result = markdown.markdown(
            response.text,
            extensions=[
                "fenced_code",
                "tables",
                "nl2br"
            ]
        )

    except Exception:

        result = "AI service is temporarily unavailable."

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO recommendations
        (user_id, soil, weather, rainfall, temperature, location, result)
        VALUES(%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            session["user_id"],
            soil,
            weather,
            rainfall,
            temperature,
            location,
            result
        )
    )

    conn.commit()
    conn.close()

    return render_template("result.html", result=result)


# DASHBOARD
@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT COUNT(*) AS total
        FROM recommendations
        WHERE user_id=%s
        """,
        (session["user_id"],)
    )

    total = cursor.fetchone()

    conn.close()

    return render_template(
        "dashboard.html",
        total=total["total"]
    )


# HISTORY
@app.route("/history")
def history():

    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM recommendations
        WHERE user_id=%s
        ORDER BY id DESC
        """,
        (session["user_id"],)
    )

    recommendations = cursor.fetchall()

    conn.close()

    return render_template(
        "history.html",
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)