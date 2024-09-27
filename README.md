---
# Routes in Flask

This project is a simple Flask web application with three routes: Home, About, and Goodbye.
---

## Features

- **Home Route**: Displays a "Hello, World!" message.
- **About Route**: Displays an "This is the About page." message.
- **Goodbye Route**: Displays a "Goodbye, see you soon!" message.
---

## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install Flask
    ```
---

## Usage

1. **Run the application**:
    ```bash
    python app.py
    ```

2. **Access the routes**:
    - Home: `http://127.0.0.1:5000/`
    - About: `http://127.0.0.1:5000/about`
    - Goodbye: `http://127.0.0.1:5000/goodbye`
---

## Code Overview

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/about')
def about():
    return "This is the About page."

@app.route('/goodbye')
def goodbye():
    return "Goodbye, see you soon!"

if __name__ == '__main__':
    app.run(debug=True)
---
