from flask import render_template, redirect, url_for, flash, session

# import the basic blue print instance
from app.architecture import architecture


@architecture.route('/')
def architecture_view():
    """-------------------------------------------------------------------------------------
Go to architecture ML page

    Parameters :
    None

    Returns :
    redirection to login if no session or architecture ml if session

   -------------------------------------------------------------------------------------"""

    if not session:
        flash("access not authorized", "danger")
        return redirect(url_for('main.login'))
    else:

        
        return render_template(
            'architecture/architecture.html'
            ) 