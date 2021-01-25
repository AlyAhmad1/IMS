from ABC import session, request, DB_obj, render_template


class H:
    def Home(self):
        if session['user'] == 'ADMIN':
            if request.method == 'POST':
                N_User = request.form.get('User')
                N_Password = request.form.get('Password')
                DB_obj.new_user(N_User, N_Password)
            return render_template('Admin_home.html')
        else:
            return render_template('local_home.html')
