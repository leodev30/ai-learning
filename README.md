#**Project 2: Multi-Agent Search**

**Q1: Viết hàm đánh giá đơn giản các hành động trạng thái**

Tính giá trị của con pacman tại mỗi bước đi bất kỳ là bao nhiêu để chọn theo cái lớn nhất.

Code được implements trong evaluationFunction trả lại giá trị số thực thể hiện đánh giá giá trị bước đi.

Cách làm: sử dụng 2 đặc trưng : vị trí thức ăn và ví trí các con ma tới pacman

Tìm ra vị trí thức ăn gần nhất tới pacman

Nếu khoảng cách manhattan từ pacman tới con ma \&lt; 2 thì return về -float(&#39;inf&#39;)

**Q2: Sử dụng thuật toán minimax triển khai trong class MinimaxAgent ở hàm getAction**

Mỗi tầng max có n tầng min bên dưới (n là số con ma)

Max là các node của pacman

Min là các node của con ma

Cách làm: viết hàm minimaxSearch đệ quy theo thuật toán minimax

Trong hàm này em có thêm vào biến turn: đếm số lượt các con ma

Depth: độ sâu của cây tìm kiếm

Evals là mảng tính các node con của từng node bằng cách đệ quy.

Nếu là ma thì return min của evals còn nếu là pacman thì return max

**Q3: Sử dụng thuật toán tỉa alphabeta triển khai trong class AlphaBetaAgent ở hàm getAction**

Tương tự như thuật toán minimax thêm 2 biến alpha beta để cắt các nhánh

Sử dụng thuật toán như trong phần guide của Q3

**Q4: Expectimax triển khai tại class ExpectimaxAgent trong hàm getAction**

Tương tự thuật toán minimax

Ở các node min thì được thay bằng các node expec. Thay vì lấy min của các node con thì node expec sẽ lấy trung bình

**Q5. Viết một hàm đánh giá mới**

Chọn thêm các đặc trưng cho hàm đánh giá: vị trí thức ăn, số con ma có manhattan tới pacman \&lt; 3 và số con ma không sợ pacman

