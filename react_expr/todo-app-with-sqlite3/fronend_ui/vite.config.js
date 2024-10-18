import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
		host: '0.0.0.0', // Bind to all IP addresses
    port: 8000,  // Specify the port you want to use
  },
})
