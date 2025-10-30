from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_PATH = "vulnerable.db"

def get_db():
  conn = sqlite3.connect(DB_PATH)
  conn.row_factory = sqlite3.Row
  return conn

@app.route('/')
def home():
  return "Lab 1: API vulnerable a SQL Injection"

@app.route('/user')
def get_user():
  name = request.args.get('name', '')
  conn = get_db()
  cur = conn.cursor()
  cur.execute("SELECT id, name, email FROM users WHERE name = ?", (name,))
  rows = cur.fetchall()
  result = [dict(row) for row in rows]
  conn.close()
  return jsonify(result)

if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0', port=5000)
