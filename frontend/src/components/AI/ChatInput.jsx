import { useState } from "react";
import { Box, Button, TextField } from "@mui/material";

const ChatInput = ({ onSend, loading }) => {
  const [message, setMessage] = useState("");

  const send = () => {
    if (!message.trim()) return;

    onSend(message);
    setMessage("");
  };

  return (
    <Box
      display="flex"
      gap={1}
      mt={2}
    >
      <TextField
        fullWidth
        size="small"
        label="Type your message..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") send();
        }}
      />

      <Button
        variant="contained"
        onClick={send}
        disabled={loading}
      >
        Send
      </Button>
    </Box>
  );
};

export default ChatInput;