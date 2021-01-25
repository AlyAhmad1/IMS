from ABC import render_template, request, DB_obj,redirect,url_for, session, make_response
import pdfkit
import _pickle as pickle


class B:
    T_Name = 'bills'
    # Pending_Amount = 0
    Total_Pending_Amount = 0
    rows = []

    # this function is for if you want to add a bill manually in related institute
    def view(self,institute):
        try:
            DB_obj.product_detail_view('Pending',institute,'Name')
            B.rows = DB_obj.Data
            B.Total_Pending_Amount=B.rows[0][1]
        except:
            B.Total_Pending_Amount = 0
        DB_obj.product_detail_view(B.T_Name,institute,'Name')
        B.rows = DB_obj.Data

        return render_template('bill.html', school=institute, rows=B.rows,Total_Pending_Amount=B.Total_Pending_Amount,
                               USER = session['user'])

    # it is function when bill created after order
    def Order_Bill(self, Company_select, table, Bill, Reciever, Paid_amount, Customer, Pending, Time, Date, ALL_LIST):
        DB_obj.BiLL_detail(Company_select, table, Bill, Reciever, Paid_amount, Customer, Pending, Time, Date, ALL_LIST)
        return redirect(url_for('new_order'))

    def dues_update(self, company):
        if request.method == 'POST':
            Amount = request.form.get('Amount')
            DB_obj.pen_update(company, Amount)
        return redirect(url_for('bill', company=company))

    def deL_bill(self, Table, company, value):
        DB_obj.delete_bill(Table,'Id',value)
        return redirect(url_for('bill',company=company))

