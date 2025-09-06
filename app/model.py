import numpy as np

class DummyTopicModel:
    def __init__(self):
        # Beispielhafte 20 Topics (mit GenAI generiert)
        self.topics = [
            "soccer", "food", "stockmarket", "travel", "fitness",
            "fashion", "gaming", "tech", "music", "movies",
            "health", "politics", "education", "finance", "art",
            "science", "nature", "pets", "photography", "books"
        ]

    def predict(self, text: str):
        """
        Simuliert eine Multi-Label Klassifikation.
        Gibt Wahrscheinlichkeiten für jedes Topic zurück.
        """
        # Dirichlet-Verteilung erzeugt Wahrscheinlichkeiten, die sich zu 1 summieren
        probabilities = np.random.dirichlet(np.ones(len(self.topics)), size=1)[0]

        # Rückgabe als Dictionary
        return dict(zip(self.topics, probabilities))
