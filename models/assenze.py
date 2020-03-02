from odoo import models, fields, api, _

class scuola_assenze(models.Model):
    _name= 'scuola.assenze'
    _description= 'Assenze Record'

    as_alunno_id = fields.Many2one('scuola.alunno', string="Data")
    assenza_data = fields.Date(string='Data', required=True)
    assenza_giustificata= fields.Selection([
        ('ingiustificata', 'Ingiustificata'),
        ('Giustificata', 'Giustificata'),
    ], default='ingiustificata', string 'Assenza')
