from flask import Flask
from routes import asset_routes

app = Flask(__name__)
app.register_blueprint(asset_routes.asset_bp, url_prefix='/assets')

if __name__ == "__main__":
    app.run(debug=True)
