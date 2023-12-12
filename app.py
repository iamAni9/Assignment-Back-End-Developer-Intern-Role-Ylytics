from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
BASE_URL = "https://app.ylytic.com/ylytic/test"  # Your base URL for the existing API

@app.route('/search', methods=['GET'])
def search_comments():
    # Extract query parameters from the URL
    author = request.args.get('author')
    at = request.args.get('at')
    like = request.args.get('like')
    reply = request.args.get('reply')
    text = request.args.get('text')

    # Construct parameters for the existing API request
    params = {}

    if author:
        params['author'] = author

    if at:
        params['at'] = at

    # if at_to:
    #     params['at_to'] = at_to

    if like:
        params['like'] = like

    # if like_to:
    #     params['like_to'] = like_to

    if reply:
        params['reply'] = reply

    # if reply_to:
    #     params['reply_to'] = reply_to

    if text:
        params['text'] = text

    for i, j in params.items():
        print(type(i), type(j))
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        for key, val in params.items():
            filtered_comments = []
            for item in data['comments']:
                # print(type(item[key]))
                if str(item[key]) == val:
                    filtered_comments.append(item)
            data['comments'] = filtered_comments
                    
        return jsonify(data)
    else:
        return jsonify({'message': 'Error occurred while fetching comments'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=4000)