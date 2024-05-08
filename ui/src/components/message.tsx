import PromptCards from "./promptCards";
import markdownIt from "markdown-it";

const md = markdownIt();

interface Props {
  role: string;
  message: string;
  documents?: any[];
  questions?: string[];
}

export default function Message({
  role,
  message,
  documents,
  questions,
}: Props) {
  return (
    <div>
      {role === "bot" ? (
        <BotMessage
          message={message}
          documents={documents || []}
          questions={questions || []}
        />
      ) : (
        <UserMessage message={message} />
      )}
    </div>
  );
}

function BotMessage({
  message,
  documents,
  questions,
}: {
  message: string;
  documents: any[];
  questions: string[];
}) {
  return (
    <div className="dark:bg-dark-500 bg-slate-100">
      <div className="flex  px-4 py-8  sm:px-6">
        <img
          className="mr-2 flex h-8 w-8 rounded-full sm:mr-4"
          src="/zit.svg"
        />

        <div className="flex w-full flex-col items-start lg:flex-row lg:justify-between">
          <div
            dangerouslySetInnerHTML={{
              __html: md.render(message),
            }}
          />

          <div className="mt-4 flex flex-row justify-start gap-x-2 text-slate-500 lg:mt-0">
            <button className="hover:text-blue-600">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5"
                viewBox="0 0 24 24"
                strokeWidth="2"
                stroke="currentColor"
                fill="none"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M7 11v8a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1v-7a1 1 0 0 1 1 -1h3a4 4 0 0 0 4 -4v-1a2 2 0 0 1 4 0v5h3a2 2 0 0 1 2 2l-1 5a2 3 0 0 1 -2 2h-7a3 3 0 0 1 -3 -3"></path>
              </svg>
            </button>
            <button className="hover:text-blue-600" type="button">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5"
                viewBox="0 0 24 24"
                strokeWidth="2"
                stroke="currentColor"
                fill="none"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M7 13v-8a1 1 0 0 0 -1 -1h-2a1 1 0 0 0 -1 1v7a1 1 0 0 0 1 1h3a4 4 0 0 1 4 4v1a2 2 0 0 0 4 0v-5h3a2 2 0 0 0 2 -2l-1 -5a2 3 0 0 0 -2 -2h-7a3 3 0 0 0 -3 3"></path>
              </svg>
            </button>
            <button className="hover:text-blue-600" type="button">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5"
                viewBox="0 0 24 24"
                strokeWidth="2"
                stroke="currentColor"
                fill="none"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M8 8m0 2a2 2 0 0 1 2 -2h8a2 2 0 0 1 2 2v8a2 2 0 0 1 -2 2h-8a2 2 0 0 1 -2 -2z"></path>
                <path d="M16 8v-2a2 2 0 0 0 -2 -2h-8a2 2 0 0 0 -2 2v8a2 2 0 0 0 2 2h2"></path>
              </svg>
            </button>
          </div>
        </div>
      </div>
      <div className="mt-4 px-4 sm:px-6 my-5 flex w-full gap-x-2 overflow-x-auto whitespace-nowrap text-xs text-slate-600 dark:text-slate-300 sm:text-sm">
        {questions?.map((question) => (
          <button
            key={question}
            className="rounded-lg bg-slate-200 p-2 hover:bg-blue-600 hover:text-slate-200 dark:bg-slate-800 dark:hover:bg-blue-600 dark:hover:text-slate-50"
          >
            {question}
          </button>
        ))}
      </div>
      <PromptCards documents={documents} />
    </div>
  );
}

function UserMessage({ message }: { message: string }) {
  return (
    <div className="flex flex-row px-4 py-8 sm:px-6">
      <img
        className="mr-2 flex h-8 w-8 rounded-full sm:mr-4"
        src="https://dummyimage.com/256x256/363536/ffffff&text=U"
      />

      <div className="flex max-w-3xl items-center">
        <p>{message}</p>
      </div>
    </div>
  );
}
