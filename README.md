#  Mistral Secure Chat

This project is a **full-stack AI chatbot** built as part of the application for the **Software Engineer Internship at Mistral AI**.  
It demonstrates secure access to a chat application **powered by Mistral AI's API** for real AI conversations.

## Features
- **Real Mistral AI Integration** - Powered by Mistral's API for intelligent responses
- **JWT Authentication** - Secure login/logout system  
- **Real-time Chat Interface** - Modern React frontend with AI responses
- **Protected API** - FastAPI backend with JWT middleware
- **Docker Ready** - Complete containerization
- **Modern UI** - TailwindCSS styling with AI-focused design
- **Responsive Design** - Works on all devices
- **Smart Error Handling** - Graceful fallbacks and user-friendly messages

## AI Features
- **Mistral AI Integration** - Real responses from Mistral's language models
- **Context Awareness** - AI knows the user's name and conversation context
- **Error Recovery** - Friendly fallback messages when API issues occur
- **Configurable Models** - Easy switch between Mistral Small/Medium/Large



##  Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/laysa66/mistral-secure-chat.git
cd mistral-secure-chat
```

### 2. Configure Mistral AI API (IMPORTANT!)

**Get your Mistral API Key:**
1. Visit [console.mistral.ai](https://console.mistral.ai/)
2. Create an account and get your API key
3. Edit `backend/.env`:
   ```bash
   MISTRAL_API_KEY=your_actual_api_key_here
   ```

**Note:** The app will work without an API key, but you'll get helpful setup messages instead of AI responses.

**Detailed setup guide:** See `MISTRAL_SETUP.md` for complete instructions.

### 3. Start the Application

**Option A: Using Scripts (Easiest)**
```bash
# Terminal 1 - Backend
./start-backend.sh

# Terminal 2 - Frontend  
./start-frontend.sh
```

**Option B: Docker (Recommended for Production)**
```bash
# Development mode with hot-reload
docker-compose -f docker-compose.dev.yml up --build

# Production mode
docker-compose up --build
```

**Access Points:**
- **Frontend**: http://localhost:3000 - AI Chat Interface
- **Backend API**: http://localhost:8000 - FastAPI with Mistral integration
- **API Docs**: http://localhost:8000/docs - Interactive API documentation

### 4. Demo Accounts
Use these accounts to test the AI chat:
this accounts are on the harsh coded in the code for demo purposes only
- **Username**: `admin` | **Password**: `secret`
- **Username**: `testuser` | **Password**: `secret`

**Try asking the AI:**
- "Explain quantum computing in simple terms"
- "Write a Python function to sort a list"
- "What's the weather like in Paris?" (it will explain it can't access real-time data)
- "Tell me a joke about programming"

##  Mistral AI Configuration

### API Key Setup
1. **Get API Key**: Visit [console.mistral.ai](https://console.mistral.ai/)
2. **Configure**: Edit `backend/.env`:
   ```bash
   MISTRAL_API_KEY=mr-your-actual-key-here
   JWT_SECRET_KEY=your-secret-jwt-key
   DEBUG=True
   ```
3. **Restart**: Restart the backend to apply changes

### Model Options
The app uses `mistral-small-latest` by default. You can change it in `backend/app/services/mistral_service.py`:

- **mistral-small-latest**: Fast and cost-effective (~$0.2/1M tokens)
- **mistral-medium-latest**: More powerful (~$2.7/1M tokens)  
- **mistral-large-latest**: Most capable (~$8/1M tokens)

### Without API Key
The app gracefully handles missing API keys:
- Shows helpful setup instructions
- Provides fallback responses
- Maintains full functionality for testing authentication

##  Manual Setup (without Docker)

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## Docker Configuration

### Docker Commands

#### Production Mode
```bash
# Quick start (recommended)
./start.sh

# Manual commands
docker compose up --build -d      # Build and start in background
docker compose down               # Stop all services
docker compose logs -f            # View logs
```

####  Development Mode (with hot-reload)
```bash
# Quick start development
./dev.sh

# Manual commands  
docker compose -f docker-compose.dev.yml up --build
docker compose -f docker-compose.dev.yml down
```

####  Other Useful Commands
```bash
# Rebuild specific service
docker compose build backend
docker compose build frontend

# Clean rebuild (if issues)
docker compose build --no-cache

# View service logs separately
docker compose logs -f backend
docker compose logs -f frontend
```


##  API Endpoints

### Authentication
- `POST /auth/login` - Login with username/password  
- `POST /auth/register` - Create new account
- `GET /auth/me` - Get current user info (requires token)

### AI Chat
- `POST /chat/` - **Send message to Mistral AI** (requires JWT token)
  - Receives user message
  - Calls Mistral API with context
  - Returns AI-generated response
  - Handles errors gracefully

### Health Checks
- `GET /` - API health check
- `GET /auth/status` - Auth service status
- `GET /chat/status` - Chat service status

## Deployment

### Docker Compose (Recommended)

```bash
docker-compose up -d --build
```

### Individual Containers
```bash
# Build images
docker build -t mistral-backend ./backend
docker build -t mistral-frontend ./frontend

# Run containers
docker run -d -p 8000:8000 --name backend mistral-backend
docker run -d -p 3000:3000 --name frontend mistral-frontend
```



### Project Structure
```
├── backend/           # FastAPI Python backend
│   ├── app/
│   │   ├── main.py           # FastAPI app
│   │   ├── auth.py           # JWT authentication
│   │   ├── models/
│   │   │   └── schemas.py    # Pydantic models
│   │   └── routers/
│   │       ├── auth.py       # Auth endpoints
│   │       └── chat.py       # Chat endpoints
│   ├── requirements.txt      # Python dependencies
│   └── Dockerfile           # Backend container
├── frontend/          # Next.js React frontend
│   ├── src/app/             # App Router
│   │   └── page.tsx         # Main page
│   ├── components/          # React components
│   │   ├── App.js           # Main app component
│   │   ├── Login.js         # Login form
│   │   └── Chat.js          # Chat interface
│   ├── package.json         # Node dependencies
│   └── Dockerfile          # Frontend container
└── docker-compose.yml       # Container orchestration
```

## Author
Laysa66


