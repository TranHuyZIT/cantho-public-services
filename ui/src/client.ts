import axios from "axios";

const client = axios.create({
  baseURL: "http://localhost:8000/",
  headers: {
    "Content-Type": "application/json",
  },
});

export const getConversations = async (name?: string) => {
  const response = await client.get(
    name ? `/conversations?name=${name}` : "/conversations"
  );
  return response.data;
};

export const getConversation = async (id: string) => {
  const response = await client.get(`/conversations/${id}`);
  return response.data;
};

export const chat = async (id?: string, message?: string) => {
  const response = await client.post(`/chat`, {
    conversation_id: id,
    message,
  });
  return response.data;
};
