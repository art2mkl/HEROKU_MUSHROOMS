from flask import render_template, redirect, url_for, flash, session

# import the basic blue print instance
from app.basic import basic


@basic.route('/')
def basic_view():
    """-------------------------------------------------------------------------------------
Go to Basic ML page

    Parameters :
    None

    Returns :
    redirection to login if no session or basic ml if session

   -------------------------------------------------------------------------------------"""

    if not session:
        flash("access not authorized", "danger")
        return redirect(url_for('main.login'))
    else:

        
        return render_template(
            'basic/basic.html'
            ) 