import { useEffect, useState } from "react";

export default function useDebounce(defaultValue: any, delay: number) {
  const [value, setValue] = useState<any>(defaultValue);

  useEffect(() => {
    const timeout = setTimeout(() => {
      setValue(defaultValue);
    }, delay);

    return () => {
      clearTimeout(timeout);
    };
  });

  return value;
}
