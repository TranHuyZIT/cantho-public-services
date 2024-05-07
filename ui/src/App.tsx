import Conversation from "./components/conversation";
import PromptInput from "./components/promptInput";
import SidebarProvider from "./layouts/Sidebar";

function App() {
  return (
    <SidebarProvider>
      <div className="dark:bg-dark-500 w-full">
        <div className="relative h-full">
          <Conversation />
          <PromptInput />
        </div>
      </div>
    </SidebarProvider>
  );
}

export default App;
