from flask import Flask, render_template

app = Flask(__name__)

full_name = "Adam Tester"
github_link = "https://github.com/adamgoodhandle"

@app.route("/about_me")
def about_me():
    return render_template(
        'about_me.html',
        full_name=full_name,
        job_role="IS Business Analysis Apprentice",
        intro_text="Qualified product design engineer and aspring techy coder. (Whatever that means!)",
        linkedin_link="TODO",
        github_link=github_link
    )

@app.route("/experience")
def experience():
    return render_template(
        "experience.html",
        full_name=full_name,
        linkedin_link="TODO",
        github_link=github_link
    )

app.run(debug=True)