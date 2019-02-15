# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteSaleClearSearch(http.Controller):
#     @http.route('/website_sale_clear_search/website_sale_clear_search/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_sale_clear_search/website_sale_clear_search/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_sale_clear_search.listing', {
#             'root': '/website_sale_clear_search/website_sale_clear_search',
#             'objects': http.request.env['website_sale_clear_search.website_sale_clear_search'].search([]),
#         })

#     @http.route('/website_sale_clear_search/website_sale_clear_search/objects/<model("website_sale_clear_search.website_sale_clear_search"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_sale_clear_search.object', {
#             'object': obj
#         })