/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        vibrant: '#00f2ff',
        darkBg: '#0b0e14',
        cardBg: '#161b22',
      },
    },
  },
  plugins: [],
}