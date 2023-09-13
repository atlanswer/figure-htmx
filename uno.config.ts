import type { UserConfig } from "unocss";
import { defineConfig, presetUno } from "unocss";

export default defineConfig({
  presets: [presetUno()],
  theme: {},
  cli: {
    entry: {
      patterns: ["public/**/*.{html,jinja2}"],
      outFile: "public/css/uno.css",
    },
  },
}) as UserConfig;
