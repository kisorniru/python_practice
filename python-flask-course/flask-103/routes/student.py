from flask import Blueprint

# Create a Blueprint for the student routes
student_bp = Blueprint("student", __name__)

@student_bp.route("/")
def student():
    return "This is the student route."

# --- ADD THIS DELIBERATE BUG ROUTE FOR TESTING ---
@student_bp.route("/test-crash", methods=["GET"])
def test_crash():
    # This is mathematically impossible and will force a massive Python crash
    broken_calculation = 10 / 0 
    return f"The result is {broken_calculation}"