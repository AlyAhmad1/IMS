from ABC import render_template, make_response, DB_obj
import pdfkit
import _pickle as pickle


class Inv:
    def view_invoice(self, id, index):
        DB_obj.product_detail_view('bills', id, 'id')
        rows = DB_obj.Data
        rows_A = pickle.loads(rows[0][9])
        rendered = render_template('invoice.html', index=index, rows=rows_A, customer=rows[0][6], pending=rows[0][4], total=rows[0][2])
        css = 'App/static/invoice.css'
        pdf_gen = pdfkit.from_string(rendered, False, css=css)
        response = make_response(pdf_gen)
        response.headers['content-type'] = 'application/pdf'
        response.headers['content-Disposition'] = 'inline; filename= output.pdf'     # inline can be attachment
        response.close()
        return response
