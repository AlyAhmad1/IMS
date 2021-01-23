from App import render_template, request, DB_obj, session


class Scl:

    T_Name = 'schools'

    # For View the school Page.
    def view(self):
        if session['user'] == 'ADMIN':
            if request.method == 'POST':
                Name = request.form.get('Name')

                # Calling function for add new School in the list
                DB_obj.Add_new(Name, Scl.T_Name)

                DB_obj.view(Scl.T_Name)
                return render_template('schools.html', rows=DB_obj.Data, T_Name=Scl.T_Name)
            DB_obj.view(Scl.T_Name)
            return render_template('schools.html', rows=DB_obj.Data, T_Name=Scl.T_Name)
        else:
            DB_obj.view(Scl.T_Name)
            return render_template('schools_local_user.html', rows=DB_obj.Data)
