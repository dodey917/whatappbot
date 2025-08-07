from flask import Flask, request, jsonify
import os
from knowledge_base import get_response
from openai_integration import get_chatgpt_response

app = Flask(__name__)

# Configuration
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')  # Set this in your environment variables

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Verify the webhook
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        
        if mode and token:
            if mode == 'subscribe' and token == VERIFY_TOKEN:
                print("WEBHOOK VERIFIED")
                return challenge, 200
            else:
                return "Verification token mismatch", 403
        return "Invalid request", 400
    
    elif request.method == 'POST':
        # Handle incoming messages
        data = request.get_json()
        
        if data.get('object') == 'page':
            for entry in data.get('entry', []):
                for messaging_event in entry.get('messaging', []):
                    if messaging_event.get('message'):
                        sender_id = messaging_event['sender']['id']
                        message_text = messaging_event['message'].get('text', '')
                        
                        # First check knowledge base
                        custom_response = get_response(message_text)
                        
                        if custom_response:
                            # Send custom response
                            send_message(sender_id, custom_response)
                        else:
                            # Fall back to ChatGPT
                            chatgpt_response = get_chatgpt_response(message_text)
                            send_message(sender_id, chatgpt_response)
        
        return jsonify({'status': 'success'}), 200

def send_message(recipient_id, message_text):
    # This would actually send the message via WhatsApp API
    # In a real implementation, you'd use the WhatsApp Business API or a service like Twilio
    print(f"Sending to {recipient_id}: {message_text}")
    # Implement actual sending logic here

if __name__ == '__main__':
    app.run(port=5000, debug=True)
