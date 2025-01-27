created_date = input('Введите дату создания заметки в формате "день-месяц-год", например "10-11-2024": ')
issue_date = input('Введите дату истечения заметки (дедлайн) в формате "день-месяц-год", например "10-12-2024": ')
temp_issue_date = issue_date[:5]
temp_created_date = created_date[:5]

print(f"Дата создания заметки, {temp_created_date}")
print(f"Дата истечения заметки, {temp_issue_date}")
