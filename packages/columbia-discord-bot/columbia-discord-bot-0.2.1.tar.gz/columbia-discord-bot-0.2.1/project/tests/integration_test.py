from project import student


def test():
    print('running tests')
    users = {}
    s = student.Student('student1', 'uni1')
    s1 = student.Student('student2', 'uni2')
    s2 = student.Student('student3', 'uni3')

    users['student1'] = s
    users['student2'] = s1
    users['student3'] = s2

    s.add_class('test-class-1')
    assert s.get_classes() == ['test-class-1']
    s.add_class('test-class-2')
    assert s.get_classes() == ['test-class-1', 'test-class-2']

    s1.add_class('test-class-1')
    assert s.look_up_class('test-class-1', users) == [s.uni, s1.uni]

    s.add_prof('test-prof-1')
    assert s.get_profs() == ['test-prof-1']
    s.add_prof('test-prof-2')
    assert s.get_profs() == ['test-prof-1', 'test-prof-2']

    s2.add_prof('test-prof-1')
    assert s.look_up_prof('test-prof-1', users) == [s.uni, s2.uni]

    s.remove_class('test-class-1')
    assert s.get_classes() == ['test-class-2']
    s.remove_class('test-class-2')
    assert s.get_classes() == []

    s.remove_prof('test-prof-2')
    assert s.get_profs() == ['test-prof-1']
    s.remove_prof('test-prof-1')
    assert s.get_profs() == []

    s.set_uni('changed-username')
    assert s.uni == 'changed-username'
