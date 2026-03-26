# Real-Time Chat Application

This is a **real-time chat application** built using **Django** and **WebSockets** with **Channels** and **Daphne**. It allows multiple users to chat independently using unique URLs, and it gives a friendly, human-like AI chatbot response powered by **Ollama (LLaMA3)**.

---

## 🔹 Features

- Real-time chat with **instant messages** using WebSockets  
- Friendly AI chatbot responds naturally  
- Multiple users can chat simultaneously using **unique URLs**  
- Maintains **chat history** for each user separately  
- Automatic reconnection if WebSocket disconnects  

---

## 🔹 Requirements

- Python 3.10+  
- Django 4.x  
- Django Channels  
- Daphne (ASGI server)  
- Ollama Python SDK (for AI responses)  

#### Install dependencies using:

```bash
pip install -r requirements.txt
```

## 🔹 How to Run

### Clone the project:
```
git clone <your-repo-url>
cd <project-folder>
```
#### Make migrations and migrate the database:
```
python manage.py makemigrations
python manage.py migrate
```
#### Run the server using Daphne (WebSocket support):
```
daphne chatproject.asgi:application
```

⚠️ Do NOT use python manage.py runserver because WebSockets require an ASGI server like Daphne.

#### Open your browser and visit a URL with your username:
```
http://127.0.0.1:8000/<your-username>/
```

### Example:
```
http://127.0.0.1:8000/manoj/
http://127.0.0.1:8000/alice/
```
Each URL gives a unique chat session.

Start chatting! Type your message and the AI bot will reply naturally.

## 🔹 How it Works
### Each user URL is treated as a room.
#### WebSocket connects to:
```
ws://127.0.0.1:8000/ws/chat/<username>/
```
Chat messages are sent and received in real-time
AI uses chat history to reply naturally to your messages

## 🔹 Notes
Make sure your username in the URL contains only letters, numbers, or underscores (a-z, A-Z, 0-9, _)
Chat history is limited to the last 10 messages for efficiency
If WebSocket disconnects, the app will automatically try to reconnect

## 🔹 Example
Open http://127.0.0.1:8000/manoj/ → start chatting as “Manoj”
Open http://127.0.0.1:8000/alice/ → another independent session as “Alice”

The AI chatbot will respond friendly and naturally in each session.

## 🔹 Credits
Built with Django, Channels, Daphne, and Ollama AI
Frontend is plain HTML + JavaScript for WebSocket connection
