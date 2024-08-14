BTVN Tuần 6
Bài 1: 
Viết lambda expression truyền vào 2 kí tự a, b in thường. Trả về kí tự được
viết sau trong bảng chữ cái.
VD: ‘z’, ‘a’; cần trả về ‘z’.
‘b’, ‘b’; cần trả về ‘b’.

Bài 2:
Viết hàm truyền vào 1 ma trận n hàng, m cột rồi in ma trận chuyển vị của
nó sao cho mảng ban đầu không thay đổi.
Đầu vào 

1 2 3
4 5 6
7 8 9

Đầu ra
1 4 7
2 5 8
3 6 9

và mảng ban đầu vẫn là
1 2 3
4 5 6
7 8 9


Bài 3:
Viết một hàm calculate nhận vào một số lượng tham số không xác định và thực hiện các phép toán khác nhau trên chúng dựa trên tùy chọn đầu vào.
Hàm calculate sẽ nhận các tham số sau:
operation: Một chuỗi định nghĩa phép toán cần thực hiện ("add", "multiply", "max", "min").
*args: Danh sách các số để thực hiện phép toán.
Hàm calculate sẽ thực hiện:
Nếu operation là "add": Trả về tổng của tất cả các số trong *args.
Nếu operation là "multiply": Trả về tích của tất cả các số trong *args.
Nếu operation là "max": Trả về giá trị lớn nhất trong *args.
Nếu operation là "min": Trả về giá trị nhỏ nhất trong *args.
Nếu operation không hợp lệ: Trả về chuỗi "Invalid operation".
Bài 4:
Cho một số nguyên dương n. Hãy tính tổng các chữ số của số đó đến khi còn một chữ số. Xét thuật toán sau đây. Ví dụ:
n=123456
Bước 1: 123456 có 6 chữ số. Sum(12345)=1+2+3+4+5+6=21.
Bước 2: 21 có 2 chữ số. Sum(21)=2+1=3.
Bước 3: 3 có 1 chữ số. Kết thúc thuật toán.
Hỏi với một số nguyên dương bất kỳ cần bao nhiêu bước thực hiện trước khi kết thúc thuật toán và kết quả cuối cùng bằng bao nhiêu. Lưu ý với số có1 chữ số số bước thực hiện là 1.
Input:
Một số nguyên dương n duy nhất.
Output:
Một dòng duy nhất gồm hai số nguyên dương lần lượt là số kết quả của thuật toán và số bước thực hiện.

Bài 5:
Viết một hàm format_phone_number nhận vào một chuỗi số điện thoại và trả về số điện thoại đã được định dạng theo chuẩn quốc tế. Chuỗi số điện thoại đầu vào có thể chứa các ký tự không phải số (ví dụ: dấu gạch ngang, dấu chấm, khoảng trắng)
Yêu cầu:
Hàm phải loại bỏ tất cả các ký tự không phải là số khỏi chuỗi đầu vào.
Chuỗi phải bắt đầu bằng chữ số 0, nếu không trả về chuỗi "Invalid phone number".
Nếu chuỗi không hợp lệ (ít hơn hoặc nhiều hơn 10 chữ số sau khi loại bỏ ký tự không phải số), hàm sẽ trả về chuỗi "Invalid phone number".

