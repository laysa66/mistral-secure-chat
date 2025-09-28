"use client";
import { useState, useRef } from "react";

export default function Chat() {
  const [messages, setMessages] = useState([{ sender: "ai", text: "Hello! Ask me anything." }]); // we start with a greeting
  const [input, setInput] = useState(""); // current input value
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
      // 2) call backend API to get AI response ( here we assume it's running on localhost:8000 )
      const res = await fetch("http://localhost:8000/chat/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text }),
      });

      if (!res.ok) {
        throw new Error(`Server error: ${res.status}`);
      }

      const data = await res.json();

      // 3) add AI response to chat
      setMessages((m) => [...m, { sender: "ai", text: data.ai_response || "No response" }]);
      inputRef.current?.focus();
    } catch (err) {
      // 4) handle errors
      setMessages((m) => [...m, { sender: "ai", text: `Error: ${err.message}` }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-6">
      <h1 className="text-2xl font-semibold mb-4">Secure AI Chat (Demo)</h1>

      <div className="border rounded p-4 min-h-[200px] mb-4 bg-white">
        {messages.map((m, i) => (
          <div key={i} className={`mb-3 flex ${m.sender === "user" ? "justify-end" : "justify-start"}`}>
            <div className={`px-4 py-2 rounded-lg ${m.sender === "user" ? "bg-blue-500 text-white" : "bg-gray-100 text-gray-800"}`}>
              {m.text}
            </div>
          </div>
        ))}
      </div>

      <form onSubmit={sendMessage} className="flex gap-2">
        <input
          ref={inputRef}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Write a message..."
          className="flex-1 border rounded px-3 py-2"
        />
        <button type="submit" disabled={loading} className="px-4 py-2 bg-green-500 text-white rounded">
          {loading ? "..." : "Send"}
        </button>
      </form>
    </div>
  );
}
