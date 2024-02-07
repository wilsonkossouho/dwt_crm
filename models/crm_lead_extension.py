# Odoo Models

from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    date_et_heure_de_depot = fields.Datetime(string='Date et heure de dépôt')
    reference_sigmap = fields.Char(string='Référence SIGMAP')
    garantie_soumission = fields.Integer(string='Garantie de soumission (FCFA)')
    duree_validite = fields.Integer(string='Durée de validité (Jours)')
    capacite_financiere = fields.Integer(string='Capacité financière (FCFA)')
    groupement = fields.Integer(string='Groupement')
    autorisation_fabricant = fields.Selection([('oui', 'Oui'), ('non', 'Non')],string='Autorisation de fabricant')
    source_financement = fields.Selection(
        [
            ('Fonds propres','Fonds propres'),
            ('Budjet national','Budjet national'),
            ('Budjet autonome', 'Budjet autonome'),
            ('Banque Mondiale', 'Banque Mondiale'),
            ('Afd', 'Afd'),
            ('KFW','KFW'),
            ('BAD', 'BAD')
        ],
        string='Source de financement')
    lot = fields.Selection([
        ('Unique','Uniques'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    ],string='Lot')
    numeros_avis = fields.Char(string='N° de l\'avis')
    date_notification = fields.Date(string="Date de Notification")