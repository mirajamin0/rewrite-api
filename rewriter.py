from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/rewrite', methods=['POST'])
def rewrite():
    data = request.get_json()

    if 'content' not in data:
        return jsonify({'error': 'No content provided'}), 400

    content = data['content']
    # Basic rewriting logic (just an example)
    rewritten_content = content.replace("old word", "new word")

    return jsonify({'rewritten_content': rewritten_content})

# Add this to allow Vercel to handle the app properly
if __name__ == "__main__":
    app.run(debug=True)
