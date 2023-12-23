import os
import requests
import urllib.parse
from functools import wraps
from flask import Flask, flash, redirect, render_template, request, session
from flask_bcrypt import Bcrypt
import bcrypt
import requests
from flask_session import Session
import random 
import sqlite3


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def dbCon():
    conn = sqlite3.connect("blog.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    return conn, c


def dbClose(conn, cursor=None):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def createDb():
    conn = sqlite3.connect("blog.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("""CREATE TABLE blogPost (id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    content TEXT NOT NULL,
    date_posted DATETIME NOT NULL,
    image_url VARCHAR(255));""")

#createDb()