from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Sample contact groups with SIP addresses
contacts = {
    "tech_admins": [
        {"name": "Kevin Adams", "email": "kevin.adams@bcsdk12.net", "contact_title": "Tech Lead"},
        {"name": "Dara Foy", "email": "dara.foy@bcsdk12.net", "contact_title": "System Administrator"},
    ],
    "project_contacts": [
        {"name": "Carlos Madera", "email": "carlos.madera@bcsdk12.net", "contact_title": "Project Manager"},
        {"name": "Joseph Taylor", "email": "joseph.taylor@bcsdk12.net", "contact_title": "Project Coordinator"},
    ],
    "cdw_contacts": [
        {"name": "Aubrey England", "email": "aubreng@cdw.com", "contact_title": "Account Manager"},
        {"name": "Mike Robinson", "email": "mike.robinson@cdw.com", "contact_title": "Sales Representative"},
        {"name": "Brennan Geis", "email": "brennan.geis@cdw.com", "contact_title": "Solution Architect"},
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/contacts/<group>')
def get_contacts(group):
    return jsonify(contacts.get(group, []))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)