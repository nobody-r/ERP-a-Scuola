from odoo import models, fields, api, _

class scuola_classi(models.Model):
    _name= 'scuola.classi'
    _description= 'Classi Record'

    classe_id= fields.one2Many('scuola.alunno','classe_alunno')
    nome_classe= fields.Char('Nome classe')
