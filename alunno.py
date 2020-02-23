from odoo import models, fields

class scuola_alunno(models.Model):
    _name= 'scuola.alunno'
    _description= 'Alunno Record'

    nome_alunno= fields.Char(string='Nome', required= True)
    cognome_alunno= fields.Char(string='Cognome', required= True)
    anni_alunno= fields.Char(string='Anni', required= True)
    note_alunno= fields.Text(string='Note')
    foto_alunno= fields.Binary(string='Foto alunno')