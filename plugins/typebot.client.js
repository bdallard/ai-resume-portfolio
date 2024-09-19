// plugins/typebot.client.js
export default defineNuxtPlugin(() => {
  if (process.client) {
    const typebotInitScript = document.createElement("script");
    typebotInitScript.type = "module";
    typebotInitScript.innerHTML = `import Typebot from 'https://cdn.jsdelivr.net/npm/@typebot.io/js@0.3.12/dist/web.js'
        
        Typebot.initBubble({
          typebot: "your-bot-id-here",
          apiHost: "your-bot-server-here",
          theme: { button: { backgroundColor: "#FFFFFF" } },
        });
        `;
    document.body.append(typebotInitScript);
  }
});

