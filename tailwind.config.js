/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*"],
  theme: {
    
    extend: {},
  },
  daisyui: {
    themes: [
      {
        mainTheme: { /* your theme's name */
          "primary": "#005B41",     /* Primary color */
          "secondary": "#232d3f",   /* Secondary color */
          "accent": "#008170", /* Accent color */
          "neutral": "#0F0F0F", /* Neutral color */
          "base-100": "#0F0F0F", /* Base color of page, used for blank backgrounds */
          "info": "#2094f3", /* Info */
          "success": "#009485", /* Success */
          "warning": "#ff9900", /* Warning */
          "error": "#ff5724", /* Error */
        },
      },
      "light",
      "dark",
    ],
  },
  plugins: [require("daisyui")],
}

