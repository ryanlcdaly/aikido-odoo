# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models
import secrets


class Tag(models.Model):
    _name = "crm.tag"
    _description = "CRM Tag"

    def _get_default_color(self):
        return secrets.SystemRandom().randint(1, 11)

    name = fields.Char('Tag Name', required=True, translate=True)
    color = fields.Integer('Color', default=_get_default_color)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists!"),
    ]
