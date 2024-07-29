import React, { useState } from "react";
import axios from "axios";
import "./App.css";

interface Message {
  sender: "user" | "bot";
  text: string;
}

const App: React.FC = () => {
  const [input, setInput] = useState<string>("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState<boolean>(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (input.trim() === "") return;

    const userMessage: Message = { sender: "user", text: input };
    setMessages([...messages, userMessage]);
    setLoading(true);

    try {
      const response = await axios.post("http://localhost:5000/ask", {
        question: input,
      });
      const botMessage: Message = {
        sender: "bot",
        text: (response as any).data.response,
      };
      setMessages([...messages, userMessage, botMessage]);
    } catch (error) {
      console.error("Error sending message:", error);
    } finally {
      setLoading(false);
    }

    setInput("");
  };

  return (
    <div className="h-screen flex flex-col items-center justify-center bg-gray-100">
      <div className="w-full h-full bg-white shadow-md rounded-lg p-6 flex flex-col xl:px-96 md:px-20">
        <div className="flex flex-col space-y-4 mb-4 overflow-y-auto flex-grow">
          {messages.map((message, index) => (
            <div
              key={index}
              className={`p-2 rounded-lg ${
                message.sender === "user"
                  ? "bg-blue-500 text-white self-end"
                  : "bg-gray-200 self-start"
              }`}
            >
              {message.text}
            </div>
          ))}
          {loading && (
            <div className="self-center p-2 text-gray-500">Loading...</div>
          )}
        </div>
        <form onSubmit={handleSubmit} className="flex space-x-4">
          <input
            type="text"
            className="flex-grow p-2 border border-gray-300 rounded-lg"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your message..."
            disabled={loading}
          />
          <button
            type="submit"
            className="px-4 py-2 bg-blue-500 text-white rounded-lg"
            disabled={loading}
          >
            Send
          </button>
        </form>
      </div>
    </div>
  );
};

export default App;
