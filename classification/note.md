Q1: 	Implement thuật toán perceptron phân loại chữ số

So sánh feature vector của dữ liệu với feature vector của label và chọn ra cái giống nhất

Thực hiện duyệt nhiều lần và mỗi lần sẽ predict trên tập data train 

Sau đó sẽ thay đổi vector trọng số tùy thuộc vào predict đúng hay là sai như theo guide

Q2:	Return 100 feature với trọng số cao nhất trong các label

`	`Xem xem nó giống với list a hay list b và viết đáp số vào file answer.py

Duyệt 100 lần mỗi lần tìm ra argMax

Append argMax vào output và update lại trọng số 

(gán cho trọng số một giá trị thật nhỏ)

Q3: 	Cho 1 tập C. Đánh giá độ chính xác cho từng C và chọn ra C có độ chính xác cao nhất

Thuật toán tương tự như perceptron nhưng có thêm một tham số là r

Implement thuật toán theo guide

Q5: 	Thực hiện thuật toán đã sửa đổi perceptron cho pacman. 

`	`Không giống như perceptron cho các số, tất cả các nhãn đều dùng chung 1 vector trọng số w

Implement thuật toán theo guide

Q6: 	Thiết kế feature cho pacman

`	`stopAgent: agent chỉ đứng yên

`	`foodAgent: agent chỉ đi ăn mà không care xung quanh

`	`suicideAgent: agent chỉ di chuyển về phía con ma gần nhất

`	`contestAgent: một con agent thông minh tránh ma ăn các viên năng lượng và thức ăn





