from flask import render_template, Blueprint, request, g

bp = Blueprint('error', __name__)

# Catch remaining errors
@bp.app_errorhandler(Exception)
def general(error):
    error_code = str(error)[:3]
    if error_code == '404':
        g.path = request.path
        
    g.error = error
    g.error_code = error_code
    return render_template("errors/general.html")