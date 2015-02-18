class Country:

    def __init__(self, name):
        self.name=name

    def __str__(self):
        return 'Hello from ' + self.name 

def main():
    Ned=Country("Nederland")
    Ger=Country("Germany")
    print(Ned)
    print(Ger)
    

if __name__ == "__main__":
	main()

