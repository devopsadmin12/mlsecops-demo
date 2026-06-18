import pickle

class SafeModel:
    def predict(self):
        return "safe prediction"

with open("models/safe.pkl", "wb") as f:
    pickle.dump(SafeModel(), f)

print("safe.pkl created")