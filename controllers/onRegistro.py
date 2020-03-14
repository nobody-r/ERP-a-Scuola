from odoo import http
from odoo.http import request
import loggingggggg

class RegistroOnboardingController(http.Controller):
    @http.route('/ERP-a-Scuola/scuola_registro_onboarding', auth='user', type='json')
    @serialize_exception
    def scuola_registro_onboarding(self):
        company = request.env.company
        if not request.env.is_admin() or \
                company.account_invoice_onboarding_state == 'closed':
            return {}

        return {
            'html': request.env.ref('ERP-a-Scuola.scuola_registro_onboarding_panel').render({
                'company': company,
                'state': company.get_and_update_account_invoice_onboarding_state()
            })
        }

    @http.route('ERP-a-Scuola/registro_dashboard_onboarding', auth='public', type='json')
    def registro_dashboard_onboarding(self):
        company = request.env.company

        if not request.env.is_admin() or company.account_dashboard_onboarding_state == 'closed':
            return {}

        return {
            'html': request.env.ref('ERP-a-Scuola.registro_dashboard_onboarding_panel').render({
                'company': company,
                'state': company.get_and_update_account_dashboard_onboarding_state()
            })
        }
