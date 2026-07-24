/** @type {import('tailwindcss').Config} */
export default {
  content: ['./templates/**/*.html', './apps/**/templates/**/*.html'],
  theme: {
    extend: {
      colors: {
        cream: { DEFAULT: '#fdf8f0', dark: '#f5ede0', darker: '#ebe3d5' },
        charcoal: { DEFAULT: '#2d2d2d', light: '#4a4a4a', lighter: '#6b6b6b' },
        terracotta: { DEFAULT: '#c4704b', light: '#d4896a', dark: '#a85a3a' },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        display: ['Cormorant Garamond', 'serif'],
      },
      boxShadow: {
        soft: '0 10px 30px rgba(0,0,0,0.08)',
      },
    },
  },
  plugins: [],
}