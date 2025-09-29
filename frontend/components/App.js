"use client";

import { useState, useEffect } from "react";
import Login from "../components/Login";
import Chat from "../components/Chat";

export default function App() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Vérifier si l'utilisateur est déjà connecté
    const token = localStorage.getItem("token");
    const username = localStorage.getItem("username");
    
    if (token && username) {
      // Vérifier si le token est toujours valide
      verifyToken(token, username);
    } else {
      setLoading(false);
    }
  }, []);

  const verifyToken = async (token, username) => {
    try {
      const res = await fetch("http://localhost:8000/auth/me", {
        headers: {
          "Authorization": `Bearer ${token}`
        }
      });
      
      if (res.ok) {
        setUser(username);
      } else {
        // Token invalide, nettoyer le localStorage
        localStorage.removeItem("token");
        localStorage.removeItem("username");
      }
    } catch (error) {
      console.error("Token verification failed:", error);
      localStorage.removeItem("token");
      localStorage.removeItem("username");
    } finally {
      setLoading(false);
    }
  };

  const handleLoginSuccess = (username) => {
    setUser(username);
  };

  const handleLogout = () => {
    setUser(null);
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-gray-600">Loading...</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {user ? (
        <Chat username={user} onLogout={handleLogout} />
      ) : (
        <Login onLoginSuccess={handleLoginSuccess} />
      )}
    </div>
  );
}