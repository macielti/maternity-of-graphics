from flask import Flask
from flask_cors import CORS
from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

# CORS
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
