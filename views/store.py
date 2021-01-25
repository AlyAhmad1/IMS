from ABC import render_template, DB_obj, redirect, url_for, request, session


class Local_store:
    T_Name = 'stores'

    # For View the school Page.
    def view(self):
        if session['user'] == 'ADMIN':
            if request.method == 'POST':
                Name = request.form.get('Name')
                # Calling function for add new Local_store in the list
                DB_obj.Add_new(Name, Local_store.T_Name)

                DB_obj.view(Local_store.T_Name)
                return render_template('local_store.html', rows=DB_obj.Data, T_Name=Local_store.T_Name)
            DB_obj.view(Local_store.T_Name)
            return render_template('local_store.html', rows=DB_obj.Data, T_Name=Local_store.T_Name)
        else:
            DB_obj.view(Local_store.T_Name)
            return render_template('local_store_local_user.html', rows=DB_obj.Data)


obj = Local_store()
