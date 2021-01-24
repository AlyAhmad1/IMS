import sqlite3


class DataBase:
    Data = []
    @staticmethod
    def Connection():
        con = sqlite3.connect('Data.db')
        cur = con.cursor()
        return con, cur

    # for  add_new school/Local_Store in list
    def Add_new (self, Name, T_Name):
        con, cur=DataBase.Connection()
        cur.execute(f'insert into "{T_Name}"(Name) values("{Name}")')
        con.commit()
        con.close()

    # for view all list of school/Local_Store on home page
    def view(self,T_Name):
        con, cur=DataBase.Connection()
        cur.execute(f'select * from {T_Name};')
        rows = cur.fetchall()
        DataBase.Data = rows
        con.close()

    # for delete or remove Schools/Local_Store from school list
    def delete(self, name, T_Name):
        con, cur = DataBase.Connection()
        cur.execute(f'delete from "{T_Name}" where Name = "{name}"')
        con.commit()
        cur.execute(f'delete from bills where Name = "{name}"')
        con.commit()
        cur.execute(f'delete from Pending where Name = "{name}"')
        con.commit()
        con.close()


    # for Adding New User
    def new_user(self,user,password):
        with sqlite3.connect('Data.db') as con:
            cur = con.cursor()
            cur.execute(f'insert into login(Name,Password) values("{user}","{password}")')
            con.commit()
        con.close()

    # for Add new Item in Stock
    def add_item(self, Company_Name, Item_Name, Price_Pi, Total_Price, Total_items, sold_items, available_items, sell_price,Profit):
        con, cur=DataBase.Connection()
        cur.execute(f'insert into compnies_stock(Company_Name,Name, Price_Pi, Total_Price, Total_items, sold_items, available_items,sell_price,Profit) values("{Company_Name}","{Item_Name}", "{Price_Pi}", "{Total_Price}", "{Total_items}", "{sold_items}", "{available_items}","{sell_price}","{Profit}")')
        con.commit()
        con.close()

    def BiLL_detail(self, school, T_Name, T_Bill, Reciever, Paid_Amount, Paid_by, Pending_Amount, Time, Date, ALL_LIST):
        con, cur = DataBase.Connection()

        L = [school, T_Bill, Paid_Amount, Pending_Amount, Date, Paid_by, Reciever, Time, ALL_LIST]
        cur.execute('''insert into bills (Name, Total_Amount,Paid_Amount,Pending_Amount,Paid_Date,Paid_By,Recieved_By,Paid_Time,All_items)
                        values(?,?,?,?,?,?,?,?,?)''', (L))
        con.commit()
        con.close()

    # this is for fetching given company like store/school
    def product_detail_view(self, T_Name, Company_Name, Name):
        con, cur=DataBase.Connection()
        cur.execute(f'select * from {T_Name} where {Name}="{Company_Name}";')
        rows = cur.fetchall()
        DataBase.Data = rows
        con.close()

    # Alter table stock for alter available sold stock when any order occur
    def stock_alter(self, T, N, Q):
        con, cur = DataBase.Connection()
        cur.execute(f'select * from {T} where Name = "{N}"')
        rows = cur.fetchone()
        available_stock = rows[5]
        current_sold = int(rows[4]) + int(Q)
        current_stock = int(available_stock) - int(Q)
        cur.execute(f'UPDATE {T} SET available_items = "{current_stock}", sold_items = "{current_sold}" WHERE Name = "{N}";')
        con.commit()
        con.close()

    def pending_updat(self, table, institute, Pending):
        con, cur = DataBase.Connection()
        try:
            cur.execute(f'select * from {table} where Name = "{institute}"')
            rows = cur.fetchall()
            current_pending = rows[0][1]
            T_Pending = int(current_pending) + int(Pending)
            cur.execute(f'UPDATE Pending SET pending = "{T_Pending}" WHERE Name= "{institute}"')
            con.commit()
            con.close()
        except:
            cur.execute(f'insert into {table} (Name,Pending) values("{institute}","{Pending}")')
            con.commit()
            con.close()

    # this will execute when admin update stock
    def stock_update(self, table, P_Name, A, B, C, D, E, F, G, H):
        con, cur = DataBase.Connection()
        cur.execute(f'UPDATE {table} SET Total_Price={G}, Name = "{A}",Total_items="{B}",Price_Pi="{C}", Company_Name="{E}",Profit = {H}, available_items={F} , sell_price="{D}" WHERE Name= "{P_Name}"')
        con.commit()
        con.close()

    # this function for when we delete a company and stock will get delete that inside this company.
    def delete1(self, name, T_Name):
        con, cur = DataBase.Connection()
        cur.execute(f'delete from "{T_Name}" where Company_Name = "{name}"')
        con.commit()
        con.close()

    def pen_update(self, institute, value):
        con, cur = DataBase.Connection()
        cur.execute(f'select * from Pending where Name = "{institute}"')
        rows = cur.fetchall()
        current_pending = rows[0][1]
        if int(current_pending) == 0:
            T_Pending = 0
        else:
            T_Pending = int(current_pending) - int(value)
        if T_Pending < 0:
            T_Pending = 0
        cur.execute(f'UPDATE Pending SET pending = "{T_Pending}" WHERE Name= "{institute}"')
        con.commit()
        con.close()

    # Deleting Bill
    def delete_bill(self,T_Name,condition,value):
        con, cur=DataBase.Connection()
        cur.execute(f'delete from "{T_Name}" where {condition} = "{value}"')
        con.commit()
        con.close()

