from lesson20.class_test.code_for_esting import Human

class TestHuman:
    def setup_class(self):
        print('\nwere in setup class section')
        self.human = Human('Joshua', 50, 'Pink')

    def setup(self):
        print('\nwere in setup section')

    def test_check_growth(self):
        self.human
        self.human.grow()
        assert self.human.age == 51


    def test_change_hair_color(self):
        human = Human('Joshua', 50, 'Pink')
        human.change_hair_color('Blonde')
        assert human.color == 'Blonde'

    def teardown(self):
        print('\nwere in teardown section')

    def teardown_class(self):
        print('\nwere in teardown class section')

