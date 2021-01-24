from . import Application, DB_obj, redirect, url_for, login_required
from .views import login, school, store, stock, HOME, bills, order, invoice


Log_obj = login.Log_handel()
scl_obj = school.Scl()
store_obj = store.Local_store()
stock_obj = stock.St()
Home_obj = HOME.H()
bill_obj = bills.B()
ord_obj = order.Ord()
inv_ob = invoice.Inv()


# for login page
@Application.route('/login', methods=['GET', 'POST'])
def login():
    return Log_obj.Login()


# for Users

@Application.route('/users')
@login_required
def users():
    return Log_obj.all_users()


# for Home page
@Application.route('/', methods=['GET', 'POST'])
@Application.route('/home', methods=['GET', 'POST'])
@login_required
def Home():
    ord_obj.reset()
    return Home_obj.Home()


# for schools page
@Application.route('/home/schools', methods=['GET', 'POST'])
def school():
    return scl_obj.view()


# For view local store page
@Application.route('/home/local_store', methods=['GET', 'POST'])
@login_required
def store():
    return store_obj.view()


# for view companies which stock we have
@Application.route('/home/stock', methods=['GET', 'POST'])
@login_required
def total_stoke():
    return stock_obj.view()


# for view companies details stock
@Application.route('/home/t_stock/detail/<company>', methods=['GET', 'POST'])
@login_required
def t_stock_detail(company):
    return stock_obj.Add(company)


# for the deletion process
@Application.route('/<Function>/delete/<Name>/<Table>/<COM>')
@Application.route('/<Function>/delete/<Name>/<Table>')
@login_required
def Delete(Name, Table, Function, COM=None):
    DB_obj.delete(Name, Table)
    if COM==None:
        DB_obj.delete1(Name, 'compnies_stock')
        return redirect(url_for(Function))
    else:

        return redirect(url_for(Function, company=COM))


# this is for bills of institutes
@Application.route('/home/bill/<company>', methods=['GET', 'POST'])
@login_required
def bill(company):
    return bill_obj.view(company)


@Application.route('/logout')
@login_required
def logout():
    return Log_obj.logout()


# this will open a new order tab
@Application.route('/home/order', methods=['GET', 'POST'])
@login_required
def order_f():
    return ord_obj.Data_fetch()


# this route is for selection of products and adding them in bill area in order template
@Application.route('/product', methods=['GET','POST'])
def P():
    return ord_obj.product_selection()


# this route is for selection of company to filter products on the order template.
@Application.route('/company/<company>', methods=['GET', 'POST'])
def C(company):
    return ord_obj.company_selection(company)


# This route is for selection of for what you are taking order
@Application.route('/category', methods=['GET', 'POST'])
def Category():
    return ord_obj.category_selection()


# This route is for selection of Place name and customer name
@Application.route('/place', methods=['GET', 'POST'])
def place():
    return ord_obj.info()


# This route is for making new order
@Application.route('/new_order')
def new_order():
    return ord_obj.reset()


# this is for getting Paid bill amount and calculation of pending amount
@Application.route('/Bill', methods=['GET', 'POST'])
def BILL():
    return ord_obj.calculation()


@Application.route('/bill_generated')
def generated():
    return ord_obj.bill_generater()


@Application.route('/stock_Update/<table>/<Name>')
def stock_update(table, Name):
    return stock_obj.update(table, Name)


@Application.route('/After_Stock_UPDATE/<table>/<Name>/<company>/<Previous_Available>/<Sold>', methods=['GET', 'POST'])
def Stock_update_save(table, Name, company, Previous_Available, Sold):
    return stock_obj.after_update(table, Name, company, Previous_Available, Sold)


@Application.route('/Update/<company>', methods=['GET', 'POST'])
def up_pend(company):
    return bill_obj.dues_update(company)


@Application.route('/home/invoice/<id>/<index>')
def pdf_templete(id, index):
    return inv_ob.view_invoice(id, index)


@Application.route('/delete/<value>/<table>/<company>')
def del_bill(table, company, value):
    return bill_obj.deL_bill(table, company, value)


if __name__ == '__main__':
    Application.run(debug=True)
