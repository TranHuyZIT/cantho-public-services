export default function PromptCards() {
  return (
    <ul
      role="list"
      className="grid ms-5 grid-cols-1 gap-6 text-slate-900 dark:text-slate-200 sm:grid-cols-2 lg:grid-cols-3"
    >
      <li className="group col-span-1 rounded-lg bg-slate-50 shadow transition-colors duration-300 hover:bg-blue-600 dark:bg-slate-900 dark:hover:bg-blue-600">
        <a
          className="flex cursor-pointer items-center justify-between space-x-6 truncate p-6"
          href=""
        >
          <div className="flex flex-col items-center gap-y-1 rounded-lg text-xs">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-6 w-6"
              strokeWidth="2"
              stroke="currentColor"
              fill="none"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <path d="M14 6l7 7l-4 4"></path>
              <path d="M5.828 18.172a2.828 2.828 0 0 0 4 0l10.586 -10.586a2 2 0 0 0 0 -2.829l-1.171 -1.171a2 2 0 0 0 -2.829 0l-10.586 10.586a2.828 2.828 0 0 0 0 4z"></path>
              <path d="M4 20l1.768 -1.768"></path>
            </svg>
          </div>
          <div className="flex-1 truncate">
            <div className="flex items-center space-x-3">
              <h3 className="text-sm font-medium text-slate-900 transition-colors duration-300 group-hover:text-slate-50 dark:text-slate-200">
                Screenwriter
              </h3>
            </div>
            <p className="mt-1 truncate text-sm text-slate-500 transition-colors duration-300 group-hover:text-slate-300">
              I want you to act as a screenwriter. You will develop an engaging
              and creative script for either a feature length film or a Web
              Series that can captivate its viewers.
            </p>
          </div>
        </a>
      </li>

      <li className="group col-span-1 rounded-lg bg-slate-50 shadow transition-colors duration-300 hover:bg-blue-600 dark:bg-slate-900 dark:hover:bg-blue-600">
        <a
          className="flex cursor-pointer items-center justify-between space-x-6 truncate p-6"
          href=""
        >
          <div className="flex flex-col items-center gap-y-1 rounded-lg text-xs">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-6 w-6"
              strokeWidth="2"
              stroke="currentColor"
              fill="none"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <path d="M14 6l7 7l-4 4"></path>
              <path d="M5.828 18.172a2.828 2.828 0 0 0 4 0l10.586 -10.586a2 2 0 0 0 0 -2.829l-1.171 -1.171a2 2 0 0 0 -2.829 0l-10.586 10.586a2.828 2.828 0 0 0 0 4z"></path>
              <path d="M4 20l1.768 -1.768"></path>
            </svg>
          </div>
          <div className="flex-1 truncate">
            <div className="flex items-center space-x-3">
              <h3 className="text-sm font-medium text-slate-900 transition-colors duration-300 group-hover:text-slate-50 dark:text-slate-200">
                Debater
              </h3>
            </div>
            <p className="mt-1 truncate text-sm text-slate-500 transition-colors duration-300 group-hover:text-slate-300">
              I want you to act as a debater. I will provide you with some
              topics related to current events and your task is to research both
              sides of the debates.
            </p>
          </div>
        </a>
      </li>

      <li className="group col-span-1 rounded-lg bg-slate-50 shadow transition-colors duration-300 hover:bg-blue-600 dark:bg-slate-900 dark:hover:bg-blue-600">
        <a
          className="flex cursor-pointer items-center justify-between space-x-6 truncate p-6"
          href=""
        >
          <div className="flex flex-col items-center gap-y-1 rounded-lg text-xs">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-6 w-6"
              strokeWidth="2"
              stroke="currentColor"
              fill="none"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <path d="M14 6l7 7l-4 4"></path>
              <path d="M5.828 18.172a2.828 2.828 0 0 0 4 0l10.586 -10.586a2 2 0 0 0 0 -2.829l-1.171 -1.171a2 2 0 0 0 -2.829 0l-10.586 10.586a2.828 2.828 0 0 0 0 4z"></path>
              <path d="M4 20l1.768 -1.768"></path>
            </svg>
          </div>
          <div className="flex-1 truncate">
            <div className="flex items-center space-x-3">
              <h3 className="text-sm font-medium text-slate-900 transition-colors duration-300 group-hover:text-slate-50 dark:text-slate-200">
                Cyber Security Specialist
              </h3>
            </div>
            <p className="mt-1 truncate text-sm text-slate-500 transition-colors duration-300 group-hover:text-slate-300">
              I want you to act as a cyber security specialist. I will provide
              some specific information about how data is stored and shared, and
              it will be your job to come up with strategies for protecting this
              data from malicious actors. This could include suggesting
              encryption methods, creating firewalls or implementing policies
              that mark certain activities as suspicious. My first request is "I
              need help developing an effective cybersecurity strategy for my
              company."
            </p>
          </div>
        </a>
      </li>
    </ul>
  );
}
