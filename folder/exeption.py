class Custom_Excep(Exception):
    def __str__(self):
        return "The group should not exceed 10 students or such a student has already been added to the group"