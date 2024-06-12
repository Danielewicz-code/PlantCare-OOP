# Create a User
user = User("Bjorne")
print("\n-- Adding Plants --")

# Add Plants
user.add_plant("Rose", "Rosa", 1, "Healthy")
user.add_plant("Tulip", "Tulipa", 2, "Healthy")

# View Plants
print("\n-- Viewing Plants --")
user.view_plants()

# Add Growth Data
print("\n-- Adding Growth Data --")
user.plants_list[0].add_growth("2024-06-12", 25, 10)
user.plants_list[1].add_growth("2024-06-13", 30, 15)

# Set Water and Sunlight Requirements
print("\n-- Setting Water and Sunlight Requirements --")
user.plants_list[0].set_required_water(500)
user.plants_list[0].set_required_sunlight(6)
user.plants_list[1].set_required_water(300)
user.plants_list[1].set_required_sunlight(4)

# Add Tasks
print("\n-- Adding Tasks --")
user.plants_list[0].add_tasks("Watering", 4, "2024-06-11")
user.plants_list[0].add_tasks("Fertilizing", 30, "2024-06-01")
user.plants_list[1].add_tasks("Watering", 5, "2024-06-10")

# View Plants with Tasks
print("\n-- Viewing Plants with Tasks --")
user.view_plants()

# Check for Notifications
print("\n-- Checking for Notifications --")
user.receive_notifications()

# Simulate Completing a Task
print("\n-- Completing Tasks --")
user.plants_list[0].care_tasks[0].complete_task()  
user.receive_notifications()  

# Update Task Frequency
print("\n-- Updating Task Frequency --")
user.plants_list[0].care_tasks[1].update_frequency(20)  

# Remove a Plant
print("\n-- Removing a Plant --")
user.remove_plant("Rose")
user.view_plants()  

# Plant Care System
print("\n-- Plant Care System --")
plant_care_system = PlantCareSystem()
plant_care_system.add_user("Jozef")
plant_care_system.add_user("Anna")

# View Users
print("\n-- Viewing Users --")
for user in plant_care_system.users_list:
    print(f"User: {user.username}")

# Remove a User
print("\n-- Removing a User --")
plant_care_system.remove_user("Anna")

# View Users Again
print("\n-- Viewing Users Again --")
for user in plant_care_system.users_list:
    print(f"User: {user.username}")
