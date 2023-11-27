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
          "primary-focus": "#008170", /* Primary color - focused */
          "primary-content": "#ffffff", /* Content color to use on primary color */

          "secondary": "#232d3f",   /* Secondary color */
          "secondary-focus": "#0F0F0F", /* Secondary color - focused */
          "secondary-content": "#ffffff", /* Content color to use on secondary color */

          "accent": "#008170", /* Accent color */
          "accent-focus": "#005B41",  /* Accent color - focused */
          "accent-content": "#ffffff", /* Content color to use on accent color */

          "neutral": "#0F0F0F", /* Neutral color */
          "neutral-focus": "#232d3f", /* Neutral color - focused */
          "neutral-content": "#ffffff", /* Content color to use on neutral color */

          "base-100": "#0F0F0F", /* Base color of page, used for blank backgrounds */
          "base-200": "#232d3f", /* Base color, a little lighter */
          "base-300": "#005B41", /* Base color, even lighter */
          "base-content": "#ffffff", /* Foreground content color to use on base color */

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

