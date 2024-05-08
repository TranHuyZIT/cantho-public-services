import { useContext, useState } from "react";
import { AppContext } from "../providers/AppContextProvider";
import { chat, getConversation } from "../client";

export default function PromptInput() {
  const { conversationId, setMessages, messages, setConversationId } =
    useContext(AppContext);
  const [loading, setLoading] = useState<boolean>(false);
  const [text, setText] = useState<string>("");

  const onSubmit = async () => {
    setMessages([...messages, { role: "user", message: text }]);
    setLoading(true);
    setText("");
    const response = await chat(conversationId, text);
    setConversationId(response["conversation_id"]);
    setLoading(false);
    const newMessages = await getConversation(response["conversation_id"]);
    setMessages([...newMessages["messages"]]);
  };

  const handleChange = (input: string) => {
    setText(input);
  };

  return (
    <div className="flex w-full absolute bottom-0 left-0 right-0 items-center rounded-b-md border-t border-slate-300 bg-slate-100 mb-2 p-2 dark:border-slate-700 dark:bg-dark-500">
      <label htmlFor="chat" className="sr-only">
        Enter your prompt
      </label>
      <input
        value={text}
        onKeyUp={(e) => {
          if (e.key === "Enter") {
            onSubmit();
          }
        }}
        onChange={(e) => handleChange(e.target.value)}
        id="chat-input"
        className="mx-2 flex min-h-full w-full rounded-md border border-slate-300 bg-slate-50 p-2 text-base text-slate-900 placeholder-slate-400 focus:border-blue-600 focus:outline-none focus:ring-1 focus:ring-blue-600 dark:border-slate-700 dark:bg-slate-800 dark:text-slate-50 dark:placeholder-slate-400 dark:focus:border-blue-600 dark:focus:ring-blue-600"
        placeholder="Enter your prompt"
      />
      <div>
        <button
          onClick={onSubmit}
          className="inline-flex hover:text-blue-600 dark:text-slate-200 dark:hover:text-blue-600 sm:p-2"
          type="submit"
        >
          {loading ? (
            <img src="/loading.svg" alt="loading" className="h-10  w-20" />
          ) : (
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-10 w-20"
              aria-hidden="true"
              viewBox="0 0 24 24"
              strokeWidth="2"
              stroke="currentColor"
              fill="none"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <path d="M10 14l11 -11"></path>
              <path d="M21 3l-6.5 18a.55 .55 0 0 1 -1 0l-3.5 -7l-7 -3.5a.55 .55 0 0 1 0 -1l18 -6.5"></path>
            </svg>
          )}
        </button>
      </div>
    </div>
  );
}
