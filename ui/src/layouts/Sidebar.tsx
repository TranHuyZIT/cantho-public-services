import clsx from "clsx";
import { useState } from "react";

export default function SidebarProvider({
  children,
}: {
  children: React.ReactNode;
}) {
  const [themeMode, setThemeMode] = useState<"light" | "dark">("dark");

  const toggleTheme = () => {
    const newTheme = themeMode === "light" ? "dark" : "light";
    setThemeMode(newTheme);
    document.querySelector("html")?.classList.toggle("dark");
  };

  return (
    <aside className="flex">
      {/* First Column */}
      <div className="flex h-screen w-12 flex-col items-center space-y-8 border-r border-slate-300 bg-slate-50 py-8 dark:border-slate-700 dark:bg-slate-900 sm:w-16">
        {/* Logo */}
        <a href="#" className="mb-1 p-2 ">
          <img src="/zit.svg" alt="logo" />
        </a>
        {/* Conversations */}
        <a
          href="#"
          className="rounded-lg bg-blue-100 p-1.5 text-blue-600 transition-colors duration-200 dark:bg-slate-800 dark:text-blue-600"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-6 w-6"
            viewBox="0 0 24 24"
            strokeWidth="2"
            stroke="currentColor"
            fill="none"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
            <path d="M21 14l-3 -3h-7a1 1 0 0 1 -1 -1v-6a1 1 0 0 1 1 -1h9a1 1 0 0 1 1 1v10"></path>
            <path d="M14 15v2a1 1 0 0 1 -1 1h-7l-3 3v-10a1 1 0 0 1 1 -1h2"></path>
          </svg>
        </a>
        {/* Discover */}
        <a
          href="#"
          className="rounded-lg p-1.5 text-slate-500 transition-colors duration-200 hover:bg-slate-200 focus:outline-none dark:text-slate-400 dark:hover:bg-slate-800"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-6 w-6"
            viewBox="0 0 24 24"
            strokeWidth="2"
            stroke="currentColor"
            fill="none"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
            <path d="M10 10m-7 0a7 7 0 1 0 14 0a7 7 0 1 0 -14 0"></path>
            <path d="M21 21l-6 -6"></path>
          </svg>
        </a>
      </div>
      {/* Second Column */}
      <div className="h-screen w-52 overflow-y-auto bg-slate-50 py-8 dark:bg-slate-900 sm:w-60 relative">
        <div className="flex items-start">
          <h2 className="inline px-5 text-lg font-medium text-slate-800 dark:text-slate-200">
            Chats
          </h2>
          <span className="rounded-full bg-blue-600 px-2 py-1 text-xs text-slate-200">
            24
          </span>
        </div>

        <div className="mx-2 mt-8 space-y-4">
          <form>
            <label htmlFor="chat-input" className="sr-only">
              Search chats
            </label>
            <div className="relative">
              <input
                id="search-chats"
                type="text"
                className="w-full rounded-lg border border-slate-300 bg-slate-50 p-3 pr-10 text-sm text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-200"
                placeholder="Search chats"
                required
              />
              <button
                type="submit"
                className="absolute bottom-2 right-2.5 rounded-lg p-2 text-sm text-slate-500 hover:text-blue-700 focus:outline-none sm:text-base"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-5 w-5"
                  aria-hidden="true"
                  viewBox="0 0 24 24"
                  strokeWidth="2"
                  stroke="currentColor"
                  fill="none"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                  <path d="M8 9h8"></path>
                  <path d="M8 13h5"></path>
                  <path d="M11.008 19.195l-3.008 1.805v-3h-2a3 3 0 0 1 -3 -3v-8a3 3 0 0 1 3 -3h12a3 3 0 0 1 3 3v4.5"></path>
                  <path d="M18 18m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0"></path>
                  <path d="M20.2 20.2l1.8 1.8"></path>
                </svg>
                <span className="sr-only">Search chats</span>
              </button>
            </div>
          </form>

          <button className="flex w-full flex-col gap-y-2 rounded-lg px-3 py-2 text-left transition-colors duration-200 hover:bg-slate-200 focus:outline-none dark:hover:bg-slate-800">
            <h1 className="text-sm font-medium capitalize text-slate-700 dark:text-slate-200">
              Tailwind Classes
            </h1>
            <p className="text-xs text-slate-500 dark:text-slate-400">12 Mar</p>
          </button>

          <button className="flex w-full flex-col gap-y-2 rounded-lg bg-slate-200 px-3 py-2 text-left transition-colors duration-200 focus:outline-none dark:bg-slate-800">
            <h1 className="text-sm font-medium capitalize text-slate-700 dark:text-slate-200">
              explain quantum computing
            </h1>
            <p className="text-xs text-slate-500 dark:text-slate-400">10 Feb</p>
          </button>
          <button className="flex w-full flex-col gap-y-2 rounded-lg px-3 py-2 text-left transition-colors duration-200 hover:bg-slate-200 focus:outline-none dark:hover:bg-slate-800">
            <h1 className="text-sm font-medium capitalize text-slate-700 dark:text-slate-200">
              How to create ERP Diagram
            </h1>
            <p className="text-xs text-slate-500 dark:text-slate-400">22 Jan</p>
          </button>
          <button className="flex w-full flex-col gap-y-2 rounded-lg px-3 py-2 text-left transition-colors duration-200 hover:bg-slate-200 focus:outline-none dark:hover:bg-slate-800">
            <h1 className="text-sm font-medium capitalize text-slate-700 dark:text-slate-200">
              API Scaling Strategies
            </h1>
            <p className="text-xs text-slate-500 dark:text-slate-400">1 Jan</p>
          </button>
        </div>
        <div className="flex flex-col absolute bottom-5 left-1/4">
          <div className="flex justify-center">
            <div className="rounded-lg border border-slate-200/20">
              <div className="flex text-xs font-semibold leading-5">
                <button
                  className={clsx(
                    "flex w-auto gap-2 rounded-lg px-4 py-2 focus:outline-non",
                    themeMode === "dark"
                      ? "bg-blue-600 text-slate-300"
                      : "text-black"
                  )}
                  onClick={toggleTheme}
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    className="inline-flex h-4 w-4"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
                    ></path>
                  </svg>
                </button>
                <button
                  className={clsx(
                    "flex gap-2 rounded-lg px-4 py-2.5 focus:outline-none text-slate-300",
                    themeMode === "light"
                      ? "bg-blue-600 text-slate-300"
                      : "text-black"
                  )}
                  onClick={toggleTheme}
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    className="inline-flex h-4 w-4"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"
                    ></path>
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      {children}
    </aside>
  );
}
