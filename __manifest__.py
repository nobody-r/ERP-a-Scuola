{
    'name' : 'modulo_scuola',
    'version' : '1.0',
    'summary': 'Modulo per la scuola',
    'sequence': 15,
    'category': 'Extra Tools',
    'author': 'Redon Copa & Antonio Vangi',
    'website': 'https://www.odoo.com/',
    'depends' : ['hr', 'report', 'barcodes'],
    'license' :'AGPL-3',
    'demo': [],
    'data': [
         'security/ir.model.access.csv',
         'views/alunno.xml',
         'views/voti.xml',
         'views/classe.xml',
         'viewshr_presenze_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
