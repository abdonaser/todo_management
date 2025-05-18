from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date, timedelta

class ToDoTask(models.Model):
    _name = 'todo.task'
    _description = 'Todo Task Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # ───────────────────
    # BASIC  F I E L D S
    # ───────────────────
    task_name = fields.Char(
        string="Task Name",
        required=True ,
        tracking=True,
        copy=False # duplicating a task forces a new name
        )

    assign_to = fields.Many2one(
        'res.partner',
        string="Assigned To" ,
        tracking=True , 
        required=True,
        domain="[('is_company','=',False)]"     # only people, not companies
        )
    
    photo = fields.Binary(
        related='assign_to.image_1920',
        string="Assignee Image",
        store=True,
        readonly=True,
        tracking=True
        )
    
    email = fields.Char(
        related='assign_to.email',
        string="Assignee e‑mail",
        store=True,
        readonly=True,
        tracking=True
        )

    description = fields.Text(string="Description" ,tracking=True )

    due_date = fields.Date(
        string="Due Date" ,
        tracking=True ,
        required=True,
        help="Deadline for completing the task."
        )

    status = fields.Selection(
        [
            ("new","New"),
            ("in_progress","In Progress"),
            ("completed","Completed"),
        ],
        string="Status",
        default='new',
        required=True,
        tracking=True
    )

# ───────────────────
# C O N S T R A I N T S
# ───────────────────

    # ─── SQL CONSTRAINTS ─────────────────────────────────────────────────────────
  
    # one partner can’t have two tasks with the same name.
    _sql_constraints = [
        (
            "unique_name_per_partner",
            "unique(task_name, assign_to)",
            "This assignee already has a task with that name.",
        ),
    ]

    # ─── PYTHON CONSTRAINTS ──────────────────────────────────────────────────────
 
    @api.constrains('due_date')
    def _check_due_date(self):
        for rec in self:
            if rec.due_date and rec.due_date < date.today():
                raise ValidationError(_("Due date cannot be in the past."))
    
    @api.constrains("assign_to")
    def _check_email(self):
        for rec in self:
            if not rec.assign_to.email:
                raise ValidationError(_("The selected assignee must have an e‑mail address."))

# ───────────────────
# O N C H A N G E S
# ───────────────────
    
    @api.onchange('task_name')
    def _onchange_task_name(self):
        for rec in self:
            if not rec.due_date: 
                rec.due_date = date.today() + timedelta(days=7)

# ───────────────────
# B U S I N E S S  H E L P E R S
# ───────────────────

    # ─── QUICK ACTIONS FOR BUTTONS ───────────────────────────────────────────────
    def action_set_in_progress(self):
        self.write({"status": "in_progress"})

    def action_set_completed(self):
        self.write({"status": "completed"})