import { Box, Paper, Typography } from "@mui/material";

const ChatMessage = ({ sender, text }) => {
  const isUser = sender === "user";

  return (
    <Box
      display="flex"
      justifyContent={isUser ? "flex-end" : "flex-start"}
      mb={2}
    >
      <Paper
        sx={{
          p: 2,
          maxWidth: "80%",
          bgcolor: isUser ? "#1976d2" : "#f5f5f5",
          color: isUser ? "#fff" : "#000",
        }}
      >
        <Typography variant="body2">
          {text}
        </Typography>
      </Paper>
    </Box>
  );
};

export default ChatMessage;