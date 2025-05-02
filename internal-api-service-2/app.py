from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/report', methods=['GET'])
def get_report():
    return jsonify(message="You have access to the REPORT endpoint (RBAC success).")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
