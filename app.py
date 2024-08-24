from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Endpoint to receive notifications from the Discord bot
@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    message = data.get('message', 'No message provided')
    
    # Process the data or log it
    print(f"Received notification: {message}")
    
    # You can add logic to handle different types of messages or trigger other processes
    # For now, just return a success response
    return jsonify({"status": "success", "message": "Notification received"}), 200

# Default route
@app.route('/')
def index():
    return "Flask app is running!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
