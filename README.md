# AI Resume Portfolio

This template portfolio is designed to showcase your skills and experience in a modern, visually appealing format. It comes with a Large Language Model (LLM) web application that generates personalized cover letters tailored to your job applications 😎

The template leverages Groq LLM, Minio for static asset management, Typebot for interactive chatbots, and Lottiefiles for animations.

[Live demo here](https://dallard.tech/)

## Features

- **LLM Integration:** Generate cover letters with ease using Groq LLM.
- **Image Management:** Easily manage and display your tech logos and other images with Minio.
- **Interactive Chatbot:** Enhance user experience with a customizable chatbot.
- **Animations:** Bring your portfolio to life with animations from Lottiefiles.

---

## Set Up Guide

### 1. Groq LLM

To utilize the cover letter generation feature, you need to set up Groq LLM:

1. Sign up for a [Groq](https://groq.com) account.
2. Create an API key.
3. Add the API key to your `.env` file.
4. (Optional) Set up the rate limiter module in the `nuxt.config.ts` 

### 2. Minio

Minio is used in this template to manage and serve static images, such as technology logos:

1. Follow the official Minio documentation to set up your instance [here](https://github.com/minio/minio-js).
2. Edit the `.env.example` file with your Minio environment variables.
3. Plug in your static files accordingly.

   You can further customize the Minio integration by editing the `minio.ts` and `images.ts` server files located in `server/api`.


> **Note:** If you prefer not to use Minio, you can modify the `ImageGrid.vue` component to load images directly from the `public` directory in your Nuxt application.

### 3. Typebot

For adding a custom, highly configurable chatbot:

1. Set up your [Typebot](https://typebot.io/) server.
2. Edit the `plugins/typebot.client.js` file with your bot's configuration.
3. Integrate it into your `nuxt.config.ts` file.

### 4. Animations

To incorporate animations, explore free options available on [Lottiefiles](https://lottiefiles.com/). You can easily add these animations to your portfolio like you can see in the `contact.vue` or `index.vue` page.

---

## Installation

Follow these steps to set up and run the project:

1. Clone the repository.
2. Install dependencies using your preferred package manager (`yarn`, `npm`, etc.). Example with `yarn`:
   ```
   yarn install
   ```
3. Edit your `.env` file and start the development server with:
   ```
   yarn dev
   ```

---

## Contributing

Contributions are welcome! If you have ideas for features, improvements, or bug fixes, feel free to submit an issue/pull request.

## License

This project is licensed under the MIT License. 

---

Feel free to tweak any section to better match your style or preferences. Happy coding 🚀
