# 👑HIT_PYTHON_PUBLIC_2024👑

### 📌Bài 1: Python là ngôn ngữ thông dịch hay biên dịch? Tại sao?
- Python là ngôn ngữ thông dịch. Dưới đây là lý do:

> - Thông dịch: Python không biên dịch mã nguồn thành mã máy trước khi chạy. Thay vào đó, mã Python được thực thi bởi một trình thông dịch (interpreter). Trình thông dịch sẽ đọc và thực thi mã nguồn từng dòng một.
> - Linh động: Việc sử dụng trình thông dịch giúp Python linh hoạt và dễ dàng để phát triển, thử nghiệm và gỡ lỗi. Các lập trình viên có thể chạy mã từng dòng hoặc từng khối để kiểm tra kết quả ngay lập tức.
> - Mã bytecode: Khi mã Python được thực thi, nó được chuyển đổi thành một dạng mã bytecode tạm thời, sau đó mã bytecode này sẽ được thông dịch và thực thi bởi máy ảo Python (Python Virtual Machine - PVM).
### 📌BTVN Buổi 2
> Yêu cầu: Hoàn thành > 70% số lượng bài tập

### 🔍1.  Cơ Bản
#### 👉Bài 1: Tính tổng các chữ số trong một số nguyên dương
- Viết một chương trình yêu cầu người dùng nhập một số nguyên dương. Tính và in ra tổng các chữ số của số đó.
- `Ví dụ:`Đối với số 12345, tổng các chữ số là 1 + 2 + 3 + 4 + 5 = 15.
- Tính tổng các ước số của một số nguyên dương:
- Viết một chương trình yêu cầu người dùng nhập một số nguyên dương n. Tính và in ra tổng của tất cả các ước số của n. Ước số của một số là các số mà chia hết cho số đó mà không dư.
- `Ví dụ:`Ước số của 6 là 1, 2, 3, và 6.
- Kiểm tra tam giác:
- Viết chương trình yêu cầu người dùng nhập vào 3 số nguyên dương. Kiểm tra xem 3 số đó có tạo thành tam giác hay không? Nếu có thì đó là tam giác gì?(Cân, đều, vuông, nhọn, tù)
#### 👉Bài 2:  Cho 2 số a, b bất kỳ. Hãy in ra màn hình:
- a.    a cộng b
- b.    a trừ b
- c.    a nhân b
- d.    a chia lấy nguyên b
- e.    a mũ b
- f.     a chia dư b
- g.    so sánh a và b (lớn hơn, nhỏ hơn hay bằng)
- h.    a AND b
- i.     a OR b
- j.     a XOR b
- k.   NOT a == b
- l.    a dịch phải 1 đơn vị
- m.  a dịch trái 1 đơn vị

### 🔍2. Vận Dụng 
#### 👉Bài 3: Tính các tổng sau:
- S(n) = 1 - 2 + 3 - 4 + 5 + .... + (2*n + 1)
- S(n) = 1 + ½ + ⅓ + ¼ +.....+1/n
- Biện luận nghiệm của phương trình bậc 2 một ẩn
#### 👉Bài 4:  Dãy số Fibonacci
- Hãy viết chương trình tìm n số Fibonacci đầu tiên.
- Quy luật của dãy số Fibonacci: số tiếp theo bằng tổng của 2 số trước, 2 số đầu tiên của dãy số là 0, 1. `Ví dụ:` 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

### 🔍3.  Nâng Cao <Research>
#### 👉Bài 5: 
- Nhập vào 1 số n. Viết chương trình in ra tất cả các số Armstrong bậc 3 từ 1 đến n. (Số Armstrong bậc 3 là số mà tổng lập phương của các chữ số của nó bằng chính nó)
#### 👉Bài 6: 
- Nhập vào 1 số n. In ra tất cả các số hoàn hảo từ 1 đến n. ( Số hoàn hảo là số mà tổng các ước của nó (không tính chính nó) bằng chính nó ).

