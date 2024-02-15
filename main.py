from flask import Flask, jsonify, request
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    # Ensure the request content type is JSON
    if request.is_json:
        # Parse the JSON into a Python dictionary
        data = request.get_json()

        # Now data is a Python dictionary
        print(data)
        fid = data.get(recipientFid, None)

        if(fid != None and fid < 100000):
            return jsonify({}), 200
        else:
            return jsonify({"error": "Invalid Fid"}), 400

    else:
        return jsonify({"error": "Request must be JSON"}), 400



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
