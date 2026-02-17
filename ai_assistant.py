"""
AI Assistant API endpoint for FIX$ Application
Provides intelligent assistance for EJV calculations and store analysis
"""

import os
from flask import jsonify, request
from openai import OpenAI
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

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


def ai_assistant():
    """Handle AI assistant chat requests"""
    try:
        data = request.json
        user_message = data.get('message', '')
        context = data.get('context', {})  # Store data, EJV scores, etc.
        provider = data.get('provider', 'openai')  # 'openai' or 'claude'
        
        print(f"AI Assistant: Received message: {user_message[:50]}...")
        print(f"AI Assistant: Provider: {provider}")
        print(f"AI Assistant: OpenAI client available: {openai_client is not None}")
        print(f"AI Assistant: Claude client available: {anthropic_client is not None}")
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Build system prompt with context
        system_prompt = build_system_prompt(context)
        
        # Get AI response based on provider
        if provider == 'claude' and anthropic_client:
            response_text = get_claude_response(system_prompt, user_message)
        elif openai_client:
            response_text = get_openai_response(system_prompt, user_message)
        else:
            error_msg = 'No AI provider available. '
            if not openai_client:
                error_msg += 'OpenAI client not initialized (check OPENAI_API_KEY). '
            if not anthropic_client:
                error_msg += 'Claude client not initialized (check CLAUDE_API_KEY).'
            return jsonify({'error': error_msg}), 503
        
        return jsonify({
            'response': response_text,
            'provider': provider
        })
        
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"AI Assistant error: {e}")
        print(f"Full traceback: {error_detail}")
        return jsonify({
            'error': f'AI Assistant Error: {str(e)}',
            'detail': 'Check server logs for more information'
        }), 500


def build_system_prompt(context):
    """Build system prompt with application context"""
    base_prompt = """You are an expert AI assistant for the FIX$ GeoEquity Impact Engine. 
    
Your role is to help users understand Economic Justice Value (EJV) calculations and make informed decisions about where to shop.

Key concepts:
- EJV 4.0: Weighted formula (0.25W + 0.15P + 0.30L + 0.15A + 0.15E) measuring 5 components
- EJV 4.1: Equal weight formula measuring 6 components (LC, W, DN, EQ, ENV, PROC) on 0-100 scale
- EJV 4.2: Adds Participation Amplification Factor (PAF) for community engagement
- Local Circulation (LC): How much money stays in the local economy
- Wealth Retention: Percentage of purchase value retained locally
- Wealth Leakage: Percentage that leaves the local economy

You can help with:
1. Explaining EJV scores and components
2. Comparing stores and their economic impact
3. Recommending stores based on economic justice priorities
4. Analyzing local economic patterns
5. Understanding participation and community engagement impact

Be conversational, helpful, and focused on empowering users to make economically just purchasing decisions."""
    
    # Add context if available
    if context:
        context_info = "\n\nCurrent Context:\n"
        
        if 'storeName' in context:
            context_info += f"- Store: {context['storeName']}\n"
        
        if 'ejv40' in context:
            context_info += f"- EJV 4.0 Score: {context['ejv40']}\n"
            
        if 'ejv41' in context:
            context_info += f"- EJV 4.1 Score: {context['ejv41']}\n"
            
        if 'location' in context:
            context_info += f"- Location: {context['location']}\n"
            
        if 'stores' in context and len(context['stores']) > 0:
            context_info += f"- Number of stores in view: {len(context['stores'])}\n"
        
        base_prompt += context_info
    
    return base_prompt


def get_openai_response(system_prompt, user_message):
    """Get response from OpenAI GPT"""
    try:
        print("Calling OpenAI API...")
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",  # Using faster, cheaper model
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=500
        )
        print("OpenAI API call successful")
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API error details: {str(e)}")
        raise Exception(f"OpenAI API error: {str(e)}")


def get_claude_response(system_prompt, user_message):
    """Get response from Claude"""
    try:
        print("Calling Claude API...")
        response = anthropic_client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=500,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        print("Claude API call successful")
        return response.content[0].text
    except Exception as e:
        print(f"Claude API error details: {str(e)}")
        raise Exception(f"Claude API error: {str(e)}")


def get_ai_recommendations(stores_data):
    """Get AI-powered store recommendations based on EJV scores"""
    try:
        if not stores_data or len(stores_data) == 0:
            return {'error': 'No store data provided'}
        
        # Analyze stores
        analysis = analyze_stores(stores_data)
        
        # Build prompt for recommendations
        prompt = f"""Analyze these {len(stores_data)} stores and provide recommendations:

{analysis}

Provide:
1. Best store for economic justice (highest EJV)
2. Store with most local impact
3. A brief explanation of the key differences

Keep response concise (3-4 sentences)."""
        
        system_prompt = build_system_prompt({'stores': stores_data})
        
        if openai_client:
            response = get_openai_response(system_prompt, prompt)
        elif anthropic_client:
            response = get_claude_response(system_prompt, prompt)
        else:
            return {'error': 'No AI provider available'}
        
        return {'recommendations': response}
        
    except Exception as e:
        return {'error': str(e)}


def analyze_stores(stores_data):
    """Create a text summary of stores for AI analysis"""
    summary = ""
    for i, store in enumerate(stores_data, 1):
        summary += f"\nStore {i}: {store.get('name', 'Unknown')}\n"
        summary += f"  - EJV 4.0: {store.get('ejv40', 'N/A')}\n"
        summary += f"  - EJV 4.1: {store.get('ejv41', 'N/A')}\n"
        summary += f"  - Local Circulation: {store.get('localCirculation', 'N/A')}\n"
        summary += f"  - Wealth Retention: {store.get('wealthRetention', 'N/A')}%\n"
    return summary


# Export the endpoint function
def register_ai_routes(app):
    """Register AI assistant routes with Flask app"""
    @app.route('/api/ai/chat', methods=['POST'])
    def chat():
        return ai_assistant()
    
    @app.route('/api/ai/recommendations', methods=['POST'])
    def recommendations():
        data = request.json
        stores = data.get('stores', [])
        return jsonify(get_ai_recommendations(stores))
    
    @app.route('/api/ai/status', methods=['GET'])
    def status():
        """Check AI assistant availability"""
        return jsonify({
            'openai_available': openai_client is not None,
            'claude_available': anthropic_client is not None
        })
