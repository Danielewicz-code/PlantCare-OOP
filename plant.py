from datetime import datetime, timedelta

class Plant:
    def __init__(self, name, species, age, health_status) -> None:
        self.name = name
        self.species = species
        self.age = age
        self.health_status = health_status
        self.required_water = 0
        self.required_sunlight = 0
        self.growth_history = []
        self.care_tasks = []
        

    def add_growth(self, date, height, num_of_leaves):
        par = {
            "Date":date,
            "Height":height,
            "Number of leaves":num_of_leaves
        }
        self.growth_history.append(par)
        print(f"New growth data added to {self.name}.")

    def update_health_status(self, new_health_status):
        self.health_status = new_health_status
        print("Health status has been updated.")

    def set_required_water(self, new_required_water):
        self.required_water = new_required_water
        print(f"{self.name} now requires {self.required_water} ml of water per day.")

    def set_required_sunlight(self, new_sun_hours):
        self.required_sunlight = new_sun_hours
        print(f"{self.name} now requires {self.required_sunlight} hours of sunlight per day.")

    def add_tasks(self, task_name, frequency, last_completed):
        task = CareTask(task_name, frequency, last_completed)
        self.care_tasks.append(task)
        print(f"Task was added to {self.name}")

    def get_due_task(self):
        due_tasks = []
        for task in self.care_tasks:
            if task.get_next_due_date() <= datetime.now().strftime('%Y-%m-%d'):
                due_tasks.append(task)
        return due_tasks


class CareTask:
    def __init__(self, task_name, frequency, last_completed) -> None:
        self.task_name = task_name
        self.frequency = frequency
        self.last_completed = datetime.strptime(last_completed, '%Y-%m-%d')
        self.next_due = self.calculate_next_due_day()

    def calculate_next_due_day(self):
        return self.last_completed + timedelta(days=self.frequency)
    
    def complete_task(self):
        self.last_completed = datetime.now()
        self.next_due = self.calculate_next_due_day()
        print(f"{self.task_name} has been completed, next is due for {self.next_due.strftime('%Y-%m-%d')}")

    def update_frequency(self, new_frequency):
        self.frequency = new_frequency
        self.next_due = self.calculate_next_due_day()
        print(f"New frequency for the task {self.task_name}, next new date is on {self.next_due.strftime('%Y-%m-%d')}.")

    def get_next_due_date(self):
        return self.next_due.strftime('%Y-%m-%d')
    
class User:
    def __init__(self, username) -> None:
        self.username = username 
        self.plants_list = []

    def add_plant(self, name, species, age, health_status):
        plant = Plant(name, species, age, health_status)
        self.plants_list.append(plant)
        print(f"Plant: {name} has been added to the plant list.")

    def remove_plant(self, key):
        plant_to_remove = None
        for plant in self.plants_list:
            if plant.name == key:
                plant_to_remove = plant
                break

        if plant_to_remove:
            self.plants_list.remove(plant_to_remove)
            print(f"{key} has been removed from the plant list.")
        else:
            raise ValueError(f"key: {key} not found.")
        
    def view_plants(self):
        for i, plant in enumerate(self.plants_list):
            print(f"Index: {i}")
            print(f"Plant: {plant.name}, {plant.species}, {plant.age}, {plant.health_status}")

    def receive_notifications(self):
        notifications = []
        for plant in self.plants_list:
            due_tasks = plant.get_due_task()
            for task in due_tasks:
                notifications.append(f"Task: {task.task_name} for plant {plant.name} is due on {task.get_next_due_date()}.")

        if notifications:
            for notification in notifications:
                print(notification)
        
        else:
            print("There are no notifications at the moment.")


class PlantCareSystem:
    def __init__(self) -> None:
        self.users_list = []
        

    def add_user(self, user):
        username = User(user)
        self.users_list.append(username)
        print(f"{user} was added.")

    def remove_user(self, key):
        user_holder = None
        for user in self.users_list:
            if user.username == key:
                user_holder = user
        
        if user_holder:
            self.users_list = [user for user in self.users_list if user.username != key]
            print(f"{key} was removed from.")

        else:
            raise ValueError(f"'{key}' not found.")

