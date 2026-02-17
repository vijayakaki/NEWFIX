import os
from flask import Flask, request, jsonify
from openai import OpenAI
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize AI clients
openai_client = None
anthropic_client = None

try:
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if openai_api_key:
        openai_client = OpenAI(api_key=openai_api_key)
except Exception as e:
    print(f"OpenAI initialization error: {e}")

try:
    claude_api_key = os.getenv('CLAUDE_API_KEY')
    if claude_api_key:
        anthropic_client = Anthropic(api_key=claude_api_key)
except Exception as e:
    print(f"Claude initialization error: {e}")

@app.route('/api/ai/status', methods=['GET'])
def status():
    return jsonify({
        'openai_available': openai_client is not None,
        'claude_available': anthropic_client is not None
    })

@app.route('/api/ai/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    provider = data.get('provider', 'openai')
    if not user_message:
        return jsonify({'error': 'Message is required'}), 400
    system_prompt = "You are an expert AI assistant for the FIX$ GeoEquity Impact Engine. Help users understand EJV calculations and economic impact."
    try:
        if provider == 'claude' and anthropic_client:
            response = anthropic_client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=500,
                system=system_prompt,
                messages=[{"role": "user", "content": user_message}]
            )
            return jsonify({'response': response.content[0].text, 'provider': 'claude'})
        elif openai_client:
            response = openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_message}],
                temperature=0.7,
                max_tokens=500
            )
            return jsonify({'response': response.choices[0].message.content, 'provider': 'openai'})
        else:
            return jsonify({'error': 'No AI provider available'}), 503
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Vercel entrypoint
app = app
