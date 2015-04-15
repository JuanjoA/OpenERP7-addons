# -*- encoding: utf-8 -*-
##################################################################################
#
#    Copyright (C) 2014 MalagaTIC (<http://www.malagatic.com>)
#    info@malagatic.com
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
##################################################################################
{
    'name' : 'Facturas - agrupar por país',
    'version' : '0.1',
    'category' : 'Invoice',
    'description' : """
        Añade la posibilidad de agrupar por país en las facturas de cliente
        Patrocinado por NetBuró
    """,
    'author' : 'Juanjo Algaz, jalgaz@gmail.com',
    'website' : 'http://www.malagatic.com',
    'license' : 'AGPL-3',
    'depends' : ['base','account'],
    'init_xml' : [],
    'demo_xml' : [],
    'update_xml' : ['mod_view.xml'],
    'active': False,
    'installable': True,
}