# created_date = 'дата создания заметки в формате "день-месяц-год", например "10-11-2024": '
# issue_date = 'дата истечения заметки (дедлайн) в формате "день-месяц-год", например "10-12-2024": '
from add_input import issue_date, created_date

temp_issue_date = issue_date[:5]
temp_created_date = created_date[:5]

print(f"Дата создания заметки, {temp_created_date}")
print(f"Дата истечения заметки, {temp_issue_date}")
