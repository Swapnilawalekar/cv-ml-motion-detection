from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/event', methods=['POST'])
def receive_event():
    event = request.json
    print("Event received from CV app:")
    print(event)
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
