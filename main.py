from App import Application, DB_obj, redirect, url_for, login_required
from App.views import login, school, store, stock, HOME, bills, order, invoice


Log_obj = login.Log_handel()
scl_obj = school.Scl()
store_obj = store.Local_store()
stock_obj = stock.St()
Home_obj = HOME.H()
bill_obj = bills.B()
ord_obj = order.Ord()
inv_ob = invoice.Inv()


# for login page
@Application.route('/App/templates/login', methods=['GET', 'POST'])
def login():
    return Log_obj.Login()


# for Users

@Application.route('/users')
@login_required
def users():
    return Log_obj.all_users()


# for Home page
@Application.route('/App/templates/', methods=['GET', 'POST'])
@Application.route('/App/templates/home', methods=['GET', 'POST'])
@login_required
def Home():
    ord_obj.reset()
    return Home_obj.Home()


# for schools page
@Application.route('/App/templates/home/schools', methods=['GET', 'POST'])
def school():
    return scl_obj.view()


# For view local store page
@Application.route('/App/templates/home/local_store', methods=['GET', 'POST'])
@login_required
def store():
    return store_obj.view()


# for view companies which stock we have
@Application.route('/App/templates/home/stock', methods=['GET', 'POST'])
@login_required
def total_stoke():
    return stock_obj.view()


# for view companies details stock
@Application.route('/App/templates/home/t_stock/detail/<company>', methods=['GET', 'POST'])
@login_required
def t_stock_detail(company):
    return stock_obj.Add(company)


# for the deletion process
@Application.route('/App/templates/<Function>/delete/<Name>/<Table>/<COM>')
@Application.route('/App/templates/<Function>/delete/<Name>/<Table>')
@login_required
def Delete(Name, Table, Function, COM=None):
    DB_obj.delete(Name, Table)
    if COM==None:
        DB_obj.delete1(Name, 'compnies_stock')
        return redirect(url_for(Function))
    else:

        return redirect(url_for(Function, company=COM))


# this is for bills of institutes
@Application.route('/App/templates/home/bill/<company>', methods=['GET', 'POST'])
@login_required
def bill(company):
    return bill_obj.view(company)


@Application.route('/App/templates/logout')
@login_required
def logout():
    return Log_obj.logout()


# this will open a new order tab
@Application.route('/App/templates/home/order', methods=['GET', 'POST'])
@login_required
def order_f():
    return ord_obj.Data_fetch()


# this route is for selection of products and adding them in bill area in order template
@Application.route('/App/templates/product', methods=['GET','POST'])
def P():
    return ord_obj.product_selection()


# this route is for selection of company to filter products on the order template.
@Application.route('/App/templates/company/<company>', methods=['GET', 'POST'])
def C(company):
    return ord_obj.company_selection(company)


# This route is for selection of for what you are taking order
@Application.route('/App/templates/category', methods=['GET', 'POST'])
def Category():
    return ord_obj.category_selection()


# This route is for selection of Place name and customer name
@Application.route('/App/templates/place', methods=['GET', 'POST'])
def place():
    return ord_obj.info()


# This route is for making new order
@Application.route('/App/templates/new_order')
def new_order():
    return ord_obj.reset()


# this is for getting Paid bill amount and calculation of pending amount
@Application.route('/App/templates/Bill', methods=['GET', 'POST'])
def BILL():
    return ord_obj.calculation()


@Application.route('/App/templates/bill_generated')
def generated():
    return ord_obj.bill_generater()


@Application.route('/App/templates/stock_Update/<table>/<Name>')
def stock_update(table, Name):
    return stock_obj.update(table, Name)


@Application.route('/App/templates/After_Stock_UPDATE/<table>/<Name>/<company>/<Previous_Available>/<Sold>', methods=['GET', 'POST'])
def Stock_update_save(table, Name, company, Previous_Available, Sold):
    return stock_obj.after_update(table, Name, company, Previous_Available, Sold)


@Application.route('/App/templates/Update/<company>', methods=['GET', 'POST'])
def up_pend(company):
    return bill_obj.dues_update(company)


@Application.route('/App/templates/home/invoice/<id>/<index>')
def pdf_templete(id, index):
    return inv_ob.view_invoice(id, index)


@Application.route('/App/templates/delete/<value>/<table>/<company>')
def del_bill(table, company, value):
    return bill_obj.deL_bill(table, company, value)


if __name__ == '__main__':
    Application.run(debug=True)
