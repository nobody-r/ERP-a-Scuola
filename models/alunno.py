from odoo import models, fields, api

class scuola_alunno(models.Model):
    _name= 'scuola.alunno'
    _description= 'Alunno Record'
    nome_alunno= fields.Char(string='Nome', required= True)
    cognome_alunno= fields.Char(string='Cognome', required= True)
    anni_alunno= fields.Char(string='Anni', required= True)
    note_alunno= fields.Text(string='Note')
    foto_alunno= fields.Binary(string='Foto alunno')
    classe_alunno= fields.one2one('alunno.classe',string='Classe alunno')

    @api.multi
    def alunno_voti(self):
        return {
            'name': ('votes'),
            'domain': [('alunno_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'scuola.voti',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
