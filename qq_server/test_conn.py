from db.models.user import User
from db.tools import DBTool

db_tool = DBTool()
users = db_tool.get_object('select * from User where id > 1', User)

print(users)