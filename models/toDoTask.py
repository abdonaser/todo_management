from odoo import models , fields

class ToDoTask(models.Model):
    _name = 'todo.task'
    _description = 'Todo Task Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    task_name = fields.Char(string="Task Name" ,tracking=True)

    assign_to = fields.Many2one('res.partner',string="Assign To" ,tracking=True)
    email = fields.Char(related="assign_to.email",string="email" ,store=True , tracking=True)

    description = fields.Text(string="Description" ,tracking=True)

    due_date = fields.Date(string="Due Date" ,tracking=True)

    status = fields.Selection(
        [
            ("new","New"),
            ("in_progress","In Progress"),
            ("completed","Completed"),
        ],
        strin="Task Status",
        default='new',
        tracking=True
    )

