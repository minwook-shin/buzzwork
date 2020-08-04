from flask import Flask, jsonify, request

from cache import init_cache
from slack_api.message import set_user_dm
from slack_api.user import search_user, set_user_status

app = Flask(__name__)
init_cache(app)


@app.route('/')
def index():
    return jsonify("True")


@app.route('/api/v1/user/<email>', methods=['GET'])
def user_api_v1(email):
    return jsonify(search_user(email))


@app.route('/api/v1/status/<email>', methods=['POST'])
def status_api_v1(email):
    user: dict = search_user(email)
    user_id = user["id"]
    status_text = request.get_json()["text"]
    status_emoji = request.get_json()["emoji"]
    return set_user_status(user_id, status_text, status_emoji)


@app.route('/api/v1/message/<email>', methods=['POST'])
def message_api_v1(email):
    user: dict = search_user(email)
    user_id = user["id"]
    status_text = request.get_json()["text"]
    return set_user_dm(user_id, status_text)


if __name__ == '__main__':
    app.run(debug=True)
