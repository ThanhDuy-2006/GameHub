# TÀI LIỆU DỰ ÁN

## Sơ đồ tác nhân
![SoDoTacNhan](/docs/Dg/SoDoTacNhan.svg)
## UseCase 
![UseCaseTongThe](/docs/Dg/UseCaseTongThe.svg)

### Chức năng Guest
![Guest Usecase](./docs/Dg/GuestUseCase.svg)
### Chức năng Player
![Player Usecase.svg](/docs/Dg/Player%20Usecase.svg)
### Chức năng Developer
![Developer Usecase](./docs/Dg/Developer%20Usecase.svg)
### Chức năng Admin
![Admin Usecase](./docs/Dg/sơ%20đồ%20hoạt%20động%20của%20admin.svg)
### Chức năng của Graphic Designer
![Graphic Designer Usecase](./docs/Dg/UseCase_GD.svg)

## Sơ đồ hoạt động (Activity Diagram)

### Sơ đồ hoạt động 

### Quy trình xem danh sách mini game có sẵn của Guest
![GuestActList](./docs/Dg/GuestActLists.svg)
### Quy trình chơi thử mini game (không cần đăng nhập, không có leader board) của Guest
![GuestActTrial](./docs/Dg/GuestActTrial.svg)
### Quy trình đăng ký tài khoản (Player / Developer / Designer) của Guest
![GuestActRegister](./docs/Dg/GuestActRegister.svg)
### Quy trình nhập thông tin xác thực để trở thành Developer hoặc Designer hoặc cả hai của Guest
![GuestActVerify](./docs/Dg/GuestActVerify.svg)

### Quy trình đăng nhập của Player
![ActLogin.svg](./docs/Dg/ActLogin.svg)
### Quy trình chơi game và nhận thưởng của Player
![ActPlay.svg](./docs/Dg/ActPlay.svg)
### Quy trình đổi thưởng của Player
![ActRedeem.svg](./docs/Dg/ActRedeem.svg)
### Quy trình xem BXH và đánh giá của Player
![ActLB.svg](./docs/Dg/ActLB.svg)


### Quy trình đăng nhập của Developer
![DevActLogin](./docs/Dg/DevActLogin.svg)
### Quy trình Developer sử dụng asset miễn phí do Designer cung cấp
![DevUseFreeAsset](/docs/Dg/DevUseFreeAsset.svg)
### Quy trình Developer mua asset có phí từ Designer
![DevBuyAsset](/docs/Dg/DevBuyAsset.svg)
### Quy trình Developer đăng ký thông tin game mới và upload file game
![DevRegAndUpload](/docs/Dg/DevRegAndUpload.svg)
### Quy trình Developer khai báo để được cấp API cho leader board
![DevGetAPILeaderboard](/docs/Dg/DevGetAPILeaderboard.svg)
### Quy trình Developer khai báo để được cấp API, SDK, Document cho hệ thống tích điểm đổi quà
![DevGetAPISDKDOC](/docs/Dg/DevGetAPISDKDOC.svg)
### Quy trình Developer khai báo để được cấp API, SDK, Document cho hệ thống nạp tiền vào tài khoản game
![DevGetAPISDKDocOfPayment](/docs/Dg/DevGetAPISDKDocOfPayment.svg)
### Quy trình Developer quản lý danh sách game của mình (cập nhật, chỉnh sửa, xoá)
![Dev'sGameManage](/docs/Dg/Dev'sGameManage.svg)
### Quy trình Developer quản lý doanh thu từ game (nếu có)
![DevRev](/docs/Dg/DevRev.svg)


### Quy trình đăng nhập của Admin
![ActivityAdminLogin](./docs/Dg/ActivityAdminLogin.svg)
### Quy trình Quản lý User người dùng
![ActivityAdminManagentUser](./docs/Dg/ActivityAdminManagentUser.svg)
### Quy trình Quản lý thông tin game (duyệt game mới, kiểm tra nội dung)
![ActivityAdminManagentGame](./docs/Dg/ActivityAdminManagentGame.svg)
### Quy trình Quản lý asset (duyệt asset mới, xoá asset vi phạm)
![ActivityAdminManagentAsset](./docs/Dg/ActivityAdminManagentAsset.svg)
### Quy trình Quản lý thông tin thanh toán (chi trả cho Developer và Designer)
![ActivityAdminManagentPayout](./docs/Dg/ActivityAdminManagentPayout.svg)
### Quy trình Quản lý chính sách tích điểm – đổi quà
![ActivityAdminManagentRewardpolicy](./docs/Dg/ActivityAdminManagentRewardpolicy.svg)
### Quy trình Quản lý báo cáo, thống kê hệ thống
![ActivityAdminManagentReport](./docs/Dg/ActivityAdminManagentReport.svg)

