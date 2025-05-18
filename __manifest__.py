{
    'name' : "odoo management",
    'author' : "Abdelrahman Naser",
    'category' : "To Do",
    'version' : "17.0.0.1.0",
    'depends' : [
        'base','mail','contacts'],
    'data':[
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/toDoTask_view.xml',
        'views/res_partner_view.xml',

    ],
    'assets': {
        'web.assets_backend': [
            'todo_management/static/src/css/todo.css',
        ]
    },
    'application':True,
}