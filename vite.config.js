import { defineConfig } from 'vite'

export default defineConfig(({ command }) => ({
  // GitHub Pages serves this project from /JohnsService/ while local Vite
  // development still runs from the site root.
  base: command === 'build' ? '/JohnsService/' : '/',
}))
