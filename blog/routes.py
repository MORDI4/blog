from flask import render_template, request, flash, redirect, url_for, session
from blog import app, db
from blog.models import Entry
from blog.forms import EntryForm, LoginForm
from datetime import datetime
import functools

@app.route('/', methods=['GET', 'POST'])
def index():
    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
    return render_template("homepage.html", all_posts=all_posts)

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

def login_required(view_func):
   @functools.wraps(view_func)
   def check_permissions(*args, **kwargs):
       if session.get('logged_in'):
           return view_func(*args, **kwargs)
       return redirect(url_for('login', next=request.path))
   return check_permissions
    


@app.route('/newpost', methods=['GET', 'POST'])
@login_required
def add_post():
    return handle_entry()


@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
@login_required
def edit_entry(entry_id):
   entry = Entry.query.filter_by(id=entry_id).first_or_404()
   return handle_entry(entry)

@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    errors = None
    next_url = request.args.get('next')
    if request.method == 'POST':
        if form.validate_on_submit():
            session['logged_in'] = True
            session.permanent = True
            flash('Jesteś teraz zalogowany.', 'success')
            return redirect(next_url or url_for('index'))
        else:
            errors = form.errors
    return render_template("login_form.html", form=form, errors=errors)

@app.route("/logout/")
def logout():
    session.clear()
    flash('Zostałeś wylogowany.', 'success')
    return redirect(url_for('index'))

@app.route("/drafts/")
@login_required
def drafts():
    all_drafts = Entry.query.filter_by(is_published=False).order_by(Entry.pub_date.desc())
    return render_template("draft.html", all_drafts=all_drafts)


    
