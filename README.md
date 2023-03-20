# Chatbot based on rasa framework

### About
Conversation assistant is developed to communicate with recruiters,
it can talk to you about my skills, experience or job preferences.

The assistant is still in development, it's my long-term hobby project.

This chatbot was built using [Rasa](https://rasa.com/docs/getting-started/).

### Getting Started
Install [Rasa](https://rasa.com/docs/rasa/user-guide/installation/#installation).

Or you can install python 3.8.4 and install libraries from requirements file.

### Visualisation
[Graph](https://github.com/nebylamarek/Rasa_project/blob/master/graph.html)

This graph visualizes the internal patterns and rules of communication.

### Train the chatbot
```
rasa train
```

### Talk to chatbot
```
rasa shell
```

## Run chatbot integrated on a frontend site
[Frontend](https://github.com/nebylamarek/Rasa_project/blob/master/index.html)
```
rasa run -m models --enable-api --cors "*"
```
