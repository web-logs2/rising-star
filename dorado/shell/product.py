# -\*- coding: utf-8 -\*-
import random
import sys


if __name__ == '__main__':

    argv = sys.argv
    if len(argv) > 2:
        print('只能有一个参数，参数为要生成的数据条数')
        sys.exit()
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('参数必须是整形')
        sys.exit()
    except IndexError:
        print('未输入参数，默认20条')
        n = 20

    with open('a.txt', 'w') as data:
        for i in range(n):
            id = str(random.randint(1, 1000))
            col_string = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 4)) + \
                         random.choice(['12', '24', '31', '23', '67', '99', '47', '53', '76', '82'])
            col_bigint = str(random.randint(1, 1000))
            col_boolean = random.choice(['true', 'false'])
            col_double = str(random.random() * 50)[:4]
            col_decimal = str(random.uniform(0, 100))[:5]
            col_array_string = ''.join(
                random.sample('zyxwvutsrqponmlkjihgfedcba', random.randint(1, 3))) + '\002' + ''.join(
                random.sample('zyxwvutsrqponmlkjihgfedcba', random.randint(1, 3))) + '\002' + ''.join(
                random.sample('zyxwvutsrqponmlkjihgfedcba', random.randint(1, 3)))
            tmp_list = []
            for j in {'姓名': ''.join(random.sample('ZYXWVUTSRQPONMLKJIHGFEDCBA', 4)), '年龄': random.randint(1, 100),
                      '性别': random.choice(['男', '女'])}.items():
                tmp_list.append(j[0] + ':' + str(j[1]))
            col_map_s_s = '\002'.join(tmp_list)

            result = ','.join(
                [id, col_string, col_bigint, col_boolean, col_double, col_decimal, col_array_string, col_map_s_s])

            if i == n - 1:
                data.write(result)
            else:
                data.write(result + '\n')
    print("success，请检查数据")
    data.close()
