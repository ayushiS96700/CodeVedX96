from flask import Flask, render_template, request, jsonify
import json
import re
import random

app = Flask(__name__)

INTENTS_FILE = 'intents.json'

def load_intents():
    try:
        with open(INTENTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"intents": []}

def save_intents(data):
    with open(INTENTS_FILE, 'w') as file:
        json.dump(data, file, indent=2)

def get_bot_response(user_message):
    data = load_intents()
    user_msg_clean = re.sub(r'[^\w\s]', '', user_message.lower()).strip()
    
    best_match_tag = None
    max_score = 0
    
    for intent in data.get('intents', []):
        for pattern in intent.get('patterns', []):
            pattern_clean = re.sub(r'[^\w\s]', '', pattern.lower()).strip()
            
            words_in_pattern = pattern_clean.split()
            matched_words = sum(1 for word in words_in_pattern if word in user_msg_clean.split())
            
            if matched_words > max_score:
                max_score = matched_words
                best_match_tag = intent

    if best_match_tag and max_score > 0:
        return random.choice(best_match_tag['responses'])
    else:
        return "Sorry, I couldn't understand that. You can contact IT Support directly or ask the Admin to add this question."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'response': 'Please enter a valid message.'})
    
    bot_reply = get_bot_response(user_message)
    return jsonify({'response': bot_reply})

@app.route('/admin/add_intent', methods=['POST'])
def add_intent():
    req_data = request.json
    tag = req_data.get('tag')
    patterns = req_data.get('patterns')
    responses = req_data.get('responses') 

    if not tag or not patterns or not responses:
        return jsonify({'status': 'error', 'message': 'All fields are required!'}), 400

    data = load_intents()
    
    pattern_list = [p.strip() for p in patterns.split(',')] if isinstance(patterns, str) else patterns
    response_list = [r.strip() for r in responses.split(',')] if isinstance(responses, str) else responses

    existing_intent = next((item for item in data['intents'] if item['tag'] == tag), None)
    if existing_intent:
        existing_intent['patterns'].extend(pattern_list)
        existing_intent['responses'].extend(response_list)
    else:
        data['intents'].append({
            "tag": tag,
            "patterns": pattern_list,
            "responses": response_list
        })

    save_intents(data)
    return jsonify({'status': 'success', 'message': f"Intent '{tag}' updated/added successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

