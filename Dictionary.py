

if __name__ == "__main__":
    infor = {'name' :  '28tech', 'job' : 'dev', 'salary' : 500
             , 'web' : '28tech.com.vn', 'city' : "HCM"}
    #tạo dic bằng hàm dic() thông qua nested list
    a = [['name', '28tech'], ['job', 'dev'], ['web', 'brocode']]
    b = dict(a)

    print(b)
    #tạo dic bằng hàm zip tạo keys-value từ 2 mảng
    c = ['name', 'job', 'web']
    d = [1, 2,4]
    e = dict(zip(c, d))
    # nó sẽ chỉ tương ứng với các phần từ đầu
    print(e)
    # không có 2 key trùng nhau
    # key chứa nhiều value nó sẽ chứa value gần nhất bạn cập nhật
    #tạo dict bằng hàm fromkeys
    f = ['a', 'b', 'c']
    defaultvalue = 0
    g = dict.fromkeys(f, defaultvalue) # hiểu đơn giản là khởi tạo
    print(g)
    #nó se không có các key trùng nhau nếu có nó sẽ lấy
    #key-value cuối cùng trong dãy
    #key cùng k thể thay đổi nhưng value có thể nhé
    #nói chung k thể đẻ key ở trạng thái list
    h = {(1, 2) : [1, 2], 'name' : '28tech', 3 : 4}
    print(h)
    # để truy cậpvaof value thông qua key
    print(e['name']) # nhưng nếu k có key đó sẽ gây ra lỗi
    # để tránh lỗi ta dùng get()  nó sẽ trả về None nếu k có
    print(e.get('job'))

    # lấy bộ key, value, item bawfnhg key, value, item trong list

    j = list(h.keys())
    k = list(h.values())
    l = list(h.items())
    print(j)
    print(k)
    print(l) # trả về tuple
    # để truy cập

    for key in infor.keys():
        print(key, infor[key])
    for key, value in infor.items():
        print(key, value)

    for x in infor: # thì nó ch duyệt key thôi
        print(x, infor[x])

    # thêm và thay đổi value của key
    infor['ok'] = 'thanhtan'
    print(infor)
    infor['name'] = '27tech'
    print(infor)

    #xóa phần tu trong key

    if 'web' in infor:
        infor.pop('web')
    # cách 2 sử dụng del
    del infor['salary']
    print(infor)

    #popitem xóa phần tử ngẫu nhiên
    z = infor.popitem()
    print(z)
    print(infor)

    #kiểm tra sự tồn tại của key value giống set O(1)

    print('job' in infor)
    print('28tech' in infor.values())

    # thêm phần tử trong dict bằng update

    infor.update(e)
    print(infor)



