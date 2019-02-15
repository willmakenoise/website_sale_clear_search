# -*- coding: utf-8 -*-
import logging
import werkzeug.utils
from odoo import http, models
from odoo.addons.http_routing.models.ir_http import slug
# from odoo.addons.website_sale.controllers.main import QueryURL as QueryURLSuper
from odoo.addons.website_sale.controllers import main as website_controller
from odoo.addons.website_sale.controllers.main import WebsiteSale as WebsiteSaleSuper
from odoo.tools import OrderedSet

_logger = logging.getLogger(__name__)


class WebsiteSale(WebsiteSaleSuper):
    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        if category and search:
            category = None
        return super(WebsiteSale, self).shop(page, category, search, ppg, **post)


class QueryURL(object):
    def __init__(self, path='', path_args=None, **args):
        self.path = path
        self.args = args
        self.path_args = OrderedSet(path_args or [])

    def __call__(self, path=None, path_args=None, **kw):
        path = path or self.path
        category = path.startswith('/shop/category/')
        for key, value in self.args.items():
            if category and key == 'search':
                continue
            kw.setdefault(key, value)
        path_args = OrderedSet(path_args or []) | self.path_args
        paths, fragments = {}, []
        for key, value in kw.items():
            if value and key in path_args:
                if isinstance(value, models.BaseModel):
                    paths[key] = slug(value)
                else:
                    paths[key] = u"%s" % value
            elif value:
                if isinstance(value, list) or isinstance(value, set):
                    fragments.append(werkzeug.url_encode([(key, item) for item in value]))
                else:
                    fragments.append(werkzeug.url_encode([(key, value)]))
        for key in path_args:
            value = paths.get(key)
            if value is not None:
                path += '/' + key + '/' + value
        if fragments:
            path += '?' + '&'.join(fragments)
        return path


website_controller.QueryURL = QueryURL
