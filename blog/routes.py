from flask import render_template, request, flash, redirect, url_for
from blog import app, db
from blog.models import Entry
from .forms import EntryForm
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def index():
    form = EntryForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            pass
        else:
            error = form.errors

    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())

    return render_template("homepage.html", all_posts=all_posts, form=form, error=error)

def handle_entry(entry=None):
    if entry == None:
        form = EntryForm()
        entry = Entry()
        is_new = True
    else:
        form = EntryForm(obj=entry)
        is_new = False
    
    errors = ""
    if form.validate_on_submit():
        form.populate_obj(entry)
        if is_new:
            entry.pub_date = datetime.now()
            db.session.add(entry)
            flash("Blog został dodany.", "success")
        else:
            flash("Blog został zaktualizowany.", "success")
        db.session.commit()
        return redirect(url_for("index"))
    elif request.method == "POST":
        errors = form.errors

    return render_template("entry_form.html", form=form, errors=errors, is_new=is_new)
    


@app.route('/newpost', methods=['GET', 'POST'])
def add_post():
    return handle_entry()


@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
   entry = Entry.query.filter_by(id=entry_id).first_or_404()
   return handle_entry(entry)
