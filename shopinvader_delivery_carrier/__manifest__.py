# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com)
# Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Shopinvader Carrier",
    "summary": "Carrier integration for Shopinvader",
    "version": "10.0.1.0.1",
    "category": "e-commerce",
    "website": "https://akretion.com",
    "author": "Akretion",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "external_dependencies": {"python": [], "bin": []},
    "depends": ["shopinvader", "sale_shipping_info_helper"],
    "data": ["views/backend_view.xml"],
    "demo": [
        "demo/backend_demo.xml",
        "demo/mail_template.xml",
        "demo/shopinvader_notification.xml",
    ],
    "qweb": [],
}
