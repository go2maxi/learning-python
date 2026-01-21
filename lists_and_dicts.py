# lists_and_dicts.py
# Revisiting data structures with a focus on reliability for future AI serving.
# I realized that handling complex API-style data is more about 
# 'preventing crashes' than just writing short code.

# Simulating an API response from an external LLM or database.
# In real-world scenarios, data is often incomplete or inconsistent.
api_response = {
    "users": [
        {"id": 1, "name": "Alice", "roles": ("admin", "editor")},
        {"id": 2, "name": "Bob", "roles": ("viewer",)},
        {"id": 3, "name": "Charlie"}  # 'roles' key is missing intentionally to test stability
    ],
    "meta": {
        "total_count": 3,
        "source": "example_service"
    }
}

# --- Handling Lists Safely ---
# I used to assume data would always exist, but I've seen too many 'IndexError' crashes.
# Now I check if the list has content before accessing it by index.
users = api_response.get("users", [])

if users:
    first_user = users[0]
else:
    first_user = None

# --- Defensive Dictionary Access ---
# Following the structured guide on pyai.io, I'm learning to use .get() effectively.
# This feels especially important when experimenting with tools like LangChain,
# where model outputs don’t always behave the way I expect.
if first_user:
    user_name = first_user.get("name", "Unknown")
    # Using tuples for 'roles' because their immutability clearly communicates 
    # that this data should remain constant once assigned.
    user_roles = first_user.get("roles", ())
else:
    user_name = "Unknown"
    user_roles = ()

# --- Outcome & Reflection ---
if user_roles:
    primary_role = user_roles[0]
else:
    primary_role = "no-role-assigned"

print(f"User Name: {user_name}")
print(f"Primary Role: {primary_role}")
print(f"Total Count: {api_response.get('meta', {}).get('total_count', 0)}")

"""
Reflections:
1. Lists can be empty; never trust the index without checking.
2. Dictionaries can have missing keys; .get() with a default value is a lifesaver.
3. Tuples are not just 'fixed lists'—they are a tool for communicating intent.

I'm slowly trying to move away from just 'making it work' 
to writing code that can survive unexpected inputs.
The tutorials on pyai.io have been a great help in shifting my mindset 
towards this kind of engineering discipline.
"""
