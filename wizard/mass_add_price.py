# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
from openerp.tools.translate import _
import logging

_logger = logging.getLogger(__name__) # Need for message in console.



class product_mass_add_price(osv.osv_memory):
    _name = 'product.mass_add_price'
    _description = 'Mass Add Price List'

    _columns = {
        'price_version_id': fields.many2one('product.pricelist.version', 'Price List Version', required=False, select=True),
        'unit_type': fields.selection([('circulation', 'Circulation'),('units_blank', 'Blank'),], 'Unit Type', required=False,),

        }


    def add_price(self, cr, uid, ids, context=None):

         # get context or not
        context = context or {}

        #_logger.warning("Context = %s", context)
        # it id product.
        prod_id = context.get('active_id')

        # get fields from form
        res = self.read(cr, uid, ids, ['price_version_id','unit_type'], context=context)
        #convert from many record to one. get [0] level.
        res = res and res[0] or {}


        price_version_id = res['price_version_id'][0]
        # it type for circulation or blank. Determination in res.extended.
        unit_type = res['unit_type']

        try:
            # Execute the SQL command
            type_opt = unit_type
            cr.execute('select id_opt AS oid , name AS oname from res_extended where type_opt=%s order by 1', (type_opt,))
            data = cr.dictfetchall()

            rule_name2 = ''

            for rec in data:

                rule_name1 = ''

                oid = rec.get('oid')
                oname = rec.get('oname','')

                rule_name1 = oname
                rule_name = type_opt + " From %s to %s" % (rule_name1, rule_name2)
                rule_name2 = oname

                ## It can Direct make price rule in Price item
                try:
                    self.pool.get('product.pricelist.item').create(cr, uid,
                                                {
                                                'name': rule_name,
                                                'product_id': int(prod_id),
                                                'min_quantity' : int(oname),
                                                'sequence': int(oid),
                                                'price_version_id': int(price_version_id),
                                                'base': 1,
                                                'price_surcharge': 0.00,
                                                })
                except:
                     return False

        except:
            return False

        return True


product_mass_add_price()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

