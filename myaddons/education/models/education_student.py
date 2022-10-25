# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import RedirectWarning, UserError, ValidationError

class MyPet(models.Model):
    _name = "education.student"
    _description = "education model"


    name = fields.Char(string='Name')
    student_code = fields.Char(string='Student Code', required=True, index=True,
                           help="Student ID is unique")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                           string='Gender', default='male')    
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute = "_compute_age",store = True)
    active = fields.Boolean(string='Active', default=True)
    notes = fields.Text(string='Internal Notes')
    description = fields.Html(string='Description', sanitize=True, strip_style=False)
    attached_file = fields.Binary('Attached File', groups='base.group_user')
    total_score = fields.Float(string='Total Score')
    
    write_date = fields.Datetime(string='Last Updated on')
    currency_id = fields.Many2one('res.currency', string='Currency')
    amount_paid = fields.Monetary('Amount Paid')

    state = fields.Selection(string='Status', selection=[('new', 'New'),
                                                        ('studying', 'Studying'),
                                                        ('off', 'Off')], default='new')

    @api.depends("gender")
    def _thu_api_depends(self):
        print("-------------------------------------------------------")
        print(self.env['education.student'].search(['|', ('active', '=', False), ('active', '=', True)]))
        print(self.env['education.student'].search([]))

        for record in self:
            if record.gender:
                record.age = 10

    @api.depends('date_of_birth')
    def _compute_age(self):
        curent_year = fields.Date.today().year
        for r in self:
            if r.date_of_birth and r.date_of_birth.year < curent_year:
                r.age = curent_year - r.date_of_birth.year
            else:
                r.age = 0


    @api.model
    def is_allowed_state(self, current_state, new_state):
        allowed_states = [('new', 'studying'), ('studying', 'off'), ('off', 'studying'), ('new', 'off')]
        return (current_state, new_state) in allowed_states

    def change_student_state(self, state):
        for student in self:
            if student.is_allowed_state(student.state, state):
                student.state = state
            else:
                # raise UserError(_("khong the chuyen tu %s thanh %s") % (student.state, state))
                raise RedirectWarning(_("khong the chuyen tu %s thanh %s") % (student.state, state), "1", _('Go to the Archived Product'))

    def change_to_new(self):
        self.change_student_state('new')

    def change_to_studying(self):
        self.change_student_state('studying')

    def change_to_off(self):
        self.change_student_state('off')