def show_menu():
	print('\n--- TODOアプリ ---')
	print('1. タスクを追加')
	print('2. タスクを表示')
	print('3. タスクを削除')
	print('4. 終了')


def add_task(tasks):
	task = input('タスクを入力してください: ')
	tasks.append(task)
	print('--> 追加しました！')


def show_tasks(tasks):
	if not tasks:
		print('タスクはありません。')
	else:
		print('▼ タスクリスト▼ ')
		for i, task in enumerate(tasks, start=1):
			print(f'{i}. {task}')


def delete_task(tasks):
	show_tasks(tasks)
	try:
		num = int(input('削除するタスク番号を入力してください: '))
	if 1 <= num <= len(tasks):
			removed = tasks.pop(num - 1)
			print(f'--> 「{removed}を削除しました。')
		else:
			print('番号が無効です。')
	except ValueError:
		print('数字を入力してください。')


def main():
	tasks = []
	while True:
		show_menu()
		choice = input('番号を選んでください:')


		if choice == "1":
			add_task(tasks)
		elif choice == "2":
			show_tasks(tasks)
		elif choice == "3":
			delete_task(tasks)
		elif choice == "4":
			print('終了します。')
			break
		else:
			print('1~4の番号を選んでください。')


if __name__ == "__main__":
	main()
