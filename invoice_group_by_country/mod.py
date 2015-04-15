# -*- encoding: utf-8 -*-
###########################################################################
#
#    Copyright (C) 2014 MalagaTIC (<http://www.malagatic.com>)
#
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###########################################################################


from openerp.osv import fields, osv, expression

class account_invoice(osv.osv):
    _inherit = 'account.invoice'
    _columns = {
        #'pais_id': fields.many2one('res.country', 'País'),
        'pais_id': fields.related(
            'partner_id', 
            'country_id', 
            type='many2one',
            relation='res.country',
            string='País',
            store=True)
        }
