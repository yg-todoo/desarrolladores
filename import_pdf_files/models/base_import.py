# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import urllib2
import base64
from odoo import api, fields, models,_


class CustomImport(models.TransientModel):

    _inherit = 'base_import.import'

    @api.model
    def _parse_import_data(self, data, import_fields, options):
        # Get fields of type date/datetime
        data = super(CustomImport, self)._parse_import_data(
            data, import_fields, options)
        all_fields = self.env[self.res_model].fields_get()
        for import_field in import_fields:
            if import_field.find('/') != -1:
                data = self._parse_indepth(
                    all_fields, import_fields, import_field, data)
            elif import_field in all_fields.keys():
                if all_fields[import_field]['type'] in ('binary'):
                    index = import_fields.index(import_field)
                    for num, line in enumerate(data):
                        if line[index][:4] == 'http':
                            line[index] = self._get_binary_image(line[index])
                        else:
                            line[index] = line[index]
        return data

    def _parse_indepth(self, all_fields, import_fields, import_field, data):
        if import_field.split('/')[0] in all_fields.keys():
            name = import_field.split('/')[0]
            field = self.env[all_fields[name]['relation']
                             ].fields_get()[import_field.split('/')[1]]
            index = import_fields.index(import_field)
            if field['type'] in ('binary'):
                for num, line in enumerate(data):
                    if line[index][:4] == 'http':
                        line[index] = self._get_binary_image(line[index])
                    else:
                        line[index] = line[index]
            return data

    def _get_binary_image(self, image_data):
        url = image_data.encode('utf8').strip()
        url = str(url).replace("\\", '')
        try:
            if url != '':
                request = urllib2.Request(url, headers={'User-Agent': "odoo"})
                binary = urllib2.urlopen(request)
            else:
                return
        except urllib2.HTTPError as err:
            if err.code == 404:
                # the image is just missing, we skip it
                return
            else:
                # we don't know why we couldn't download the image
                # so we propagate the error, the import will fail
                # and we have to check why it couldn't be accessed
                raise
        else:
            return base64.b64encode(binary.read())
