import json
import os

from flask import Flask, jsonify, redirect, render_template, request, url_for


app = Flask(__name__)
app.secret_key = os.urandom(24)

CONTACTS_FILE = os.path.join(os.path.dirname(__file__), "contacts.json")


def load_contacts():
    with open(CONTACTS_FILE) as f:
        return json.load(f)


def save_contacts(data):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(data, f, indent=2)


@app.route("/admin")
def admin_panel():
    contacts = load_contacts()
    return render_template("admin.html", contacts=contacts)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/contacts/<group>')
def get_contacts(group):
    contacts = load_contacts()
    return jsonify(contacts.get(group, []))


@app.route("/api/groups")
def get_groups():
    contacts = load_contacts()
    return jsonify(list(contacts.keys()))


@app.route("/admin/add_contact", methods=["POST"])
def add_contact():
    group = request.form.get("group")
    name = request.form.get("name")
    sip = request.form.get("sip")
    
    contacts = load_contacts()
    if group in contacts:
        contacts[group].append({"name": name, "sip": sip})
        save_contacts(contacts)
    
    return redirect(url_for("admin_panel"))


@app.route("/admin/delete_contact", methods=["POST"])
def delete_contact():
    group = request.form.get("group")
    index = int(request.form.get("index", -1))
    
    contacts = load_contacts()
    if group in contacts and 0 <= index < len(contacts[group]):
        contacts[group].pop(index)
        save_contacts(contacts)
    
    return redirect(url_for("admin_panel"))


@app.route("/admin/add_group", methods=["POST"])
def add_group():
    group = request.form.get("group", "").strip().lower().replace(" ", "_")
    
    contacts = load_contacts()
    if group and group not in contacts:
        contacts[group] = []
        save_contacts(contacts)
    
    return redirect(url_for("admin_panel"))


@app.route("/admin/delete_group", methods=["POST"])
def delete_group():
    group = request.form.get("group")
    
    contacts = load_contacts()
    if group in contacts:
        del contacts[group]
        save_contacts(contacts)
    
    return redirect(url_for("admin_panel"))


import json
import os

from flask import Flask, jsonify, redirect, render_template, request, url_for


app = Flask(__name__)
app.secret_key = os.urandom(24)

CONTACTS_FILE = os.path.join(os.path.dirname(__file__), "contacts.json")


def load_contacts():
    with open(CONTACTS_FILE) as f:
        return json.load(f)


def save_contacts(data):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(data, f, indent=2)


@app.route("/admin")
def admin_panel():
    contacts = load_contacts()
    return render_template("admin.html", contacts=contacts)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/contacts/<group>')
def get_contacts(group):
    contacts = load_contacts()
    return jsonify(contacts.get(group, []))


@app.route("/api/groups")
def get_groups():
    contacts = load_contacts()
    return jsonify(list(contacts.keys()))


@app.route("/admin/add_contact", methods=["POST"])
def add_contact():
    group = request.form.get("group")
    name = request.form.get("name")
    title = request.form.get("title")
    email = request.form.get("email")
    
    contacts = load_contacts()
    if group in contacts:
        contacts[group].append({"name": name, "title": title, "email": email})
        save_contacts(contacts)
    
    return redirect(url_for("admin_panel"))


@app.route("/admin/delete_contact", methods=["POST"])
def delete_contact():
    group = request.form.get("group")
    index = int(request.form.get("index", -1))
    
    contacts = load_contacts()
    if group in contacts and 0 <= index < len(contacts[group]):
        contacts[group].pop(index)
        save_contacts(contacts)
    
    return redirect(url_for("admin_panel"))


@app.route("/admin/add_group", methods=["POST"])
def add_group():
    group = request.form.get("group", "").strip().lower().replace(" ", "_")
    
    contacts = load_contacts()
    if group and group not in contacts:
        contacts[group] = []
        save_contacts(contacts)
    
    return redirect(url_for("admin_panel"))


@app.route("/admin/delete_group", methods=["POST"])
def delete_group():
    group = request.form.get("group")
    
    contacts = load_contacts()
    if group in contacts:
        del contacts[group]
        save_contacts(contacts)
    
    return redirect(url_for("admin_panel"))

@app.route("/admin/edit_contact", methods=["POST"])
def edit_contact():
    group = request.form.get("group")
    index = int(request.form.get("index", -1))
    name = request.form.get("name")
    title = request.form.get("title")
    email = request.form.get("email")

    contacts = load_contacts()
    if group in contacts and 0 <= index < len(contacts[group]):
        contacts[group][index] = {"name": name, "title": title, "email": email}
        save_contacts(contacts)

    return redirect(url_for("admin_panel"))

@app.route("/admin/rename_group", methods=["POST"])
def rename_group():
    old_group = request.form.get("old_group")
    new_group = request.form.get("new_group", "").strip().lower().replace(" ", "_")

    contacts = load_contacts()
    if old_group in contacts and new_group and new_group not in contacts:
        contacts[new_group] = contacts.pop(old_group)
        save_contacts(contacts)

    return redirect(url_for("admin_panel"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)