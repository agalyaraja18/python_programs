try:
    import non_existent_module as my_module
    print("Module imported successfully!")
except ModuleNotFoundError:
    print("Module not found. Using fallback implementation.")
    class FallbackModule:
        @staticmethod
        def greet(name):
            return f"Hello, {name}! (from fallback)"
    my_module = FallbackModule()

print(my_module.greet("Alice"))