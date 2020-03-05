from odoo import models, fields, api, exceptions, _

class scuola_presenze(models.Model):
    _name= 'scuola.presenze'
    _description= 'Presenze Record'

    alunno_id = fields.Many2one('scuola.alunno', string="Alunno", required=True, ondelete='cascade', index=True)
    classe_id = fields.Many2one('scuola.classi', string="Classi", readonly=True)
    check_in = fields.Datetime(string="Check In", default=fields.Datetime.now, required=True)
    check_out = fields.Datetime(string="Check Out")
    
    worked_hours = fields.Float(string='Worked Hours', compute='_compute_worked_hours', store=True, readonly=True)
   
   @api.multi
    def name_get(self):
        result = []
        for presenza in self:
            if not presenza.check_out:
                result.append((presenza.id, _("%(alunno_name)s from %(check_in)s") % {
                    'alunno_name': presenza.alunno_id.nome_alunno,
                    'check_in': fields.Datetime.to_string(fields.Datetime.context_timestamp(presenza, fields.Datetime.from_string(presenza.check_in))),
                }))
            else:
                result.append((presenza.id, _("%(alunno_name)s da %(check_in)s fino %(check_out)s") % {
                    'alunno_name': presenza.alunno_id.nome_alunno,
                    'check_in': fields.Datetime.to_string(fields.Datetime.context_timestamp(presenza, fields.Datetime.from_string(presenza.check_in))),
                    'check_out': fields.Datetime.to_string(fields.Datetime.context_timestamp(presenza, fields.Datetime.from_string(presenza.check_out))),
                }))
        return result
   
   
    @api.depends('check_in', 'check_out')
    def _compute_worked_hours(self):
        for presenza in self:
            if presenza.check_out:
                delta = presenza.check_out - presenza.check_in
                presenza.worked_hours = delta.total_seconds() / 3600.0
    
    @api.constrains('check_in', 'check_out')
    def _check_validity_check_in_check_out(self):
        """ verifica la coerenza dell ora di ingresso rispetto a quella di uscita. """
        for presenza in self:
            if presenza.check_in and presenza.check_out:
                if presenza.check_out < presenza.check_in:
                    raise exceptions.ValidationError(_('"Chek Out" non può essere precedente "Check In".'))
                    
                    
    @api.constrains('check_in', 'check_out', 'alunno_id')
    def _check_validity(self):
        """ Verifies the validity of the attendance record compared to the others from the same employee.
            For the same employee we must have :
                * maximum 1 "open" attendance record (without check_out)
                * no overlapping time slices with previous employee records
        """
        for presenza in self:
            # we take the latest attendance before our check_in time and check it doesn't overlap with ours
            last_presenza_before_check_in = self.env['scuola.presenze'].search([
                ('alunno_id', '=', presenza.alunno_id.id),
                ('check_in', '<=', presenza.check_in),
                ('id', '!=', presenza.id),
            ], order='check_in desc', limit=1)
            if last_presenza_before_check_in and last_presenza_before_check_in.check_out and last_presenza_before_check_in.check_out > presenza.check_in:
                raise exceptions.ValidationError(_("Non puoi creare una presenza per %(alunno_name)s, l alunno risulta gia checked in alle %(datetime)s") % {
                    'alunno_name': presenza.alunno_id.nome_alunno,
                    'datetime': fields.Datetime.to_string(fields.Datetime.context_timestamp(self, fields.Datetime.from_string(presenza.check_in))),
                })

            if not attendance.check_out:
                # if our attendance is "open" (no check_out), we verify there is no other "open" attendance
                no_check_out_presenza = self.env['scuola.presenza'].search([
                    ('alunno_id', '=', presenza.alunno_id.id),
                    ('check_out', '=', False),
                    ('id', '!=', presenza.id),
                ], order='check_in desc', limit=1)
                if no_check_out_presenza:
                    raise exceptions.ValidationError(_("Cannot create new attendance record for %(alunno_name)s, the employee hasn't checked out since %(datetime)s") % {
                        'alunno_name': presenza.alunno_id.nome_alunno,
                        'datetime': fields.Datetime.to_string(fields.Datetime.context_timestamp(self, fields.Datetime.from_string(no_check_out_presenza.check_in))),
                    })
            else:
                # we verify that the latest attendance with check_in time before our check_out time
                # is the same as the one before our check_in time computed before, otherwise it overlaps
                last_presenza_before_check_out = self.env['scuola.presenza'].search([
                    ('alunno_id', '=', presenza.alunno_id.id),
                    ('check_in', '<', presenza.check_out),
                    ('id', '!=', presenza.id),
                ], order='check_in desc', limit=1)
                if last_presenza_before_check_out and last_presenza_before_check_in != last_presenza_before_check_out:
                    raise exceptions.ValidationError(_("Cannot create new attendance record for %(empl_name)s, the employee was already checked in on %(datetime)s") % {
                        'empl_name': attendance.employee_id.name,
                        'datetime': fields.Datetime.to_string(fields.Datetime.context_timestamp(self, fields.Datetime.from_string(last_presenza_before_check_out.check_in))),
                    })

    @api.multi
    @api.returns('self', lambda value: value.id)
    def copy(self):
        raise exceptions.UserError(_('You cannot duplicate an attendance.'))
