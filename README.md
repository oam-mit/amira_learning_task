# Amira Intervention Challenge - Streamlit Application

[![Video Link](https://img.shields.io/badge/Video%20Link-8A2BE2)](https://drive.google.com/file/d/1LY2XrMrAU0TNf85XtXWcrb0unbStX7Mk/view?usp=sharing)

This project was developed as part of the Amira Intervention Challenge, aimed at improving reading comprehension at the word level using generative AI techniques. The application presents an interactive interface for both teachers and students, designed to handle micro-interventions for struggling readers. The micro-interventions are dynamically generated for each word, offering personalized, engaging experiences.

<!-- ## Features

1. Interactive Form: Users can input words, sentences, levels of understanding, and native language to generate tailored micro-interventions.
2. JSON Export: The application allows users to download the AI responses in JSON format for further use or review.
3. Follow-up Conversations: Users can engage in follow-up interactions by continuing the conversation in a chat interface, improving the depth and clarity of interventions. -->

## Thought Process

The core design of this application revolves around building micro-interventions at the word level, providing students with specific support based on their struggles with individual words in a passage. The thought process follows these principles:

1. Personalized Learning: By leveraging generative AI tools, the solution offers tailored interventions based on the word, sentence context, student's learning level, and their native language. This is critical in understanding a student's specific struggles with word recognition or pronunciation.

2. Engaging Interventions: The challenge called for creative and engaging ways to improve reading skills. The application's flexibility allows for prompts that can generate phonetic breakdowns, contextual meanings, sample dialogues, and activity suggestions, all of which can help make the learning process more engaging.

3. Seamless Interaction: The chat interface allows for smooth follow-up conversations. Students or teachers can ask follow-up questions about a word or instruction, and the generative model dynamically generates appropriate responses.

4. Modularity: Each intervention is built to be modular so that different components (e.g., phonemes, context, and activities) can be assembled to form a complete intervention. This makes the application extendable and adaptable for future development or platform integration.

## How to Run

### Prerequisites

1. Docker
2. Python

### Instructions

1. Clone the Repository

```
git clone https://github.com/oam-mit/amira_learning_task
```

2. Add a .env file in the project folder with your OpenAI API key

```
OPENAI_API_KEY=<your key>
```

3. Run with Docker Compose

```
docker-compose up --build
```

4. Access the Application
   Once the container is up, the Streamlit application will be accessible at http://localhost:8501.

## Example Outputs

Example outputs are given in the [Examples](https://github.com/oam-mit/amira_learning_task/tree/main/examples) folder.
