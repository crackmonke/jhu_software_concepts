# Personal Website

This is a personal website for a JHU assignment.

## Dependencies
* Windows OS
* Python 3.10+
* pip
* (Optional) Docker

## Set up

1. **Clone the repository** and navigate to the project folder.

2. **Create and activate a virtual environment:**
   ```
   python -m venv venv
   venv\Scripts\activate   # On Windows
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Running Locally

1. **Run the website:**
   ```
   python run.py
   ```

2. **Open your browser and go to:**  
   http://localhost:8080

## Running with Docker

1. **Build the Docker image:**
   ```
   docker build -t personal-site .
   ```

2. **Run the Docker container:**
   ```
   docker run -p 8080:8080 personal-site
   ```

3. **Open your browser and go to:**  
   http://localhost:8080

## Authors
* crackmonke - Savy

## Acknowledgements
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* https://realpython.com/flask-project/
