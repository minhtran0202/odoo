import odoo
import logging
import json
from odoo import http
from odoo.http import request
_logger = logging.getLogger(__name__)

class MyPetAPI(odoo.http.Controller):
    

    @odoo.http.route('/test1', type='http', auth='none')
    def pet(self):
        pets = request.env['my.pet'].sudo().search([])
        html_result = '<html><body><ul>'
        for pet in pets:
            html_result += "<li> %s </li>" % pet.name
        html_result += '</ul></body></html>'
        return html_result

    @http.route('/test2', type='json', auth='none')
    def courses_json(self):
        courses = request.env['my.pet'].sudo().search([])
        return courses.read(['name'])

    @http.route('/test3', type='http', auth='public')
    def all_courses_mark(self):
        courses = request.env['my.pet'].sudo().search([])
        html_result = '<html><body><ul>'
        for course in courses:
            if request.env.user.id == course.create_uid.id:
                html_result += "<li> <b>%s</b> </li>" % request.env.user.id
            else:
                html_result += "<li> %s </li>" % request.env.user.id
        html_result += '</ul></body></html>'
        return html_result


    @http.route('/test5', type='http', auth='none')
    def course_details(self, id):
        record = request.env['my.pet'].sudo().browse(int(id))
        html_result = '<html><body>'
        html_result += '<h1> %s </h1>' %record.name
        html_result += '<h1>%s</h1>' %record.description
        html_result += '</body></html>'

        return html_result

    @http.route("/test5/<id>", type='http', auth='none')
    def course_details_in_path(self, id):
        print("--------------------------------------------",id)
        return self.course_details(id)