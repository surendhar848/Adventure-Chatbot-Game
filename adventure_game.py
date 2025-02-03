import random
import nltk
from nltk.chat.util import Chat, reflections

# Download the punkt tokenizer from nltk if it's not already present
nltk.download('punkt')

# Responses from the AI for different actions
responses = {
    "greet": [
        "Hello, brave adventurer! What would you like to do today?",
        "Greetings! Ready to embark on a new adventure?",
        "Hi there! What is your next move?",
    ],
    "talk_to_npc": [
        "The NPC smiles and greets you. 'What can I do for you today?'",
        "You approach the NPC, who asks, 'Need any help on your journey?'",
    ],
    "go_forest": [
        "You walk into the dense forest, hearing the sounds of wildlife.",
        "The forest is quiet, except for the rustling of leaves in the breeze.",
    ],
    "go_castle": [
        "You approach the grand castle gates. The guards look at you warily.",
        "The majestic castle looms before you. The doors are open, but no one is around.",
    ],
    "unknown": [
        "I don't understand that. Can you try something else?",
        "Hmm, not sure what you're asking. Could you rephrase that?",
    ],
}

# AI Chatbot Responses
pairs = [
    (r"hi|hello|hey", (lambda: random.choice(responses["greet"]))),
    (r"talk to npc", (lambda: random.choice(responses["talk_to_npc"]))),
    (r"go forest", (lambda: random.choice(responses["go_forest"]))),
    (r"go castle", (lambda: random.choice(responses["go_castle"]))),
    (r".*", (lambda: random.choice(responses["unknown"]))),  # Catch-all for unrecognized input
]

# Creating the chatbot instance
class AdventureChat(Chat):
    def respond(self, user_input):
        for pattern, response_func in self._pairs:
            if nltk.re.match(pattern, user_input):
                return response_func()  # Call the function to get a random response
        return random.choice(responses["unknown"])

chatbot = AdventureChat(pairs, reflections)

# Game Introduction
def intro():
    print("Welcome to the Adventure Game!")
    print("Type 'quit' to end the game at any time.")
    print("You can try commands like 'talk to npc', 'go forest', or 'go castle'.")
    print("Let's start your adventure!")

def main():
    intro()

    while True:
        user_input = input("\nYou: ").lower()

        if user_input == "quit":
            print("Goodbye, adventurer!")
            break

        response = chatbot.respond(user_input)
        print(f"AI: {response}")  # No need for random.choice() here

if __name__ == "__main__":
    main()
