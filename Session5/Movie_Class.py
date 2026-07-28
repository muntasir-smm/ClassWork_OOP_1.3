'''
Write Python programs for creating following classes and their objects:

11. Movie Class

'''

class Movie:
    def __init__(self,name,Type,Ratings):
        self.name=name
        self.Type=Type
        self.Ratings=Ratings

def main():
    cinema1=Movie("The Messege","Religious","10/10")
    print(f"Name:{cinema1.name}\nType:{cinema1.Type}\nRatings: {cinema1.Ratings}")
main()
