from flask import Flask, redirect, render_template, request, session, flash, url_for, send_from_directory
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from flask_session import Session
from werkzeug.utils import secure_filename
from sam import login_required, dbCon, dbClose
import sqlite3
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)
load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['UPLOAD_FOLDER'] = "static/uploads"

Session(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/blog")
def blog():
    conn, c = dbCon()
    c.execute("SELECT * FROM blogPost ORDER BY date_posted DESC")
    blogs = c.fetchall()
    dbClose(conn, c)
    return render_template("blog.html", blogs=blogs)



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("Email and password required", "warning")

        

        if EMAIL != email or PASSWORD != password:
            flash("Invalid email or password", "warning")
            return redirect("/login")
        
        
        session["user_id"] = 1
        flash("You have been logged in!", "info")
        return redirect("/createBlog")
    else:    
        return render_template("login.html")

@app.route("/createBlog", methods=["GET", "POST"])
@login_required
def createBlog():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        content = request.form.get("content")
        # Handle the file upload if there's one
        file = request.files.get("image")
        image_url = None
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            # Ensure the UPLOAD_FOLDER exists
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            # Full path to where the file will be saved
            file_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename)
            # Save the file
            file.save(file_path)
            # The relative path to be stored in the database
            image_url = os.path.join('uploads', filename)
        else:
            print("No file part")

        conn, c = dbCon()
        try:
            c.execute("INSERT INTO blogPost (title, description, content, image_url, date_posted) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)", 
                      (title, description, content, image_url))
            conn.commit()
            flash("Blog post created successfully!", "success")
        except sqlite3.Error as e:
            print(f"An error occurred: {e.args[0]}")
            flash("An error occurred while creating the blog post.", "danger")
        finally:
            dbClose(conn, c)

        return redirect("/blog")
    else:
        return render_template("createBlog.html")

@app.route("/manage")
@login_required
def manageBlog():
        conn, c = dbCon()
        c.execute("SELECT * FROM blogPost")
        posts = c.fetchall()
        dbClose(conn, c)
        return render_template("manageBlog.html", posts=posts)

@app.route("/about")
def about():
    return render_template("aboutme.html")


@app.route("/delete-post/<int:post_id>", methods=["POST"])
@login_required
def delete_post(post_id):
    conn, c = dbCon()
    c.execute("DELETE FROM blogPost WHERE id = ?", (post_id,))
    conn.commit()
    dbClose(conn, c)
    flash("Blog post deleted successfully.", "success")
    return redirect("/manage")

@app.route("/blog/<int:post_id>")
def blog_post(post_id):
    conn, c = dbCon()
    c.execute("SELECT * FROM blogPost WHERE id = ?", (post_id,))
    post = c.fetchone()
    dbClose(conn, c)

    if post is None:
        flash("Blog post not found.", "warning")
        return redirect(url_for('blog'))

    return render_template("blog_post.html", post=post)


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out!", "info")
    return redirect("/")

@app.errorhandler(Exception)
def handle_error(error):
    return f"An error occurred: {str(error)}", 500

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'img', 'upload'), filename)



if __name__ == '__main__':
    app.run(debug=True)
