from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue dans mon application Flask ! 🚀"

@app.route('/hello')
def hello():
    return 'Bonjour depuis Flask ! 👋'
    
@app.route('/bonjour/<prenom>')
def greet(prenom):
    return f"Bonjour, {prenom.capitalize()} ! 😄"

@app.route('/articles', methods=['GET'])
def list_articles():
    return {'articles': ['Article 1', 'Article 2', 'Article 3']}
    
if __name__ == '__main__':
    app.run(debug=True)
