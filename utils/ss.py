'''
@File    :   ss.py
@Time    :   2020/12/03 20:40:38
@Author  :   wuyangyang
@Version :   1.0
@Contact :   wuyy@ushareit.com
@License :   (C)Copyright 2020-2021, SHAREIT
@Desc    :   None
'''


from sharestore_lib.SharestorePool import SharestorePool

def get_fake_item(item_id):
    options = {'host': 'test.main.cbs.sg2.sharestore', 'port': 9090}
    pool = SharestorePool(max_size=10, options=options)
    pool.SetTimeout(timeout_ms=100)
    segment = "scas_item_miniVideo_counter_test"
    key = "fake_data_init_time:{item_id}".format(item_id=item_id)
    value = pool.GetValue(segment, key, True)
    print(value)

p=90
g=88
def f(a, b=90):
    print(locals())
    breakpoint()

f('a', 'b')