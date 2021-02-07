from ABC import render_template, request, redirect, url_for, DB_obj, session,FlaskForm,StringField,PasswordField,InputRequired


class Log_handel():
    T_Name = 'login'

    def Login(self):
        try:
            if session['user']:
                return redirect(url_for('Home'))
        except:
            if request.method == 'POST':
                User = request.form.get('User')
                Password = request.form.get('Password')
                DB_obj.view(Log_handel.T_Name)
                for i in DB_obj.Data:
                    if User == i[0] and Password == i[1]:
                        if User == 'admin':
                            session['user'] = 'ADMIN'
                            return redirect(url_for('Home'))
                        else:
                            session['user'] = 'LOCAL'
                            return redirect(url_for('Home'))
            return render_template('login_page.html')

    def logout(self):
        if 'user' in session:
            session.pop('user')
            return redirect('/login')

    def all_users(self):
        DB_obj.view('login')
        rows = DB_obj.Data
        return render_template('Users.html', rows=rows)
