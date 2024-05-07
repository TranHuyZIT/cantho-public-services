import Conversation from "./components/conversation";
import PromptInput from "./components/promptInput";
import SidebarProvider from "./layouts/Sidebar";
import AppContextProvider from "./providers/AppContextProvider";

function App() {
  return (
    <AppContextProvider>
      <SidebarProvider>
        <div className="dark:bg-dark-500 w-full bg-slate-100">
          <div className="relative h-full">
            <Conversation />
            <PromptInput />
          </div>
        </div>
      </SidebarProvider>
    </AppContextProvider>
  );
}

export default App;