### 🔍4.  Research 
#### 👉Bài 7: 
- Viết một chương trình nhận vào một số N từ người dùng và in ra tất cả các cặp số Amicable từ 1 đến N. Cặp số Amicable là cặp số mà tổng các ước số của số thứ nhất bằng số thứ hai và ngược lại.
#### 👉Bài 8: 
- Viết một chương trình nhận vào một số N từ người dùng và in ra tam giác Pascal có N hàng.
#### 👉Bài 9: Cho một số a bất kỳ:
- a. Trả về số lượng các bits cần thiết để biểu diễn số a ở dạng nhị phân, không bao gồm phần dấu và các số 0 ở đầu.
- b. Với biến x = “awesome”, sử dụng 3 cách print để cùng đưa ra màn hình “Python is awesome”
- c. Viết chương trình kiểm tra version của python hiện tại
### 📌BTVN Buổi 3
> Yêu cầu: Hoàn thành > 70% số lượng bài tập
Vì các String, List là các object trong Python. Vì vậy mỗi object sẽ có các phương thức và thuộc tính riêng. Trong khi làm bài các bạn có thể sử dụng các phương thức để giải quyết vấn đề,  như là replace(), count(),... Sẽ rất có ích cho các bạn, giúp tiết kiệm thời gian và code ngắn gọn hơn!
#### 👉Bài 1:
- Nhập vào một list có N phần tử là số nguyên.(N nhập từ bàn phím):
- Nhập một số X từ bàn phím, kiểm tra số lần X xuất hiện trong list.
- Thay thế phần tử từ vị trí 2 -> 7 trong list thành [8, 5, 4, 0, 1, 3].
- Sử dụng list sau khi thay thế để giải quyết các bài toán tiếp theo.
- Tìm số lớn nhất, và nhỏ nhất trong list.
- Nhập một số Y tùy chọn từ bàn phím. Chèn số Y vào đầu list.
- Sau khi chèn số Y, kiểm tra các số trong list có sắp xếp theo thứ tự tăng dần hay giảm dần không. Nếu sắp xếp theo tăng dần thì in ra màn hình “TĂNG”, còn nếu sắp xếp theo thứ tự giảm dần thì in ra màn hình “GIÁM”, nếu không tăng không giảm thì in “NO”.
- Tạo một list mới có N phần tử. Các phần tử sẽ có vị trí từ 1 -> N. Với mỗi phần tử ở vị trí i (1 <= i <= N) giá trị của nó là tổng i phần tử đầu tiên của list cũ.
- Tạo một list mới [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000] và sắp xếp nó theo thứ tự tăng dần của giá trị, và sắp xếp nó theo sự tăng dần của giá trị tuyệt đối.

#### 👉Bài 2:
- Cho một list a gồm k phần tử(a và k nhập từ bàn phím). Nhập vào hai số nguyên n, m là số dòng và số cột của một ma trận.
- Hãy xây dựng ma trận X(n × m) với các phần tử lần lượt lấy ra từ list ở trên (nếu có thể).
- `Ví dụ:`: a = [1, 2, 4, 3, 5, 4, 3, 6, 1, 4, 2, 7, 4, 3, 4, 8, 7, 6], k = 18. Giả sử n = 3 và m = 4, ma trận x(3 × 4) thu được có dạng [[1, 2, 4, 3], [5, 4, 3, 6], [1, 4, 2, 7]].
- Nhưng với n = 3, m = 7 ta không thể xây dựng được ma trận. In ra kết quả nếu có thể, không thì in ra “NO”

#### 👉Bài 3: 
- Nhập 2 chuỗi s1, s2 từ bàn phím:
- In ra đảo ngược của chuỗi s1
- Nhập vào 2 số nguyên a, b (1 <=a < b <= len(s2)). In ra chuỗi s2 sau khi đảo ngược chuỗi từ vị trí a đến b.
- In ra chuỗi s3 là chuỗi s1 sau khi xóa các kí tự vị trí chẵn
- Trả về chuỗi s4 là đan xen các kí tự của s1 và s2
- `Ví dụ:` s1 = “abc”, s2 = “123” -> s4 = “a1b2c3”
- Đổi chỗ 2 ký tự đầu tiên của 2 chuỗi và in ra kết quả
- `Ví dụ:` s1 = “set”, s2 = “bit” -> “bet” và “sit”

#### 👉Bài 4: Chuẩn hóa định dạng họ tên
- Bạn Chiến đang rất bận với sự kiện sinh nhật của câu lạc bộ và cần sự trợ giúp của các bạn để xử lý một bài toán nhỏ. Đề bài như sau:
- Mô tả bài toán:
- Bạn nhận được một chuỗi văn bản chứa họ và tên của một thành viên trong câu lạc bộ. Tuy nhiên, chuỗi này chưa được viết đúng chuẩn theo định dạng họ tên.
- Yêu cầu:
- Hãy viết một chương trình để chuẩn hóa chuỗi họ tên này theo định dạng chuẩn, tức là mỗi từ trong họ tên đều bắt đầu bằng chữ cái viết hoa và các chữ cái còn lại là chữ thường. Định dạng chuẩn của họ tên là: "Họ Tên đệm Tên", với mỗi phần đều
- bắt đầu bằng chữ cái viết hoa.
- Input: Một chuỗi văn bản chứa họ và tên của một thành viên.
- Output: Chuỗi văn bản đã được chuẩn hóa theo định dạng chuẩn.
- `Ví dụ:` “lương Thái         sơN” -> “Lương Thái Sơn”

