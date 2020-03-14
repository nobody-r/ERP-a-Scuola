from odoo import http
from odoo.http import request


class RegistroOnboardingController(http.Controller):

    @http.route('/web/webclient/version_info', auth='public', type='json')
    @serialize_exception
    def scuola_registro_onboarding(self):
        """ Returns the `banner` for the account invoice onboarding panel.
            It can be empty if the user has closed it or if he doesn't have
            the permission to see it. """

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

    @http.route('/registro_dashboard_onboarding', auth='public', type='json')
    def registro_dashboard_onboarding(self):
        """ Returns the `banner` for the account dashboard onboarding panel.
            It can be empty if the user has closed it or if he doesn't have
            the permission to see it. """
        company = request.env.company

        if not request.env.is_admin() or \
                company.account_dashboard_onboarding_state == 'closed':
            return {}

        return {
            'html': request.env.ref('ERP-a-Scuola.registro_dashboard_onboarding_panel').render({
                'company': company,
                'state': company.get_and_update_account_dashboard_onboarding_state()
            })
        }
