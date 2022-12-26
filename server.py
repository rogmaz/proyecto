from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/transform", methods=["POST"])
def transform_sentence():
    # Read the sentence from the request body
    sentence = request.json["sentence"]
    if sentence.isdigit():
    # Transform the sentence by changing its case
        transformed_sentence = str(int(sentence) + 1)
    else:
        transformed_sentence = sentence.upper()


    # Send an HTTP response to the client, including the transformed sentence in the response body
    return jsonify({"transformed_sentence": transformed_sentence})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)