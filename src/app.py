# src/app.py
from flask import Flask, jsonify, request
from src.datastructure import FamilyStructure

app = Flask(__name__)
jackson_family = FamilyStructure("Jackson")

@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404

@app.route('/member', methods=['POST'])
def add_member():
    if request.is_json:
        data = request.json
        jackson_family.add_member(data)
        return jsonify({"message": "Member added successfully"}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    if jackson_family.delete_member(member_id):
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Member not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
