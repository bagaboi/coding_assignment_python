# import awsgi
from flask import Flask, request, jsonify

app= Flask(__name__)

@app.route('/check_string_alphabets',methods=['POST'])
def check_string_alphabets():
    """
    Reading a JSON request containing a 'text' field (string) and checks if all letters of the alphabet (a-z, case-insensitive) are present in the string
    Returns: JSON response:
    - 'result': True if all letters are present, False otherwise
    - 'error': Error message incase there is any other exception of payload not being passed correctly
    """
    try:
        data=request.get_json()
        s=data['text'].lower()
        alphabets=set("abcdefghijklmnopqrstuvwxyz")
        is_present=True
        for a in alphabets:
            if a not in s:
                is_present = False
                return jsonify({'result':is_present})
        return jsonify({'result':is_present})
    except Exception as e:
        return jsonify({'error':str(e)}), 500

# def lambda_handler(event, context):
#     return awsgi.response(app, event, context, base64_content_types={"image/png"})
