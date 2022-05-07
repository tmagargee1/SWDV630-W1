class Teams:
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)
    
    def __contains__(self, member):
        return member in self.__myTeam
    
    def __iter__(self):
        return iter(self.__myTeam)



def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    
    print ('It is', 'Tim' in classmates, 'that Tim is in the list')
    print ('It is', 'Sam' in classmates, 'that Sam is in the list')

    print('The students in the class are:', end=" ")
    for i in classmates:
        print(i, end=" ")

    print (len(classmates))

main()
