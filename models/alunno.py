from odoo import models, fields, api, _

class scuola_alunno(models.Model):
    _name= 'scuola.alunno'
    _description= 'Alunno Record'
    _rec_name= 'combination'


    nome_alunno= fields.Char(string='Nome', required= True)
    cognome_alunno= fields.Char(string='Cognome', required= True)
    anni_alunno= fields.Char(string='Anni', required= True)
    note_alunno= fields.Text(string='Note')
    foto_alunno= fields.Binary(string='Foto alunno')
    combination = fields.Char(string='Combination', compute='fields_combination')

    @api.depends('nome_alunno', 'cognome_alunno')
    def fields_combination(self):
        for test in self:
            test.combination = nome_alunno + ' ' + cognome_alunno

    @api.multi
    def alunno_voti(self):
        return {
            'name': _('votes'),
            'domain': [('alunno_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'scuola.voti',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
