from odoo import models, fields, api, _

class scuola_alunno(models.Model):
    _name= 'scuola.alunno'
    _description= 'Alunno Record'

    nome_alunno= fields.Char(string='Nome', required= True)
    cognome_alunno= fields.Char(string='Cognome', required= True)
    anni_alunno= fields.Char(string='Anni', required= True)
    note_alunno= fields.Text(string='Note')
    foto_alunno= fields.Binary(string='Foto alunno')
    assenze_alunno= fields.One2many('scuola.assenze','as_alunno_id', string='Assenza')
    voti_alunno= fields.One2many('scuola.voti','alunno_id', string='Voti')
    classe_alunno= fields.Many2one('scuola.classi', string='Classe')

    @api.multi
    def name_get(self):
        risultato=[]
        for alunno in self:
            nome= alunno.nome_alunno + ' ' + alunno.cognome_alunno  + ' ' + str(alunno.id)
            risultato.append((alunno.id, nome))
        return risultato


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


