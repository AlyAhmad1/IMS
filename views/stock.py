from App import render_template, request, redirect, url_for, DB_obj, session


class St:
    T_Name = 'compnies'
    T_Name1 = 'compnies_stock'
    Data_update = [1,2,3,4,5,6,7,8]

    # function for view company name on the Stoke page
    def view(self):
        if request.method == 'POST':
            Name = request.form.get('Name')

            # Adding New Company
            DB_obj.Add_new(Name,St.T_Name)

            # Collecting all Data
            DB_obj.view(St.T_Name)
            return render_template('t_stock.html', rows=DB_obj.Data, T_Name=St.T_Name)
        DB_obj.view(St.T_Name)
        return render_template('t_stock.html', rows=DB_obj.Data, T_Name=St.T_Name)

    # function for adding stock items in the company items page
    def Add(self,company):
        if session['user'] == 'ADMIN':
            if request.method == 'POST':
                Item_Name = request.form.get('Item_Name')
                Price_Pi = request.form.get('Price_Pi')
                Total_items = request.form.get('Total_items')
                Total_Price = int(Price_Pi) * int(Total_items)
                sold_items = request.form.get('sold_items')
                available_items = int(Total_items) - int(sold_items)
                sell_price = request.form.get('Sell')
                Profit = (int(Total_items) * int(sell_price)) - int(Total_Price)

                DB_obj.add_item(company,Item_Name, Price_Pi, Total_Price, Total_items, sold_items, available_items, sell_price,Profit)
                DB_obj.product_detail_view(St.T_Name1, company,'Company_Name')
                return render_template('t_stock_detail.html', rows=DB_obj.Data, company=company, T_Name=St.T_Name1 ,Data_update=St.Data_update)
            DB_obj.product_detail_view(St.T_Name1, company,'Company_Name')
            return render_template('t_stock_detail.html', rows=DB_obj.Data, company=company, T_Name=St.T_Name1)
        else:
            DB_obj.product_detail_view(St.T_Name1, company,'Company_Name')
            return render_template('t_stock_detail_local_user.html', rows=DB_obj.Data, company=company)

    #  this function execute when we enter in update stock page
    def update(self,table,Name):
        DB_obj.product_detail_view(table,Name,'Name')
        St.Data_update=DB_obj.Data
        return render_template('Update_Stock.html' , Data_update=St.Data_update)

        #  this function execute when we exit in update stock page and go to total stock page
    def after_update(self,table,P_Name,company,after_update,sold):
        if request.method == 'POST':
            Name = request.form.get('Item_Name')
            Quantity = request.form.get('Total_items')
            Buy_Price =  request.form.get('Price_Pi')
            Sell_Price = request.form.get('Sell')
            Company_Name = request.form.get('Comp')
            Available = request.form.get('Available')
            if int(Available)>int(after_update):
                Available_Updated = int(Available)-int(after_update)
                Q = int(Available_Updated) + int(Quantity)
            else:
                Available_Updated = int(after_update)-int(Available)
                Q = int(Quantity) - int(Available_Updated)

            Updated_total_price = Q*int(Buy_Price)
            Updated_profit = (Q*int(Sell_Price)) - Updated_total_price
            DB_obj.stock_update(table, P_Name, Name, Q, Buy_Price, Sell_Price, Company_Name, Available, Updated_total_price, Updated_profit)
            return redirect(url_for('t_stock_detail',company=company))
