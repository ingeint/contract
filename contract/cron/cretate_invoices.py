# -*- coding: utf-8 -*-
import base64
import time
from datetime import datetime, timedelta
import requests
import re
import xmlrpc.client as xc
import os
import os.path
from os import path


class CreateInvoices:
    @staticmethod
    def create_invoices():

        server = 'http://10.27.115.2:3031'
        db = "odoo14thundertest"
        user = "admin"
        password = "7f74862a8d36ad08720a4e4638d418e416aa35d9"
        import xmlrpc.client
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(server))
        uid = common.authenticate(db, user, password, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(server))
        models.execute_kw(db, uid, password, 'contract.contract', 'create_service_order', [''])


if __name__ == '__main__':
    # Connect by xml-rpc
    app = CreateInvoices
    app.create_invoices()