### Quy trình đăng nhập của Graphic Designer
![ActivityLoginGraphicDesigner](./docs/Dg/ALogin_GD.svg)
### Quy trình quản lí danh sách asset của Graphic Designer
![ActivityManageassetlistGraphicDesigner](./docs/Dg/AManageasset_GD.svg)
### Quy trình upload asset của Graphic Designer
![ActivityUploadAsset](./docs/Dg/AUploadAsset_GD.svg)
### Quy trình đăng kí asset của Graphic Designer
![ActivityRegisterAssetGraphicDesigner](./docs/Dg/ADKi_GD.svg)
### Quy trình quản lý tài khoản cá nhân 
![ActivityManageMyAccoutGraphicDesigner](./docs/Dg/Amanagemyacccout_GD.svg)
### Quy trình theo dõi doanh thu từ asset
![ActivityTrackRevenueFromAssetGraphicDesigner](./docs/Dg/ATreackAsset_GD.svg)

## Sơ đồ luồng xử lý (Sequence Diagram)

### Luồng xử lý đăng nhập của Player
![SeqLogin.svg](./docs/Dg/SeqLogin.svg)
### Luồng xử lý chơi game và nhận thưởng của Player
![SeqPlayGame.svg](./docs/Dg/SeqPlayGame.svg)
### Luồng xử lý đổi thưởng của Player
![SeqRedeem.svg](./docs/Dg/SeqRedeem.svg)
### Luồng xử lý xem BXH và Review của Player
![SeqLB.svg](./docs/Dg/SeqLB.svg)

### Luồng xử lý đăng nhập của Developer
![SeqDevLogin.svg](/docs/Dg/SeqDevLogin.svg)
### luồng xử lý Developer sử dụng asset miễn phí do Designer cung cấp
![SeqDevUseFreeAsset.svg](/docs/Dg/SeqDevUseFreeAsset.svg)
### Luồng xử lý Developer mua asset có phí từ Designer
![SeqDevBuyAsset.svg](/docs/Dg/SeqDevBuyAsset.svg)
### Luồng xử lý Developer đăng ký thông tin game mới và upload file game
![SeqDevRegAndUpload.svg](/docs/Dg/SeqDevRegAndUpload.svg)
### Luồng xử lý Developer khai báo để được cấp API cho leader board
![SeqDevGetAPILeaderboard.svg](/docs/Dg/SeqDevGetAPILeaderboard.svg)
### Luồng xử lý Developer khai báo để được cấp API, SDK, Document cho hệ thống tích điểm đổi quà
![SeqDevGetAPISDKDocForReward.svg](/docs/Dg/SeqDevGetAPISDKDocForReward.svg)
### Luồng xử lý Developer khai báo để được cấp API, SDK, Document cho hệ thống nạp tiền vào tài khoản game
![SeqDevGetAPISDKDocForPayment.svg](/docs/Dg/SeqDevGetAPISDKDocForPayment.svg)
### Luồng xử lý Developer quản lý danh sách game của mình (cập nhật, chỉnh sửa, xoá)
![SeqDevManage.svg](/docs/Dg/SeqDevManage.svg)
### Luồng xử lý Developer quản lý doanh thu từ game (nếu có)
![SeqDevRev.svg](/docs/Dg/SeqDevRev.svg)

