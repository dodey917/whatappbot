# WhatsApp Bot with OpenAI Integration

This bot integrates with WhatsApp and uses OpenAI's ChatGPT 3.5 Turbo, with custom responses from a knowledge base.

## Setup

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set environment variables:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `VERIFY_TOKEN`: Your Meta webhook verify token
   - `WHATSAPP_TOKEN`: Your WhatsApp Business API token (if using)

## Deployment to Render

1. Push your code to a GitHub repository
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Set environment variables in Render dashboard
5. Deploy!

## Meta Webhook Setup

1. Go to Meta Developer Dashboard
2. Configure Webhook URL to point to your Render URL (e.g., `https://your-app.onrender.com/webhook`)
3. Set the Verify Token to match your `VERIFY_TOKEN` environment variable
4. Subscribe to messages events
