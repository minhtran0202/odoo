from odoo import fields, models

class EducationClass(models.Model):
   _name = 'education.class'
   _description = 'Education Class'

   name = fields.Char(string='Name', required=True)
   # ... (some fields)

   #  relational fields
   school_id = fields.Many2one('education.school', string='School', required=True)