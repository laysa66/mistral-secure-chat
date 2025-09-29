# 🤖 Mistral API Configuration

## How to get your Mistral API key

1. **Visit the site of Mistral AI**
   - Go to [console.mistral.ai](https://console.mistral.ai/)
   
2. **Create an account**
   - Sign up with your email
   - Confirm your account

3. **Get your API key**
   - Log in to your Mistral account
   - Go to the "API Keys" section
   - Create a new API key
   - Copy your key (it usually starts with `mr-...>)

4. **Configure your application**
   - Open the `backend/. env`file
   - Replace `your_mistral_api_key_here` with your real API key
   - Example: `MISTRAL_API_KEY=mr-123456789abcdef...`

5. **Restart your application**
   - Stop and restart your backend to take into account the changes

## Available models

- `mistral-small-latest` : Fast and economical (recommended for beginners)
- `mistral-medium-latest` : More powerful but more expensive
- `mistral-large-latest` : The most performant

## Approximate prices (check on the official website)

- Mistral Small : ~$0.2 / 1M tokens
- Mistral Medium: ~$2.7 / 1M tokens  
- Mistral Large : ~$8 / 1M tokens

## Test without API key

If you do not have an API key yet, the application will still work and display an explanatory message instead of AI responses.

## Security

 **IMPORTANT**: 
- Never share your API key
- Never commit it in Git
- The `.env` file is in `.gitignore` for this reason