from flask import Flask, request, jsonify
import jwt 

app = Flask(__name__)

@app.route('/api/report', methods=['GET'])
def get_report():
    token = request.headers.get('Authorization', '').split('Bearer ')[-1]
    if not token:
        return "Unauthorized", 401

    try:
        decoded = jwt.decode(token, options={"verify_signature": False})
        
        # Check if the user has the 'admin' role
        if 'admin' not in decoded.get('roles', []):
            return jsonify(message="Forbidden: You do not have access to this resource"), 403
        
        return jsonify(message=f"Hello {decoded['preferred_username']}, here’s your report!")
    except Exception as e:
        return str(e), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
