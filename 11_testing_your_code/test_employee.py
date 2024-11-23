from employee import Employee

def test_give_default_raise():
    person = Employee("James", "Sunderland", 0)
    person.give_raise()
    assert person.salary == 5000

def test_give_custom_raise():
    person = Employee("James", "Sunderland", 100)
    person.give_raise(5400)
    assert person.salary == 5500