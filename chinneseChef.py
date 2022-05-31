from chef import Chef


# inheritance
class ChinneseChef(Chef):
    # overiding the original method
    def make_special_dish(self):
        print("the chef makes orange chicken")

    def make_fried_rice(self):
        print("the chef makes fried rice")
