# ui/web.py
from flask import Flask, render_template_string, redirect, url_for, request, flash
from sentinellite import pull_feeds, scan_logs
from pathlib import Path

app = Flask(__name__)
app.secret_key = "sentinellite-secret"

TPL = """
<!doctype html>
<title>SentinelLite UI</title>
<link rel="stylesheet" href="https://cdn.simplecss.org/simple.min.css">
<main>
  <h1>🛡️ SentinelLite</h1>
  <p>Basic controls to pull feeds, scan logs, and read the latest digest.</p>
  <form method="post" action="/action">
    <button name="action" value="pull">Pull Feeds</button>
    <button name="action" value="scan">Scan Logs</button>
    <button name="action" value="read">Read Latest Digest</button>
  </form>
  {% with messages = get_flashed_messages() %}
    {% if messages %}
      <ul>
      {% for m in messages %}<li>{{ m }}</li>{% endfor %}
      </ul>
    {% endif %}
  {% endwith %}
  {% if digest %}
  <h2>{{ digest_name }}</h2>
  <pre style="white-space: pre-wrap;">{{ digest }}</pre>
  {% endif %}
</main>
"""

@app.route("/")
def index():
    return render_template_string(TPL, digest="", digest_name="")

@app.route("/action", methods=["POST"])
def action():
    act = request.form.get("action")
    if act == "pull":
        pull_feeds()
        flash("Feeds pulled and consolidated.")
        return redirect(url_for("index"))
    elif act == "scan":
        scan_logs()
        flash("Scan complete; digest generated.")
        return redirect(url_for("index"))
    elif act == "read":
        dig_dir = Path("output/digests")
        latest = sorted(dig_dir.glob("threat_digest_*.md"))[-1] if dig_dir.exists() else None
        if latest:
            return render_template_string(TPL, digest=latest.read_text(), digest_name=latest.name)
        else:
            flash("No digest found. Run a scan first.")
            return redirect(url_for("index"))
    else:
        flash("Unknown action.")
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