#### 👉Bài 5: Thầy giáo Ba và Nasus.	
- Thầy giáo Ba là một người đẹp trai, tài năng, tư duy tốt. Thầy thích các số 1, 3, 7, 5, 9 vì vậy các số trong hệ thập phân có chữ số cuối cùng  là một trong năm số trên thì thầy đều thích. Sắp tới là một dịp đặc biệt, Nasus là một học sinh đã
- được thầy giúp đỡ rất nhiều. Vì vậy anh ấy muốn tặng thầy các con số mà thầy thích. Nasus có một list chứa các số nguyên, Nasus đố các bạn trong list đó có bao nhiêu số mà thầy Ba sẽ thích, hãy in các số đó lên màn hình theo thứ tự tăng dần.
- Input:
- Dòng đầu tiên là một số nguyên N: số lượng số mà Nasus có, 1 <= N <= 100
- Dòng thứ hai có N số nguyên, mỗi số cách nhau bởi một dấu cách. Giá trị mỗi số nằm trong đoạn [1, 1000]
- Output: 
- Dòng đầu tiên là số lượng số thầy Ba thích trong các số Nasus có
- Dòng thứ hai là các số thầy Ba thích theo thứ tự tăng dần mà Nasus có
### Input
| một số nguyên N: số lượng số mà Nasus có | 1 <= N <= 100 |
|------------------|--------------|
|  N số nguyên, mỗi số cách nhau bởi một dấu cách | Giá trị mỗi số nằm trong đoạn [1, 1000]|

### Output
| số lượng số thầy Ba thích trong các số Nasus có  |
|------------------|
| các số thầy Ba thích theo thứ tự tăng dần mà Nasus có  | 


- `Ví dụ:`

### Input
| Số lượng phần tử | Danh sách số |
|------------------|--------------|
| 10               | 1 4 29 187 2 30 50 87 12 34 |

### Output
| Số lượng kết quả | Kết quả      |
|------------------|--------------|
| 4                | 1 29 87 187  |

### 📌BTVN Buổi 5
#### 👉Bài 1: Tạo một từ điển gồm có các khóa là Mã sinh viên, các giá trị lưu trữ là Điểm tổng kết của sinh viên.
- Cho biết có bao nhiêu sinh viên có điểm tổng kết trong đoạn [3.0, 3.5].
- Bổ sung thêm 1 sinh viên vào từ điển.
- Xóa mọi sinh viên có điểm tổng kết nhỏ hơn 2.0 ra khỏi từ điển.
- In toàn bộ từ điển ra màn hình.
#### 👉Bài 2: Cho 1 chuỗi được nhập từ bàn phím. In ra 1 dict có có key là các kí tự trong chuỗi và value là số lần kí tự đó xuất hiện trong chuỗi.

#### 👉Bài 3:Bạn A đang được giao nhiệm vụ là lập N (10 <= N <= 100000) tài khoản sinh viên cho Trường Đại Học Công Nghiệp theo với format như sau:
- Tên tài khoản chính là Mã Sinh Viên tuần tự là 2023600001,
2023600002, … (việc tạo mã sinh viên phải đảm bảo độ dài luôn là
10).
- Mật khẩu chính là một string được lấy random trong list
 [CNTT; KHMT; KTPM; HTTT] + mã số sinh viên. (Gợi ý: Sử dụng
hàm choice() trong thư viện random).
- Yêu Cầu : Em hãy tạo 1 dictionary chứa thông tin tài khoản của N
sinh viên với mỗi phần tử trong dictionary lưu dictionary con theo
dạng:
“Account + (vị trí [i] +1)”:{
“Username”: lưu tên tài khoản tại đây
“Password”: lưu mật khẩu của tài khoản này tại đây}
`Ví dụ:`
“Account1” : {
“Username”: 2023600001,
“Password”: KTPM2023600001    #lưu ý đây là random ra KTPM
}
#### 👉Bài 4: Tạo một từ điển chứa nội dung file CONFIG sau:
| Keys | Values |
|:---------:|:---------:|
| n | 1500 |
| m |  2|
| CLUSTERS |  3|
| ITER |  10000|
| METHOD | FCM|
| MEASURE | EUCLIDEAN|
| YEARS | 51|
- In nội dung từ điển ra màn hình.
- Sửa lại thông số MEASURE = “MANHATAN”, in kết quả.
- Cho biết thông số METHOD hiện đang được đặt là gì (in ra màn hình).
- Bổ sung thêm thông số “LOSS FUNCTION” có giá trị là “NORM_2”, in kết
quả.
- Xóa thông số YEARS trong từ điển, in kết quả.
- Nhập vào một xâu S từ bàn phím. Cho biết S có trùng với giá trị của thông số
nào trong file CONFIG hay không?
- Tạo một set chứa toàn bộ giá trị của các thông số trong file CONFIG ở trên, in
kết quả.
- Tạo một list chứa toàn bộ giá trị của các thông số trong file CONFIG ở trên, in
kết quả.

