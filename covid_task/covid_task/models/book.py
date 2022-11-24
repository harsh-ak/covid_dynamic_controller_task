from odoo import fields,models,api
from datetime import date


class Book(models.Model):
    _name="book.book"

    name= fields.Char(string="Name")
    book_type=fields.Selection([('New','New'),('Old','Old')])
    user_id=fields.Many2one(comodel_name="res.users",string="User Name")







