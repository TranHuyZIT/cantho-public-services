import { createContext, ReactNode, useState } from "react";

export interface AppContextType {
  conversationId?: string;
  setConversationId: (conversationId: string) => void;
  messages: any[];
  setMessages: (messages: any[]) => void;
}

export const AppContext = createContext({} as AppContextType);

export default function AppContextProvider({
  children,
}: {
  children: ReactNode;
}) {
  const [conversationId, setConversationId] = useState<string>("");
  const [messages, setMessages] = useState<any[]>([]);

  return (
    <AppContext.Provider
      value={{ conversationId, setConversationId, messages, setMessages }}
    >
      {children}
    </AppContext.Provider>
  );
}
