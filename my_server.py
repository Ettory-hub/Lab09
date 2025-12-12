from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

TOKENS = {}

def _get_data():
    data = request.get_json(silent=True)
    if isinstance(data, dict):
        return data
    return request.form.to_dict() if request.form else {}

@app.get("/health")
def health():
    return jsonify(ok=True)


@app.get("/")
def index():
    return jsonify(ok=True, routes=["/health", "/login", "/verify"]) 

@app.post("/login")
def login():
    data = _get_data()
    user_id = (data.get("id") or "").strip()
    if not user_id:
        return jsonify(ok=False, error="Missing 'id'"), 400

    token = str(uuid.uuid4())
    TOKENS[user_id] = token
    return jsonify(ok=True, id=user_id, uuid_token=token)

@app.post("/verify")
def verify():
    data = _get_data()
    user_id = (data.get("id") or "").strip()
    token = (data.get("uuid-token") or data.get("uuid_token") or "").strip()

    if not user_id or not token:
        return jsonify(ok=False, valid=False, error="Missing 'id' or 'uuid-token'"), 400

    valid = TOKENS.get(user_id) == token
    return jsonify(ok=True, valid=valid)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
