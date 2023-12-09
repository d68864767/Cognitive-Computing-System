```python
# Import necessary modules
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class Learner:
    def __init__(self):
        self.model = RandomForestClassifier()

    def learn(self, analyzed_data, target):
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(analyzed_data, target, test_size=0.2, random_state=42)

        # Train the model
        self.model.fit(X_train, y_train)

        # Evaluate the model
        score = self.model.score(X_test, y_test)

        return score
```
