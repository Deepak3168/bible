from flask import Flask,render_template,request
from cs50 import SQL

app = Flask(__name__)


BOOKS = [
    "ఆదికాండము",
    "నిర్గమకాండము",
    "లేవీయకాండము",
    "సంఖ్యాకాండము",
    "ద్వితియోపదేశకాండము",
    "యెహోషువ",
    "న్యాయాధిపతులు",
    "రూతు",
    "1సమూయేలు",
    "2సమూయేలు",
    "1రాజులు",
    "2రాజులు",
    "1దినవృత్తాంతములు",
    "2దినవృత్తాంతములు",
    "ఎజ్రా",
    "నెహెమ్యా",
    "ఎస్తేరు",
    "యోబు",
    "కీర్తనలు",
    "సామెతలు",
    "ప్రసంగి",
    "పరమగీతము",
    "యెషయా",
    "యిర్మియా",
    "విలాపవాక్యములు",
    "యెహేజ్కేలు",
    "దానియేలు",
    "హోషేయా",
    "యోవేలు",
    "ఆమోసు",
    "ఓబద్యా",
    "యోనా",
    "మీకా",
    "నహూము",
    "హబక్కూకు",
    "జెఫన్యా",
    "హగ్గయి",
    "జెకర్యా",
    "మలాకీ",
    "మత్తయి",
    "మార్కు",
    "లూకా",
    "యోహాను",
    "అపో.కార్యములు",
    "రోమీయులకు",
    "1కోరింథీయులకు",
    "2కోరింథీయులకు",
    "గలతియులకు",
    "ఎఫెసీయులకు",
    "ఫిలిప్పీయులకు",
    "కొలస్సీయులకు",
    "1థెస్సలొనికయులకు",
    "2థెస్సలొనికయులకు",
    "1తిమోతికి",
    "2తిమోతికి",
    "తీతుకు",
    "ఫిలేమోనుకు",
    "హెబ్రీయులకు",
    "యాకోబు",
    "1పేతురు",
    "2పేతురు",
    "1యోహాను",
    "2యోహాను",
    "3యోహాను",
    "యూదా",
    "ప్రకటన గ్రంథం"
]
db = SQL("sqlite:///bible.db")



@app.route("/")
def index():
    return render_template("index.html",books=BOOKS)


@app.route("/getbible", methods=['GET', 'POST'])
def getbible():
    selected_book = request.args.get('book')
    if not selected_book:
        return render_template("error.html", message="THE BOOK IS NOT SELECTED")

    chapter_no = request.args.get("chapter_no")
    if not chapter_no:
        return render_template("error.html", message="THE CHAPTER NO IS MISSING ")

    verse_no = request.args.get("verse_no")
    if not verse_no:
        return render_template("error.html", message="THE VERSE NO IS MISSING")
    
    book_no = BOOKS.index(selected_book)

    v_result = db.execute(f"SELECT verse FROM bible WHERE Book = {book_no} AND Chapter = {chapter_no} ")
    result=[item["verse"] for item in v_result]
    return render_template("index.html", result=result,books=BOOKS,verse_no=verse_no)

