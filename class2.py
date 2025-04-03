class student:
    def class_pass_fail(self):
        if self.marks >=35:
            return True
        else:
            return False

sumanta=student()
sumanta.marks=69
sumanta.language=["Bengoli","English","Hindi"]


result=sumanta.class_pass_fail()
print(result)




print(sumanta.marks)
