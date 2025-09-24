import React, { useEffect, useState } from "react";
import api from "../../services/api";

const AccountInfo = () => {
  const [designer, setDesigner] = useState(null);
  const [paymentinfo, setPaymentInfo] = useState("");
  const [loading, setLoading] = useState(true);

  const roleId = localStorage.getItem("role_id"); // ✅ id designer thực

  // Fetch thông tin designer
  useEffect(() => {
    const fetchDesigner = async () => {
      try {
        const res = await api.get(`/designers/${roleId}`);
        setDesigner(res.data);
        setPaymentInfo(res.data.paymentinfo || "");
      } catch (err) {
        console.error("Lỗi khi lấy thông tin designer:", err);
      } finally {
        setLoading(false);
      }
    };
    fetchDesigner();
  }, [roleId]);

  // Update payment info (cần user_id + paymentinfo)
  const handleUpdate = async () => {
    if (!designer) return;
    try {
      await api.put(`/designers/${roleId}`, {
        user_id: designer.user_id,   // ✅ backend cần user_id
        paymentinfo,                 // ✅ backend cần paymentinfo
      });
      alert("Cập nhật thông tin thanh toán thành công!");
    } catch (err) {
      console.error("Lỗi khi cập nhật:", err);
      alert("Không thể cập nhật thông tin!");
    }
  };

  if (loading) return <p>Đang tải thông tin...</p>;
  if (!designer) return <p>Không tìm thấy designer.</p>;

  return (
    <div style={{ padding: 20 }}>
      <h2>Thông tin Designer</h2>
      <p><strong>ID:</strong> {designer.id}</p>
      <p><strong>User ID:</strong> {designer.user_id}</p>

      <div>
        <label>Thông tin thanh toán</label>
        <textarea
          value={paymentinfo}
          onChange={(e) => setPaymentInfo(e.target.value)}
        />
      </div>
      <button onClick={handleUpdate}>Cập nhật</button>
    </div>
  );
};

export default AccountInfo;
