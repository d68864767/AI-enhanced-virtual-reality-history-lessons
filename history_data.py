```python
# history_data.py

# Import necessary modules
import json

# Define the path to the history data file
DATA_FILE_PATH = "path/to/your/data/file.json"

# Define a variable to hold the history lessons
lessons = []

def load_data():
    """
    Load the history data from the JSON file.
    """
    global lessons
    with open(DATA_FILE_PATH, 'r') as f:
        lessons = json.load(f)

def get_lessons():
    """
    Return the history lessons.
    """
    return lessons
```
