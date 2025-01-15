import random
import numpy as np

class MarkovTextGenerator:
    def __init__(self, text, n=2):

        self.n = n
        self.model = {}
        self.build_markov_model(text)

    def build_markov_model(self, text):
        words = text.split()
        for i in range(len(words) - self.n):
            key = tuple(words[i:i+self.n-1])  
            value = words[i+self.n-1]          
            if key not in self.model:
                self.model[key] = []
            self.model[key].append(value)

    def generate_text(self, length=50):
        current_key = random.choice(list(self.model.keys()))
        result = list(current_key)
        
        for _ in range(length - self.n + 1):
            if current_key in self.model:
                next_word = random.choice(self.model[current_key])
                result.append(next_word)
                current_key = tuple(result[-(self.n-1):])
            else:
                break  

        return ' '.join(result)

if __name__ == "__main__":
    text = "hi how are ther welcom"
    markov_generator = MarkovTextGenerator(text, n=3)
    generated_text = markov_generator.generate_text(length=20)
    print("Generated Text:\n", generated_text)
