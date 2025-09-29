"use client";
import { useState, useRef } from "react";

export default function Chat({ username, onLogout }) {
  const [messages, setMessages] = useState([{ 
    sender: "ai", 
    text: ` Hello ${username} ! comment pui-je t'aider aujourd'hui ?  ` 
  }]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false); 
  const inputRef = useRef(null);

  const sendMessage = async (e) => {
    e?.preventDefault();
    const text = input.trim();
    if (!text) return;

    // 1) show user message immediately
    setMessages((m) => [...m, { sender: "user", text }]);
    setInput("");
    setLoading(true);

    try {
      const token = localStorage.getItem("token");
      
      if (!token) {
        throw new Error("No authentication token found. Please login again.");
      }

      const res = await fetch("http://localhost:8000/chat/", {
        method: "POST",
        headers: { 
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({ message: text }),
      });

      if (res.status === 401) {
        // Token expired ou invalide
        localStorage.removeItem("token");
        localStorage.removeItem("username");
        throw new Error("Session expired. Please login again.");
      }

      if (!res.ok) {
        throw new Error(`Server error: ${res.status}`);
      }

      const data = await res.json();

      // 3) add AI response to chat
      setMessages((m) => [...m, { 
        sender: "ai", 
        text: data.ai_response || "No response" 
      }]);
      inputRef.current?.focus();
    } catch (err) {
      // 4) handle errors
      setMessages((m) => [...m, { 
        sender: "ai", 
        text: `Error: ${err.message}` 
      }]);
      
      // Si c'est une erreur d'auth, déconnecter
      if (err.message.includes("login again")) {
        setTimeout(() => onLogout(), 2000);
      }
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("username");
    onLogout();
  };

  return (
    <div className="max-w-2xl mx-auto p-6">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-semibold"> Mistral AI Chat</h1>
        <div className="flex items-center gap-4">
          <span className="text-sm text-gray-600">Welcome, {username}</span>
          <button 
            onClick={handleLogout}
            className="px-3 py-1 text-sm bg-red-500 text-white rounded hover:bg-red-600"
          >
            Logout
          </button>
        </div>
      </div>

      <div className="border rounded p-4 min-h-[200px] mb-4 bg-white">
        {messages.map((m, i) => (
          <div key={i} className={`mb-3 flex ${m.sender === "user" ? "justify-end" : "justify-start"}`}>
            <div className={`px-4 py-2 rounded-lg max-w-[80%] ${
              m.sender === "user" 
                ? "bg-blue-500 text-white" 
                : m.text.startsWith("Error:") 
                  ? "bg-red-100 text-red-800 border border-red-200"
                  : "bg-gray-100 text-gray-800"
            }`}>
              {m.text}
            </div>
          </div>
        ))}
        {loading && (
          <div className="flex justify-start mb-3">
            <div className="bg-gray-100 text-gray-800 px-4 py-2 rounded-lg animate-pulse">
               Mistral IA is thinking...
            </div>
          </div>
        )}
      </div>

      <form onSubmit={sendMessage} className="flex gap-2">
        <input
          ref={inputRef}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Écrivez votre message à l'IA..."
          className="flex-1 border rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
          disabled={loading}
        />
        <button 
          type="submit" 
          disabled={loading || !input.trim()} 
          className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
        >
          {loading ? "⏳" : "🚀 Envoyer"}
        </button>
      </form>
    </div>
  );
}
