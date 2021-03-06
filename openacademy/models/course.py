# -*- coding: utf-8 -*-

from odoo import models, fields


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Open academy course'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.users', string='Responsible')
    session_ids = fields.One2many(string="Session", comodel_name='openacademy.session', inverse_name='course_id')

    _sql_constraints = [
        ('name_description',
         'check(name != description)',
         'The course description and the course title must be different!'),

        ('name_uniq',
         'unique(name)',
         'Name must be unique!')]

    def copy(self, default=None):
        new_name = 'Copy of ' + self.name
        default = dict(default or {}, name=new_name)
        return super(Course, self).copy(default)
