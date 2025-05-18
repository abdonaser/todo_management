from odoo import models , fields

class ToDoTask(models.Model):
    _inherit = 'res.partner'

    task_ids = fields.One2many('todo.task','assign_to' , string="Tasks")


