import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app() -> Flask:
    app = Flask(__name__, template_folder="templates")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-change-this-secret")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///byteguard.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Secure cookie settings for CSRF/session hardening.
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SECURE"] = False
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)

    from .models import User  # noqa: WPS433

    @login_manager.user_loader
    def load_user(user_id: str):
        return User.query.get(int(user_id))

    @app.after_request
    def set_security_headers(response):
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Content-Security-Policy"] = "frame-ancestors 'none'; default-src 'self';"
        return response

    from .auth_routes import auth_bp  # noqa: WPS433
    from .post_routes import post_bp  # noqa: WPS433

    app.register_blueprint(auth_bp)
    app.register_blueprint(post_bp)

    with app.app_context():
        db.create_all()

    return app
