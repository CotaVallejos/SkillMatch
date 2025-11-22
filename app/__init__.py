from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Importar y registrar blueprints *dentro* de create_app
    from .routes import api_bp
    app.register_blueprint(api_bp)

    @app.route("/")
    def health():
        return "Flask listo ✅"

    return app
