{
    'name' : 'Covid Task',
    'version' : '1.0',
    'sequence': -200,
    'description': "This is Task",
    #'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['website'],
    'data': [
        'controllers/template_inherit.xml',
        'controllers/book_template.xml',
        'views/template_inherit.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

}