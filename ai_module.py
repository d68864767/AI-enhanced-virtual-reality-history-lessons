```python
# ai_module.py

import history_data

class AI:
    def __init__(self):
        self.lessons = history_data.get_lessons()
        self.current_lesson = 0

    def get_next_lesson(self):
        if self.current_lesson >= len(self.lessons):
            return None
        lesson = self.lessons[self.current_lesson]
        self.current_lesson += 1
        return lesson
```
