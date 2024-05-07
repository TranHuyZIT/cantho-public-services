import defaultTheme from "tailwindcss/defaultTheme";

/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        dark: {
          500: "#020617",
        },
        slate: {
          50: "#f8fafc",
          100: "#f1f5f9",
          200: "#e2e8f0",
          300: "#cbd5e1",
          400: "#94a3b8",
          500: "#64748b",
          600: "#475569",
          700: "#334155",
          800: "#1e293b",
          900: "#0f172a",
        },
        blue: {
          50: "#eff6ff",
          100: "#dbeafe",
          200: "#bfdbfe",
          300: "#93c5fd",
          400: "#60a5fa",
          500: "#3b82f6",
          600: "#2563eb",
          700: "#1d4ed8",
          800: "#1e40af",
          900: "#1e3a8a",
        },
      },
    },
    screens: {
      ...defaultTheme.screens,
      xs: "375px",
    },
    colors: {
      primary: {
        500: "#2463eb",
      },
    },
    fontSize: {
      ...defaultTheme.fontSize,
      h1: ["128px", "0.86em"],
      "h1-mobile": ["86px", "0.86em"],
      "h1-small": ["96px", "1em"],
      h2: ["40px", "1em"],
      "h2-mobile": ["32px", "1em"],
      h3: ["32px", "1em"],
      "h3-mobile": ["26px", "1em"],
      h4: ["24px", "1em"],
      h5: ["18px", "1em"],
      body: ["16px", "1.5em"],
      "body-l-mobile": ["18px", "1.5em"],
      "body-l": ["24px", "1.5em"],
      "body-xl": ["36px", "1.5em"],
      "body-xl-mobile": ["22px", "1.5em"],
      link: ["16px", "1.5em"],
    },
    fontFamily: {
      default: ["var"],
    },
  },
  plugins: [],
};
