from odoo import models, fields

class scuola_voti(models.Model):
    _name= 'scuola.voti'
    _description= 'Voti Record'

    voto_alunno = fields.Float(digits=(2,2), string='Voto', required= True)
    voto_materia = fields.Char(string='Materia', required= True)
    voto_data = fields.Date(string='Data voto', required= True)
    alunno_id = fields.Many2one('scuola.alunno', string="Alunni")




