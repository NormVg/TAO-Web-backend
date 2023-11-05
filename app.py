from flask import Flask , request , jsonify , send_file ,  render_template 
import tinydb

launches = tinydb.TinyDB("./db/files/launches.json")
projects = tinydb.TinyDB("./db/files/projects.json")
teams = tinydb.TinyDB("./db/files/teams.json")

app = Flask(__name__)


@app.get("/")
def index():
    return "this is TheAlphaOnes web backend data service"

# ALL API ROUTES WILL START FROM /api/name
# FOR THE DATA SENDING


# FOR THE DATA INSERTING 



if __name__ == "__main__":
    app.run(debug=True)
