# -*- coding: utf-8 -*-
# Copyright 2018 Vauxoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo import fields, models
_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'
    _name = 'account.move'

    date_payment = fields.Datetime('Payment Date',)
    prioritized = fields.Boolean('Prioritized', readonly=True)


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"
    _name = 'account.move.line'

    _sql_constraints = [
        (
            'check_amount_currency_balance_sign',
            '''CHECK(
                (
                    (currency_id != company_currency_id)
                    AND
                    (
                        (debit - credit <= 0 AND amount_currency <= 0 AND move_id.state != 'posted')
                        OR
                        (debit - credit >= 0 AND amount_currency >= 0 AND move_id.state != 'posted')
                    )
                )
                OR
                (
                    currency_id = company_currency_id
                    AND
                    ROUND(debit - credit - amount_currency, 2) = 0
                    AND
                    move_id.state != 'posted'
                )
            )''',
            "The amount expressed in the secondary currency must be positive when account is debited and negative when "
            "account is credited. If the currency is the same as the one from the company, this amount must strictly "
            "be equal to the balance."
        ),
    ]
