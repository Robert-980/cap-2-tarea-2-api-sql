import sqlite3
from flask import Flask, render_template, abort, request, url_for, jsonify
from tkinter import*
import tkinter as tk

# from db import get_db_connection

# Se agrega esta linea

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

#------------------------------------

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Welcome to the API - Tarea Nro2"})

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/base", methods=["GET"])
def base():
    return render_template('base.html')

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/post', methods=['GET'])
def get_all_post():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM database').fetchall()
    conn.close()
    posts_lists = [dict(post) for post in posts]
    return jsonify(posts_lists)

@app.route('/post/<int:post_id>', methods=['GET'])
def get_one_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM database WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404, description="Post not found")
    return jsonify(dict(post))

@app.route('/post/create', methods=['POST'])
def create_one_post():
    data = request.json
    title = data.get('title')
    content = data.get('content')

    conn = get_db_connection()
    conn.execute('INSERT INTO database (title, content) VALUES (?, ?)', (title, content))
    conn.commit()
    conn.close()
    return jsonify({"message": "Post created"})

@app.route('/post/edit/<int:post_id>', methods=['PUT'])
def edit_one_post(post_id):
    data = request.json
    title = data.get('title')
    content = data.get('content')

    conn = get_db_connection()
    conn.execute('UPDATE database SET title = ?, content = ? WHERE id = ?', (title, content, post_id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Post updated"})


@app.route("/post/delete/<int:post_id>", methods=["POST"])
def delete_one_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM database WHERE id = ?', (post_id,)).fetchone()
    
    if post is None:
        abort(404)

    conn.execute('DELETE FROM database WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('get_all_posts'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
########################################################################## END BLOQUE 2

