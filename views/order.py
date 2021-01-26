from ABC import render_template,DB_obj, request, redirect,url_for,session
from . import bills
bill_obj = bills.B()
import _pickle as pickle
import datetime, sqlite3


class Ord:
    T_Scl = 'schools'
    T_Store = 'stores'
    T_companies = 'compnies'
    T_Products = 'compnies_stock'
    Company_select = ''
    Products = []
    Products_selected = []
    select_cat = ''
    Bill = 0
    institute = ''
    Selected_inst = ''
    customer = ''
    Paid_amount = 0
    Pending = 0
    All_companies = []
    Selected_product_with_quantity = list()

    #  fetching all companies,Stores,schools
    def Data_fetch(self):
        DB_obj.view(Ord.T_companies)
        Ord.All_companies = DB_obj.Data
        return render_template('Order.html', COMPANIES=Ord.All_companies, cat=Ord.select_cat, institute=Ord.institute, Selected_inst=Ord.Selected_inst,
                               selected_company=Ord.Company_select, Products=Ord.Products, Products_selected=Ord.Products_selected,
                               Bill=Ord.Bill, customer=Ord.customer, Receiver=session['user'],
                               Paid=Ord.Paid_amount, Pending=Ord.Pending)

    def company_selection(self,company):
        if request.method == 'POST':
            Ord.Company_select = request.form.get('companies')
            DB_obj.product_detail_view(company, Ord.Company_select, 'Company_Name')
            Ord.Products = DB_obj.Data
            return redirect(url_for('order_f'))

    def product_selection(self):
        if request.method == 'POST':
            pro = request.form.get('products')
            quantity = int(request.form.get('Quantity'))
            DB_obj.product_detail_view(Ord.T_Products, pro, 'Name')
            Data = DB_obj.Data
            Total_price = int(Data[0][7]) * int(quantity)
            Ord.Products_selected.append(list([str(pro), quantity, int(Data[0][7]), (Total_price)]))
            Ord.Bill += Total_price
            return redirect(url_for('order_f'))

    def category_selection(self):
        if request.method == 'POST':
            Ord.select_cat = request.form.get('cat')
            DB_obj.view(Ord.select_cat)
            Ord.institute = DB_obj.Data
            return redirect(url_for('order_f'))

    def info(self):
        if request.method == 'POST':
            Ord.Selected_inst = request.form.get('place')
            Ord.customer = request.form.get('customer')
            return redirect(url_for('order_f'))

    def calculation(self):
        if request.method == 'POST':
            Ord.Paid_amount = request.form.get('BILL')
            Ord.Pending = int(Ord.Bill) - int(Ord.Paid_amount)
            return redirect(url_for('order_f'))

    def bill_generater(self):
        if Ord.Paid_amount == '0' or Ord.Paid_amount == 0:
            Ord.Pending = Ord.Bill
            print(Ord.Pending, Ord.Bill)
        D = str(datetime.datetime.now()).split(' ')
        Time = D[1].split('.')[0]
        Date = D[0]

        # updating pending Amount
        DB_obj.pending_updat('Pending', Ord.Selected_inst, Ord.Pending)

        # Stock Managing
        for i in range(len(Ord.Products_selected)):
            product_name = Ord.Products_selected[i][0]
            selected_quantity = Ord.Products_selected[i][1]
            DB_obj.stock_alter('compnies_stock', product_name, selected_quantity)

        for i in Ord.Products_selected:
            Ord.Selected_product_with_quantity.append(i)
        pickle_obj = pickle.dumps(Ord.Selected_product_with_quantity)
        return bill_obj.Order_Bill(Ord.Selected_inst, 'bills', Ord.Bill, session['user'],
                                   Ord.Paid_amount, Ord.customer, Ord.Pending, Time, Date,
                                   pickle_obj)

    def reset(self):
            Ord.Company_select = ''
            Ord.Products = []
            Ord.Products_selected = []
            Ord.Bill = 0
            Ord.institute = ''
            Ord.Selected_inst = ''
            Ord.customer = ''
            Ord.Paid_amount = 0
            Ord.Pending = 0
            Ord.Selected_product_with_quantity = []
            Ord.select_cat = ''
            Ord.All_companies = []
            return redirect(url_for('order_f'))
