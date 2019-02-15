# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale as WebsiteSaleSuper


class WebsiteSale(WebsiteSaleSuper):
    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        if category and search:
            search = None
        return super(WebsiteSale, self).shop(page, category, search, ppg, **post)
