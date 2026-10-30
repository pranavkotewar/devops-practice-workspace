from flask import Flask, jsonify, redirect, render_template_string, request, url_for
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_prefix=1)

NOTES = [{"id": 1, "text": "Welcome to the Flask demo"}]

PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Flask Notes</title>
<style>
body{font-family:Segoe UI,Arial,sans-serif;background:#0b1220;color:#e2e8f0;max-width:560px;margin:8vh auto;padding:0 16px}
h1{color:#34d399}
form{display:flex;gap:8px;margin-bottom:18px}
input{flex:1;padding:10px;border-radius:6px;border:1px solid #334155;background:#111827;color:#e2e8f0}
button{padding:10px 16px;border:0;border-radius:6px;background:#10b981;color:#04130e;font-weight:600;cursor:pointer}
li{display:flex;justify-content:space-between;background:#111827;margin:8px 0;padding:10px 14px;border-radius:8px}
a{color:#f87171;text-decoration:none}
.small{color:#64748b;font-size:12px}
</style></head>
<body>
<h1>Flask Notes</h1>
<form method="post" action="{{ url_for('add') }}">
  <input name="text" placeholder="Write a note" required>
  <button type="submit">Add</button>
</form>
<ul>
{% for n in notes %}
  <li><span>{{ n.text }}</span><a href="{{ url_for('delete', note_id=n.id) }}">delete</a></li>
{% endfor %}
</ul>
<p class="small">API: <a style="color:#60a5fa" href="{{ url_for('api_notes') }}">notes as JSON</a></p>
</body></html>"""


@app.route("/")
def index():
    return render_template_string(PAGE, notes=NOTES)


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text", "").strip()
    if text:
        NOTES.append({"id": max([n["id"] for n in NOTES] + [0]) + 1, "text": text[:200]})
    return redirect(url_for("index"))


@app.route("/delete/<int:note_id>")
def delete(note_id):
    NOTES[:] = [n for n in NOTES if n["id"] != note_id]
    return redirect(url_for("index"))


@app.route("/api/notes")
def api_notes():
    return jsonify(NOTES)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
