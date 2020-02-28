from odoo import models, fields

class alunno_classe(models.Model):
    _name = 'alunno.classe'
    _description = 'Classe Record'

    alunno_id = fields.One2many('scuola.alunno', string='Alunni')
