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
    	probabilities = np.random.dirichlet(np.ones(len(self.topics)), size=1)[0]
    	# numpy.float64 zu Python float konvertieren und auf 4 Nachkommastellen runden
    	probabilities = [round(float(p), 4) for p in probabilities]
    	return dict(zip(self.topics, probabilities))

