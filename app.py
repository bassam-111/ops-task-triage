"""Minimal Flask UI for Ops Task Triage."""

from flask import Flask, request, render_template_string

from triage import triage

app = Flask(__name__)

PAGE = """
<!doctype html>
<title>Ops Task Triage</title>
<h1>Ops Task Triage</h1>
<form method="post">
  <textarea name="task" rows="4" cols="70" placeholder="Paste a task or client message here..."></textarea><br>
  <button type="submit">Triage</button>
</form>
{% if result %}
  <h2>Result</h2>
  <p><b>Category:</b> {{ result.category }} &nbsp; <b>Priority:</b> {{ result.priority }}</p>
  <p><b>Next action:</b> {{ result.next_action }}</p>
  <p><b>Draft follow-up:</b> {{ result.draft_follow_up }}</p>
{% endif %}
"""


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        result = triage(request.form.get("task", ""))
    return render_template_string(PAGE, result=result)


if __name__ == "__main__":
    app.run(debug=True)
