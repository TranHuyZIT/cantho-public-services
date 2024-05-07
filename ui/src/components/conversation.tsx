import Message from "./message";

export default function Conversation() {
  return (
    <div className="flex max-h-[97vh] w-full flex-col">
      {/* Prompt Messages */}
      <div className="flex-1 overflow-y-auto bg-slate-300 text-sm leading-6 text-slate-900 shadow-md dark:bg-slate-800 dark:text-slate-300 sm:text-base sm:leading-7">
        <Message role="user" message="What is quantum computing?" />

        <Message
          role="bot"
          message="Certainly! Quantum computing is a new type of computing that
          relies on the principles of quantum physics. Traditional
          computers, like the one you might be using right now, use bits to
          store and process information. These bits can represent either a 0
          or a 1. In contrast, quantum computers use quantum bits, or
          qubits.

          Unlike bits, qubits can represent not only a 0 or a 1 but also a
          superposition of both states simultaneously. This means that a
          qubit can be in multiple states at once, which allows quantum
          computers to perform certain calculations much faster and more
          efficiently."
        />
      </div>
    </div>
  );
}
