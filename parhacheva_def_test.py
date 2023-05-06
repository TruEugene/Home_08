from parhacheva_def import pass_list

def test_pass_list_save():
    data = ['0,1,2,3,4,5,6,7,8,9,0,11', '0,1,2,3,4,5,6,7,8,9,0,11', '0,1,2,3,4,5,6,7,8,9,0,11']
    assert pass_list(data, '1') == data

def test_pass_list_notsave():
    data = ['0,1,2,3,4,5,6,7,8,9,0,11', '0,0,2,3,4,5,6,7,8,9,0,11', '0,1,2,3,4,5,6,7,8,9,0,11']
    assert pass_list(data, '0') == ['0,0,2,3,4,5,6,7,8,9,0,11']

def test_pass_list_notsave_fare():
    data = ['0,0,2,3,4,5,6,7,8,9,1000,11', '0,0,2,3,4,5,6,7,8,9,0,11', '0,0,2,3,4,5,6,7,8,9,1000,11']
    assert pass_list(data, '0') == ['0,0,2,3,4,5,6,7,8,9,0,11']
