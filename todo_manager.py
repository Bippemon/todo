import json

FILE_PATH = "data.json"

def load_todos():
    try:
        # läser "data.json". returnar listan
        with open(FILE_PATH, "r") as file:
            data = file.read()
            return json.loads(data) if data else []
        
    # om fil inte finns eller inte gå att läsa - returna tom lista
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_todos(todos):
    try:
        # sparar i "data.json"
        with open(FILE_PATH, "w") as file:
            json.dump(todos, file)
    
    except FileNotFoundError:
        # skapar ny fil och sparar om inte finns
        with open(FILE_PATH, "x") as file:
            json.dump(todos, file)

# test
if __name__ == "__main__":
    print(load_todos())