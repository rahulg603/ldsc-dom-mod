class test(object):
    def __init__(self, store_text):
        self.text = store_text
    
    def compare_storage(self, new_text):
        return(self.__compareStorage__(True, new=new_text))

    def __compareStorage__(self, negate, new):
        return(negate & (new == self.text))

if __name__ == "__main__":
    a = test("initialized.")
    print a.compare_storage(new_text = "initialized.")