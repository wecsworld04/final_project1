class Voting:

    def __init__(self):
        pass

    def vote_menu(self):
        print('--------------------------')
        print('VOTE MENU')
        print('--------------------------')
        print('v: Vote')
        print('x: Exit')
        option = input('Option: ').lower().strip()
        while option != 'v' and option != 'x':
            option = input('Invalid (v/x): ').lower().strip()
        return option

    def candidate_menu(self):
        print('--------------------------')
        print('CANDIDATE MENU')
        print('--------------------------')
        print('1: Bianca')
        print('2: Edward')
        print('3: Felicia')
        candidate = input('Candidate: ')
        while candidate not in ('1', '2', '3'):
            candidate = input('Invalid (1/2/3): ')
        if candidate == '1':
            print('Voted Bianca')
        elif candidate == '2':
            print('Voted Edward')
        elif candidate == '3':
            print('Voted Felicia')
        return int(candidate)

    def main(self):
        bianca = 0
        edward = 0
        felicia = 0
        total = 0
        while True:
            menu = self.vote_menu()
            if menu == 'x':
                break

            candidate = self.candidate_menu()

            if candidate == 1:
                bianca += 1
            elif candidate == 2:
                edward += 1
            elif candidate == 3:
                felicia += 1

            total += 1
        print('----------------------------------------------')
        print(f'Bianca – {bianca}, Edward – {edward}, Felicia – {felicia}, Total – {total}')
        print('----------------------------------------------')


if __name__ == "__main__":
    voting = Voting()
    voting.main()