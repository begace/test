import example_module as em

print("This is the main script")

def main_function():
    print("This is a function in the main script")

if __name__ == "__main__":
    main_function()
    em.some_func()