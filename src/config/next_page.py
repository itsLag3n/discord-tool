
class next_page:
    def __init__(self, page):
        self.page = page
    
    def main(self):
        if self.page in [1]:
            self.page += 1
        return self.page