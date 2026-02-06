# oop_self_identity.py

class IdentityTest:
    def show_self_id(self):
        print(f"id(self):     {id(self)}")

# Instance creation
test_instance = IdentityTest()

# Comparison
print(f"id(instance): {id(test_instance)}")
test_instance.show_self_id()
