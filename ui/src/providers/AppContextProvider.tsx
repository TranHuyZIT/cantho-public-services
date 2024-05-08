import React, { createContext, ReactNode, useEffect, useState } from "react";
import { getConversation } from "../client";

export interface AppContextType {
  conversationId?: string;
  setConversationId: (conversationId?: string) => void;
  messages: any[];
  setMessages: (messages: any[]) => void;
  conversations: any[];
  setConversations: React.Dispatch<React.SetStateAction<any[]>>;
}

export const AppContext = createContext({} as AppContextType);

export default function AppContextProvider({
  children,
}: {
  children: ReactNode;
}) {
  const [conversationId, setConversationId] = useState<string | undefined>("");
  const [messages, setMessages] = useState<any[]>([]);
  const [conversations, setConversations] = useState<any[]>([]);

  useEffect(() => {
    const fetchConversation = async () => {
      if (!conversationId) {
        setMessages([]);
        return;
      }
      const response = await getConversation(conversationId);
      setMessages(response["messages"]);
    };
    fetchConversation();
  }, [conversationId]);

  useEffect(() => {
    setTimeout(() => {
      // Scroll to the bottom of the chat
      const chatInput = document.getElementById("prompt-input");
      chatInput?.scrollIntoView({ behavior: "smooth" });
    }, 0);
  }, [messages]);

  return (
    <AppContext.Provider
      value={{
        conversationId,
        setConversationId,
        conversations,
        setConversations,
        messages,
        setMessages,
      }}
    >
      {children}
    </AppContext.Provider>
  );
}
