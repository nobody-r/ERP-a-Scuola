from odoo import models, fields

class alunno_classe(models.Model):
    _name = 'alunno.classe'
    _description = 'Classe Record'

    alunno_id = fields.many2one('scuola.alunno', string='Alunni')
