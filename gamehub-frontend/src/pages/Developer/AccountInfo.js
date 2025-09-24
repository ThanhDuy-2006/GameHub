import React, { useEffect, useState } from "react";
import api from "../../services/api";

const DevAccountInfo = () => {
  const [developer, setDeveloper] = useState(null);
  const [paymentInfo, setPaymentInfo] = useState("");
  const [loading, setLoading] = useState(true);

  const roleId = localStorage.getItem("role_id"); // ✅ id developer thực

  // Fetch thông tin developer
  useEffect(() => {
    const fetchDeveloper = async () => {
      try {
        const res = await api.get(`/developers/${roleId}`);
        setDeveloper(res.data);
        setPaymentInfo(res.data.payment_info || "");
      } catch (err) {
        console.error("Lỗi khi lấy thông tin developer:", err);
      } finally {
        setLoading(false);
      }
    };
    fetchDeveloper();
  }, [roleId]);

  // Update payment info (cần user_id + payment_info)
  const handleUpdate = async () => {
    if (!developer) return;
    try {
      await api.put(`/developers/${roleId}`, {
        user_id: developer.user_id,   // ✅ backend cần user_id
        payment_info: paymentInfo,    // ✅ backend cần payment_info
      });
      alert("Cập nhật thông tin thanh toán thành công!");
    } catch (err) {
      console.error("Lỗi khi cập nhật:", err);
      alert("Không thể cập nhật thông tin!");
    }
  };

  if (loading) return <p>Đang tải thông tin...</p>;
  if (!developer) return <p>Không tìm thấy developer.</p>;

  return (
    <div style={{ padding: 20 }}>
      <h2>Thông tin Developer</h2>
      <p><strong>ID:</strong> {developer.id}</p>
      <p><strong>User ID:</strong> {developer.user_id}</p>

      <div>
        <label>Thông tin thanh toán</label>
        <textarea
          value={paymentInfo}
          onChange={(e) => setPaymentInfo(e.target.value)}
        />
      </div>
      <button onClick={handleUpdate}>Cập nhật</button>
    </div>
  );
};

export default DevAccountInfo;
