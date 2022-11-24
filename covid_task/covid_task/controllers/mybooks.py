from odoo import http

from odoo import fields,models,api
from datetime import date
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.addons.payment.controllers import portal as payment_portal
from odoo.addons.payment import utils as payment_utils
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.addons.portal.controllers import portal
from odoo.addons.portal.controllers.portal import pager as portal_pager, get_records_pager

class MyBook(http.Controller):
    @http.route(['/my/books', '/my/books/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_books(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        print("__________________________________aaayyooooooooooooooooo")

        partner = request.env.user.partner_id
        book_user= partner.user_id
        Book = request.env['book.book']

        values = {
            'book_user':book_user,
            "page_name":'books'
        }
        # domain = self._prepare_quotations_domain(partner)

        # searchbar_sortings = self._get_sale_searchbar_sortings()

        # default sortby order
        # if not sortby:
        #     sortby = 'date'
        # sort_order = searchbar_sortings[sortby]['order']
        #
        # if date_begin and date_end:
        #     domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]

        # count for pager
        # book_count = Book.search_count(domain)
        book_count = request.env['book.book'].search_count([])
        print("_________________________________",book_count)
        # make pager
        pager = portal_pager(
            url="/my/books",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
            total=book_count,
            page=page,
            # step=self._items_per_page
        )
        # search the count to display, according to the pager data
        books =Book.search([])
        # request.session['my_book_history'] = books.ids[:100]

        values.update({
            'date': date_begin,
            'books': books.sudo(),
            'page_name': 'books',
            'pager': pager,
            'default_url': '/my/books',
            # 'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
        })
        return request.render("covid_task.books_template_custom", values)

    @http.route('/my/books/<model("book.book"):book_obj>/', type='http', auth="public", website=True)
    def book(self, book_obj, **kwargs):
        return request.render('covid_task.book_template', {'books': book_obj})