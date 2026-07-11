import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

/* -----------------------------
   CRUD APIs
------------------------------ */

export const getInteractions = async () => {
  const response = await api.get("/interactions/");
  return response.data;
};

export const getInteraction = async (id) => {
  const response = await api.get(`/interactions/${id}`);
  return response.data;
};

export const createInteraction = async (data) => {
  const response = await api.post("/interactions/", data);
  return response.data;
};

export const updateInteraction = async (id, data) => {
  const response = await api.put(`/interactions/${id}`, data);
  return response.data;
};

export const deleteInteraction = async (id) => {
  const response = await api.delete(`/interactions/${id}`);
  return response.data;
};

/* -----------------------------
   AI
------------------------------ */

export const chatWithAI = async (message) => {
  const response = await api.post("/ai/chat", {
    message,
  });

  return response.data;
};
export default api;