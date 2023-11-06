from flask import Flask , request , jsonify , send_file ,  render_template 
import tinydb
import uuid


launches = tinydb.TinyDB("./db/files/launches.json")
projects = tinydb.TinyDB("./db/files/projects.json")
teams = tinydb.TinyDB("./db/files/teams.json")

app = Flask(__name__)


@app.get("/")
def index():
    return "this is TheAlphaOnes web backend data service"

# ALL API ROUTES WILL START FROM /api/name
# FOR THE DATA SENDING

@app.route("/api/all-page",methods=['GET','POST'])
def all_data_main():
    data_launches = launches.all()
    data_projects = projects.all()
    data_teams = teams.all()
    data = {
        "launches":data_launches,
        "projects":data_projects,
        "teams":data_teams,
    }
    return jsonify(data)

@app.route("/api/launches-page",methods=['GET','POST'])
def launches_data():
    data_launches = launches.all()
    return jsonify(data_launches)

@app.route("/api/projects-page",methods=['GET','POST'])
def projects_data():
    data_projects = projects.all()
    return jsonify(data_projects)

@app.route("/api/teams-page",methods=['GET','POST'])
def teams_data():
    data_teams = teams.all()
    return jsonify(data_teams)

@app.get("/api/image/<name>",methods=['GET','POST'])
def send_asset(name):
    return send_file("./db/assets/"+name)



# FOR THE DATA INSERTING 

@app.route("/user/admin/teams-add",methods=['GET','POST'])
def teams_add():
    return ""

@app.route("/user/admin/projects-add",methods=['GET','POST'])
def projects_add():
    return ""

@app.route("/user/admin/launches-add",methods=['GET','POST'])
def launches_add():
    return ""


if __name__ == "__main__":
    app.run(debug=True)
