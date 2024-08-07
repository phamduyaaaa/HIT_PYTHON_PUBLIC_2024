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
