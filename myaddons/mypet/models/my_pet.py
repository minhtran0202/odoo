# -*- coding: utf-8 -*-
from itertools import product
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class MyPet(models.Model):
    _name = "my.pet"
    _description = "My pet model"

    name = fields.Char('Pet Name', required=True)
    nickname = fields.Char('Nickname')
    description = fields.Text('Pet Description',compute= '_btn_test',store="True")
    age = fields.Integer('Pet Age', default=1, )
    weight = fields.Float('Weight (kg)')
    dob = fields.Datetime('DOB', required=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', default='male')
    pet_image = fields.Binary("Pet Image", attachment=True, help="Pet Image")    
    toy = fields.Char('Pet Toy', required=False)
    basic_price = fields.Float('Basic Price', default=0)
    owner_id = fields.Many2one('res.partner', string='Owner')
    is_private = fields.Boolean(string='Is Private', groups='mypet.my_pet_group_admin', default=False)
    product_ids = fields.Many2many(comodel_name='product.pet', 
                                string="Related Products", 
                                relation='pet_product_rel',
                                column1='col_pet_id',
                                column2='col_product_id')

    
    @api.model
    def create(self, vals):
        print(">>>>>>>>>>>>>>>>>>>>>>.",self.search([]))
        return super(MyPet, self).create(vals)

    @api.model
    def btn_multi_update(self):
        # we can do something on records... it's up to you!
        # res = { 'type': 'ir.actions.client', 'tag': 'reload' } # reload the current page/url
        active_ids = [pet.id for pet in self.env["my.pet"].search([])]
        print("-------------------------------------------------------------------------------")
        print(active_ids)
        res = {            
            "name": _("Multi Update"),
            "type": "ir.actions.act_window",
            "res_model": "my.pet",
            "binding_model_id": self.env['ir.model']._get("my.pet").id,
            "view_mode": "form",
            "target": "new",
            "views": [[False, 'form']],
            "context": {
                "active_ids": active_ids,
                "default_dob": fields.Date.context_today(self),
                "default_owner_id": self.env.user.partner_id.id,
            },
        }
        return res

        
    def custom_remove(self,):
        print(1)

    @api.depends('name','gender')
    def _btn_test(self):
        print("------------------------------------------------------------------------")
        print(self.env)
        print(self.env.context)
        for record in self:
            if record.gender=="male":
                record.description = 'male'
            else:
                record.description = 'female'
    
    @api.onchange('nickname')
    def _test_onchange(self):
        print("--------------------------------------------------------------------------------------")
        print(self)
        for record in self:
            if record.nickname == "minh":
                record.name = "min"

    def test_create(self,):
        product_pet_list = self.env['product.pet'].search([])
        print("----------",product_pet_list)
        val={'product_ids':[(4,9)]}
        # self.env['my.pet'].create(val)
        for pet in self:
            pet.write(val)

class SuperPet(models.Model):
    _name = "super.pet" # <- new model name
    _inherit = "my.pet" # <- inherit fields and methods from model "my.pet"
    _description = "Prototype inheritance"

    # add new field
    is_super_strength = fields.Boolean("Is Super Strength", default=False)
    is_fly = fields.Boolean("Is Super Strength", default=False)
    planet = fields.Char("Planet")
    
    # avoid error: TypeError: Many2many fields super.pet.product_ids and my.pet.product_ids use the same table and columns
    product_ids = fields.Many2many(comodel_name='product.product', 
                                string="Related Products", 
                                relation='super_pet_product_rel', # <- change this relation name!
                                column1='col_pet_id',
                                column2='col_product_id')