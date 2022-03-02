from odoo import models, fields, api

class empresa(models.Model):
    _name = 'odoo_x.empresa'
    _description = 'model empresa'

    name = fields.Char('Nombre',required=True)

    locales_id = fields.One2many('odoo_x.locales','empresa_id',string='Locales')

class locales(models.Model):
    _name = 'odoo_x.locales'
    _description = 'model locales'

    name = fields.Char('ID',required=True)
    lugar = fields.Char(String='Lugar',required=True)

    empresa_id = fields.Many2one('odoo_x.empresa',string='Empresa')
    empleados_id = fields.One2many('odoo_x.empleados','locales_id',string='Empleados')

class empleados(models.Model):
    _name = 'odoo_x.empleados'
    _description = 'model empleados'

    name = fields.Char('Nombre',required=True)

    locales_id = fields.Many2one('odoo_x.locales',string='Locales')

class clientes(models.Model):
    _name = 'odoo_x.clientes'
    _description = 'model clientes'

    name = fields.Char('Nombre',required=True)
    numero = fields.Integer(String='Numero',required=True)

    pagos_id = fields.One2many('odoo_x.pagos','clientes_id',string='Pagos')

class pagos(models.Model):
    _name = 'odoo_x.pagos'
    _description = 'model pagos'

    name = fields.Char('ID',required=True)

    clientes_id = fields.Many2one('odoo_x.clientes',string='Clientes')
    cesta_id = fields.Many2one('odoo_x.cesta',string='Cesta')

class cesta(models.Model):
    _name = 'odoo_x.cesta'
    _description = 'model cesta'

    name = fields.Char('ID',required=True)

    ordenadores_id = fields.One2many('odoo_x.ordenadores','cesta_id',string='Ordenadores')
    ratones_id = fields.One2many('odoo_x.ratones','cesta_id',string='Ratones')
    moviles_id = fields.One2many('odoo_x.moviles','cesta_id',string='Moviles')
    cables_id = fields.One2many('odoo_x.cables','cesta_id',string='Cables')
    pagos_id = fields.One2many('odoo_x.pagos','cesta_id',string='Pagos')


class ordenadores(models.Model):
    _name = 'odoo_x.ordenadores'
    _description = 'model ordenadores'

    name = fields.Char('Nombre',required=True)
    marca = fields.Char(String='Marca',required=True)
    precio = fields.Integer(String='Precio',required=True)

    cesta_id = fields.Many2one('odoo_x.cesta',string='Cesta')

class ratones(models.Model):
    _name = 'odoo_x.ratones'
    _description = 'model ratones'

    name = fields.Char('Nombre',required=True)
    marca = fields.Char(String='Marca',required=True)
    precio = fields.Integer(String='Precio',required=True)

    cesta_id = fields.Many2one('odoo_x.cesta',string='Cesta')

class moviles(models.Model):
    _name = 'odoo_x.moviles'
    _description = 'model moviles'

    name = fields.Char('Nombre',required=True)
    marca = fields.Char(String='Marca',required=True)
    precio = fields.Integer(String='Precio',required=True)

    cesta_id = fields.Many2one('odoo_x.cesta',string='Cesta')

class cables(models.Model):
    _name = 'odoo_x.cables'
    _description = 'model cables'

    name = fields.Char('Nombre',required=True)
    tipo = fields.Char(String='Tipo',required=True)
    precio = fields.Integer(String='Precio',required=True)

    cesta_id = fields.Many2one('odoo_x.cesta',string='Cesta')
