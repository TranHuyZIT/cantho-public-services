import { useContext } from "react";
import Message from "./message";
import { AppContext } from "../providers/AppContextProvider";
import { useAutoAnimate } from "@formkit/auto-animate/react";

export default function Conversation() {
  const { messages } = useContext(AppContext);
  const [animationParent] = useAutoAnimate();

  return (
    <div className="flex max-h-[97vh] w-full flex-col">
      {/* Prompt Messages */}
      <div
        ref={animationParent}
        className="flex-1 overflow-y-auto bg-slate-300 text-sm leading-6 text-slate-900 shadow-md dark:bg-slate-800 dark:text-slate-300 sm:text-base sm:leading-7"
      >
        {messages?.map((message) => (
          <Message
            key={message._id?.["$oid"] || "new-user-chat"}
            role={message.role}
            message={message.message}
            documents={message.documents}
            questions={message.metadata?.questions}
          />
        ))}
        <div id="prompt-input" className="h-10 w-full"></div>
      </div>
    </div>
  );
}
