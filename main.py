import os
class TaskTracker():
    def __init__(self):
        self.all_tasks = []
        if os.path.isfile("tasks.txt"):
            with open("tasks.txt", "r") as file:
                for s in file.readlines():
                    f = s.split(sep=":")
                    self.add_task(f[0], f[1])
        else:
            self.all_tasks = []

    def add_task(self, name, deadline):
        task = Task(name, deadline)
        id = 0
        for t in self.all_tasks:
            if t.id >= id:
                id = t.id
        task.id = id+1

        if not task in self.all_tasks:
            self.all_tasks.append(task)
        else:
            print("Задача уже существует!")


    def show_tasks(self):
        for t in self.all_tasks:
            print(t)


    def del_task(self):
        number = input("Введите номер задачи, которую нужно удалить:")
        i = int(number)
        for n,t in enumerate(self.all_tasks):
            if i == t.id:
                del self.all_tasks[n]
                break
            else :
                raise ValueError("Задачи с таким номером не существует!")
        return number

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for t in self.all_tasks:
                file.write(t.name + ":" + t.deadline + "\n")






class Task():
    def __init__(self, name, deadline):

        self.id = 0
        if isinstance(name, str):
            self.name = name

        else:
            raise TypeError("Имя должно быть строкой !")
        if isinstance(deadline, str):  #возможно нужно сделать тип datetime
            self.deadline = deadline
        else:
            raise TypeError("Срок должен быть строкой !")

    def __str__(self):
        return f"{self.name}     дедлайн: {self.deadline}     номер:{self.id}"















def main():
    task_tracker = TaskTracker()
    # user = input("Введите номер пользователя:")
    # if user == "1":
    #     task_traker1 = TaskTracker()
    # elif user == "2":
    #     task_tracker2 = TaskTracker()
    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Изменить статус задачи")  #выполнено/не выполнено/в процессе
        print("4. Посмотреть все задачи")
        print("5. Посмотреть статус задач")
        print("6. Посмотреть срок выполнения задач")
        print("7. Завершить работу")



        choice = input("Выберите действие: ")

        if choice == "1":
            print("Добавление задачи...")
            name = input("Введите имя задачи:")
            deadline = input("Введите срок выполнения задачи:")
            task_tracker.add_task(name, deadline)

        elif choice == "2":
            print("Удаление задачи")
            task_tracker.del_task()
            print(f"Вы удалили задачу под номером {task_tracker.de}")
        elif choice == "3":
            print("Изменение статуса задачи")

        elif choice == "4":
            print("Вывод всех задач...")
            task_tracker.show_tasks()

        elif choice == "5":
            print("Вывод статуса задач")

        elif choice == "6":
            print("Вывод сроков выполнения задач")

        elif choice == "7":
            print("Завершение работы")
            task_tracker.save_tasks()
            break


if __name__ == "__main__":
    main()
