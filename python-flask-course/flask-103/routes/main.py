from flask import Blueprint, jsonify, current_app

# Create a Blueprint for the main routes
main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def main():
    return "Welcome to the Flask 103 course! This is the main route of the application."

@main_bp.app_errorhandler(404)
def global_404_handler(error):
    # This catches any unmatched URL paths across your entire site
    return jsonify({
        "status": 404,
        "error": "Resource Not Found",
        "message": "Please check your URL path and try again."
    }), 404

@main_bp.app_errorhandler(500)
def global_500_handler(error):
    # 1. Log the absolute real crash details to your server terminal for debugging
    # The 'error' object contains the exact code line and traceback that broke
    current_app.logger.error(f"Server Error Encountered: {error}")

    # 2. Return a clean, polite, safe message to the user/client API
    return jsonify({
        "status": 500,
        "error": "Internal Server Error",
        "message": "Something went wrong on our servers. Our development team has been notified."
    }), 500

# --- ADD THIS DELIBERATE BUG ROUTE FOR TESTING ---
@main_bp.route("/test-crash", methods=["GET"])
def test_crash():
    # This is mathematically impossible and will force a massive Python crash
    broken_calculation = 10 / 0 
    return f"The result is {broken_calculation}"