### Luồng xử lý đăng nhập của Admin
![SeqAdminLogin](./docs/Dg/SeqAdminLogin.svg)
### Quy trình Quản lý User người dùng
![SeqAdminManagentUser](./docs/Dg/SeqAdminManagentUser.svg)
### Quy trình Quản lý thông tin game (duyệt game mới, kiểm tra nội dung)
![SeqAdminManagentGame](./docs/Dg/SeqAdminManagentGame.svg)
### Quy trình Quản lý asset (duyệt asset mới, xoá asset vi phạm)
![SeqAdminManagentAsset](./docs/Dg/SeqAdminManagentAsset.svg)
### Quy trình Quản lý thông tin thanh toán (chi trả cho Developer và Designer)
![SeqAdminManagentPayout](./docs/Dg/SeqAdminManagentPayout.svg)
### Quy trình Quản lý chính sách tích điểm – đổi quà
![SeqAdminManagentRewardpolicy](./docs/Dg/SeqAdminManagentRewardpolicy.svg)
### Quy trình Quản lý báo cáo, thống kê hệ thống
![SeqAdminManagentReport](./docs/Dg/SeqAdminManagentReport.svg)

### Luồng xử lý xem danh sách mini game có sẵn
![SeqGuestList.svg](./docs/Dg/SeqGuestList.svg)
### Luồng xử lý chơi thử mini game (không cần đăng nhập, không có leader board)
![SeqGuestTrial.svg](./docs/Dg/SeqGuestTrial.svg)
### Luồng xử lý đăng ký tài khoản (Player / Developer / Designer)
![SeqGuestRegister.svg](./docs/Dg/SeqGuestRegister.svg)
### Luồng xử lý nhập thông tin xác thực để trở thành Developer hoặc Designer hoặc cả hai
![SeqGuestVerify.svg](./docs/Dg/SeqGuestVerify.svg)

### Luồng xử lý đăng nhập của Graphic Designer
![SeqGraphicDesignerLogin](./docs/Dg/SLogin_GD.svg)
### Luồng xử lý quản lý asset của Graphic Designer
![SeqGraphicDesignerManageassetlist](./docs/Dg/SManageAsset_GD.svg)
### Luồng xử lý Upload Asset của Graphic Designer
![SeqGraphicDesignerUploadAsset](./docs/Dg/SUploadAsset_GD.svg)
### Luồng xử lý đăng kí Asset của Graphic Designer
![SeqGraphicDesignerRegisterAsset](./docs/Dg/SRegisterAsset_GD.svg)
### Luồng xử lý quản lý tài khoản cá nhân của Graphic Designer
![SeqGraphicDesignerManageMyAccout](./docs/Dg/SMYACCout_GD.svg)
### Luồng xử lý theo dõi doanh thu từ Asset của Graphic Designer
![SeqGraphicDesignerTrackrevenue](./docs/Dg/STRack_GD.svg)

## Sơ đồ trạng thái 

### Tài khoản User
![UserAccount](/docs/Dg/UserAccount.svg)
### Game
![Game](/docs/Dg/Game.svg)
### Phiên chơi game
![TrangThaiThucThePhienChoi](./docs/Dg/TrangThaiThucThePhienChoi.svg)
### Asset (Designer)
![AssetDesigner](/docs/Dg/AssetDesigner.svg)
### Payment Transaction
![PaymentTransaction](/docs/Dg/PaymentTransaction.svg)
### Reward & Redemption
![RewardAndRedemption](/docs/Dg/RewardAndRedemption.svg)

## Mô hình kiến trúc
![MoHinhKienTruc](./docs/Dg/MoHinhKienTruc.svg)







Download source code (CMD)
git clone https://github.com/ChienNguyensrdn/Flask-CleanArchitecture.git
Kiểm tra đã cài python đã cài đặt trên máy chưa
python --version
Run app
Bước 1: Tạo môi trường ảo co Python (phiên bản 3.x)
Windows:
 	py -m venv .venv
Unix/MacOS:
 	python3 -m venv .venv
Bước 2: Kích hoạt môi trường:

Windows:
   .venv\Scripts\activate.ps1
Nếu xảy ra lỗi active .venv trên winos run powshell -->Administrator
Set-ExecutionPolicy RemoteSigned -Force
Unix/MacOS:
   source .venv/bin/activate
Bước 3: Cài đặt các thư viện cần thiết

Install:
   pip install -r requirements.txt
Bước 4: Chạy mã xử lý dữ liệu

Run:
   python app.py
Truy câp http://localhost:6868/docs