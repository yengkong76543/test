chị ơi, bữa trc em setup firewall VPS em chỉ whitelist port server havoc và port listener havoc với port web nữa á chị mà vài ngày chạy là vps bị suspended do abuse luôn 
Giải thích: Lí do em bị report là không hiểu về C2, Cách thức Hoạt Động, Avoid Detection, Signatute của C2 
Cụ thể: Signature là những gì đặc trưng để trích xuất của C2 đã biết 
signature:
Trong mỗi C2 như Havoc, Cobalt Strike, MSFConsole đều luôn có signature để AV detect được. Ví dụ trong CBS bản < 3.13 sẽ có khoảng trắng từ http status response
Trong C2 như em tìm hiểu listener port là 80 và 443, bản thân nó cũng là signature.
Nguyên nhân là 443 là https = http + ssl thì cái ssl em dùng mặc định của C2 havoc nó sẽ signature của havoc, mà cả trăm nghìn case đều xài chung 1 cấu trúc như serial number, jarm, ...(Hình minh họa)
Phần https từ khóa tìm hiểu là : JARM/ Hash TLS/SSL stack
Port: Em đang lấy port mặc định của havoc là 40056
User: Em đang lấy user mặc định của havoc là 5pider
DNS Server -> Thường trong profile của sẽ bị dính đến signature.
Giải pháp: Tìm hiểu về Havoc, những signature thường bị maps với havoc (toàn bộ các phiên bản trước đó và đang dùng), từ những signature đó, đưa ra giải pháp để bypass. 


kiểu này nè "target request --> VPS1. Confirm đúng IP target, mới allow IP cho forwart tiếp đúng IP target đến VPS2 (chứa source havoc) về C2" 


Client -> VPS 1 (port 80, 443) -> forward traffic VPS1:443 , VPS2:50000 -> VPS 2 (port 50000) -> RAT

