# oop_self_identity.py

class IdentityTest:
    def show_self_id(self):
        print(f"id(self):     {id(self)}")

# Instance creation
test_instance = IdentityTest()

# Comparison
print(f"id(instance): {id(test_instance)}")
test_instance.show_self_id()


# --- Additional Experiment (2026-03-09) ---

# I was wondering if two instances created from the same class
# would share the same memory address.

instance_a = IdentityTest()
instance_b = IdentityTest()

print(f"\nid(instance_a): {id(instance_a)}")
print(f"id(instance_b): {id(instance_b)}")
print(f"instance_a is instance_b: {instance_a is instance_b}")


# Another small test: integer identity

x = 256
y = 256
print(f"\n256 is 256: {x is y}")

x2 = 257
y2 = 257
print(f"257 is 257: {x2 is y2}")