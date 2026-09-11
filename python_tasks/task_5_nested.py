# Task: Deep Dictionary Navigation
# Instructions: Extract 'year'. If any key is missing, return "Unknown".

def get_vehicle_year(data):
    # TODO: Write your logic here safely
    try:
        return data["specs"]["model_info"]["year"]
    except KeyError:
        return "Unknown"

# Test Case
vehicle = {'specs': {'model_info': {'year': 2024}}}
# Expected: 2024
print(get_vehicle_year(vehicle))
print(get_vehicle_year({}))
print(get_vehicle_year({'specs': {}}))
print(get_vehicle_year({'specs': {'model_info': {}}}))
print(get_vehicle_year({'specs': {'model_info': {'name' : 'Camry'}}}))