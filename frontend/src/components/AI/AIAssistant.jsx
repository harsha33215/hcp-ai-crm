import { useState } from "react";

import { Box, Typography, CircularProgress } from "@mui/material";

import ChatMessage from "./ChatMessage";
import ChatInput from "./ChatInput";

import { chatWithAI } from "../../services/api";

export default function AIAssistant({ setInteractionData, setRefreshTable }) {
  const [messages, setMessages] = useState([]);

  const [loading, setLoading] = useState(false);

  const sendMessage = async (message) => {
    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text: message,
      },
    ]);

    try {
      setLoading(true);

      const data = await chatWithAI(message);

      if (data.interaction) {
        setInteractionData(data.interaction);

        if (setRefreshTable) {
          setRefreshTable((prev) => !prev);
        }
      }

      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text: data.message || JSON.stringify(data),
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text: "Failed to connect AI",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

return (
  <Box
    sx={{
      display: "flex",
      flexDirection: "column",
      height: "100%",
    }}
  >
    <Typography variant="h5" fontWeight={700} mb={2}>
      AI Assistant
    </Typography>

    {/* Scrollable Messages */}
    <Box
      sx={{
        flex: 1,
        overflowY: "auto",
        border: "1px solid #ddd",
        borderRadius: 2,
        p: 2,
        bgcolor: "#fafafa",
      }}
    >
      {messages.map((msg, index) => (
        <ChatMessage
          key={index}
          sender={msg.sender}
          text={msg.text}
        />
      ))}

      {loading && (
        <Box textAlign="center" mt={2}>
          <CircularProgress size={24} />
        </Box>
      )}
    </Box>

    {/* Input always at bottom */}
    <Box mt={2}>
      <ChatInput
        onSend={sendMessage}
        loading={loading}
      />
    </Box>
  </Box>
);
}
