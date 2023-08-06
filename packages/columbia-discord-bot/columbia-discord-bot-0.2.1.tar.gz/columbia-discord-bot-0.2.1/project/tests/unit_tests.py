from project import student


def test_add_class():
    s = student.Student('test-username', 'test-uni')
    print('testing add class')
    s.add_class('test-class')
    assert s.get_classes() == ['test-class']
    print('done')


def test_add_prof():
    s = student.Student('test-username', 'test-uni')
    print('testing add profs')
    s.add_prof('test-prof')
    assert s.get_profs() == ['test-prof']
    print('done')


def test_remove_class():
    s = student.Student('test-username', 'test-uni')
    print('testing remove class')
    s.add_class('test-class')
    s.remove_class('test-class')
    assert s.get_classes() == []
    print('done')


def test_remove_prof():
    s = student.Student('test-username', 'test-uni')
    print('testing remove profs')
    s.add_prof('test-prof')
    s.remove_prof('test-prof')
    assert s.get_profs() == []
    print('done')


def test_set_uni():
    s = student.Student('test-username', 'test-uni')
    print('testing set uni')
    s.set_uni('uni-test')
    assert s.uni == 'uni-test'


def test_get_classes():
    s = student.Student('test-username', 'test-uni')
    s.add_class('test-class')
    assert s.get_classes() == ['test-class']


def test_get_profs():
    s = student.Student('test-username', 'test-uni')
    s.add_prof('test-prof')
    assert s.get_profs() == ['test-prof']


def test_look_up_class():
    users = {}
    s = student.Student('student1', 'uni1')
    s1 = student.Student('student2', 'uni2')
    s2 = student.Student('student3', 'uni3')

    users['student1'] = s
    users['student2'] = s1
    users['student3'] = s2

    s.add_class('test-class')
    s1.add_class('test-class')
    s2.add_class('test-class-1')

    test_str = s1.look_up_class('test-class', users)
    assert test_str == [s.uni, s1.uni]
    test_str = s1.look_up_class('test-class-1', users)
    assert test_str == [s2.uni]


def test_look_up_prof():
    users = {}
    s = student.Student('student1', 'uni1')
    s1 = student.Student('student2', 'uni2')
    s2 = student.Student('student3', 'uni3')

    users['student1'] = s
    users['student2'] = s1
    users['student3'] = s2

    s.add_prof('test-prof')
    s1.add_prof('test-prof')
    s2.add_prof('test-prof-1')

    test_str = s1.look_up_prof('test-prof', users)
    assert test_str == [s.uni, s1.uni]
    test_str = s1.look_up_prof('test-prof-1', users)
    assert test_str == [s2.uni]
