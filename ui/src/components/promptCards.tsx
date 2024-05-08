import MarkdownIt from "markdown-it";

interface Props {
  documents: any[];
}
const md = new MarkdownIt();

export default function PromptCards({ documents }: Props) {
  return (
    <ul
      role="list"
      className="grid ms-5 grid-cols-1 gap-6 pb-5 text-slate-900 dark:text-slate-200 sm:grid-cols-2 lg:grid-cols-3"
    >
      {documents.map((doc) => (
        <li
          key={doc.source}
          className="group col-span-1 rounded-lg bg-slate-50 shadow transition-colors duration-300 hover:bg-blue-600 dark:bg-slate-900 dark:hover:bg-blue-600"
        >
          <a
            className="flex cursor-pointer items-center justify-between p-6"
            href=""
          >
            <div className="flex flex-col items-center gap-y-1 rounded-lg text-xs"></div>
            <div className="flex-1">
              <div className="flex items-center space-x-3">
                <h3 className="text-sm font-medium text-slate-900 transition-colors duration-300 group-hover:text-slate-50 dark:text-slate-200">
                  {doc.full_text.split("::")[0]}
                </h3>
              </div>
              <div
                dangerouslySetInnerHTML={{
                  __html: md.render(doc.full_text.split("::")[1]),
                }}
                className="mt-1 text-sm text-slate-500 transition-colors duration-300 group-hover:text-slate-300"
              />
            </div>
          </a>
        </li>
      ))}
    </ul>
  );
}
