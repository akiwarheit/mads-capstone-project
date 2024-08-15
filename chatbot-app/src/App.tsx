import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import "./App.css";

interface Message {
  sender: "user" | "bot";
  text: string;
}

interface ApiResponse {
  response: string;
}

const initialQuestions = [
  "What type of terrain do you prefer to live in (e.g., forests, open water, developed areas)?",
  "Are you looking for a county with a higher or lower population density (e.g., densely populated urban areas or more sparsely populated rural areas)?",
  "What is your preferred quality of public schools (e.g., high-ranking elementary schools, average middle schools, lower-ranking high schools)?",
  "What is your budget range for housing, specifically in terms of fair market rent for different bedroom sizes (e.g., $700 for one bedroom, $830 for two bedrooms, $1047 for three bedrooms, $1425 for four bedrooms)?",
];

const App: React.FC = () => {
  const [input, setInput] = useState<string>("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [questionIndex, setQuestionIndex] = useState<number>(0);
  const [userResponses, setUserResponses] = useState<string[]>([]);

  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  useEffect(() => {
    const welcomeMessage: Message = {
      sender: "bot",
      text: "Welcome! I'm here to help you find the best place to live.",
    };
    const firstQuestion: Message = {
      sender: "bot",
      text: initialQuestions[0],
    };
    setMessages([welcomeMessage, firstQuestion]);
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (input.trim() === "") return;

    const userMessage: Message = { sender: "user", text: input };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setUserResponses((prevResponses) => [...prevResponses, input]);
    setLoading(true);
    setInput("");

    try {
      if (questionIndex < initialQuestions.length - 1) {
        setQuestionIndex((prevIndex) => prevIndex + 1);
        const nextQuestion: Message = {
          sender: "bot",
          text: initialQuestions[questionIndex + 1],
        };
        setMessages((prevMessages) => [...prevMessages, nextQuestion]);
      } else {
        console.log();
        const payload = {
          question: `[INST] I am looking for a county that matches the description: ${userResponses.join(
            ","
          )}. What county matches this? Provide the terrain characteristics for each county. [/INST]`,
        };

        const response = await axios.post<ApiResponse>(
          "http://localhost:8080/ask",
          payload
        );

        const botMessage: Message = {
          sender: "bot",
          text: response.data.response.replace("[/] ", ""),
        };
        setMessages((prevMessages) => [...prevMessages, botMessage]);
      }
    } catch (error) {
      console.error("Error sending message:", error);
      const errorMessage: Message = {
        sender: "bot",
        text: "Sorry, something went wrong. Please try again.",
      };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    } finally {
      setLoading(false);
    }
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
          <div ref={messagesEndRef} />
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
