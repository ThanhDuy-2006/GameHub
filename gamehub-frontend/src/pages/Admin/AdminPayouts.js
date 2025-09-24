import React, { useEffect, useState } from "react";
import api from "../../services/api";

const AdminPayouts = () => {
  const [payouts, setPayouts] = useState([]);
  const [loading, setLoading] = useState(true);

  // State cho form tạo payout
  const [recipientId, setRecipientId] = useState("");
  const [recipientType, setRecipientType] = useState("developer");
  const [amount, setAmount] = useState("");

  const fetchPayouts = async () => {
    try {
      const res = await api.get("/payout-transactions/");
      setPayouts(res.data);
    } catch (err) {
      console.error("Lỗi khi lấy payout transactions:", err);
    } finally {
      setLoading(false);
    }
  };

  const updateStatus = async (id, newStatus) => {
    try {
      const payout = payouts.find((p) => p.id === id);
      const adminId = localStorage.getItem("role_id"); // ✅ id admin thực

      await api.put(`/payout-transactions/${id}`, {
        recipient_id: payout.recipient_id,
        recipient_type: payout.recipient_type,
        amount: payout.amount,
        status: newStatus,
        processed_by_admin_id: adminId, // ✅ thêm admin xử lý
      });

      setPayouts(
        payouts.map((p) =>
          p.id === id ? { ...p, status: newStatus, processed_by_admin_id: adminId } : p
        )
      );
      alert("Cập nhật trạng thái thành công");
    } catch (err) {
      console.error("Lỗi khi cập nhật trạng thái:", err);
    }
  };

  // Xóa payout
  const deletePayout = async (id) => {
    try {
      await api.delete(`/payout-transactions/${id}`);
      setPayouts(payouts.filter((p) => p.id !== id));
      alert("Đã xóa payout");
    } catch (err) {
      console.error("Lỗi khi xóa payout:", err);
    }
  };

  // Tạo payout mới
  // Tạo payout mới
const handleCreatePayout = async (e) => {
  e.preventDefault();
  try {
    await api.post("/payout-transactions/", {
      recipient_id: parseInt(recipientId),
      recipient_type: recipientType,
      amount: parseFloat(amount),
      status: "pending", // ✅ chỉ gửi status
      // ❌ KHÔNG gửi processed_by_admin_id khi tạo
    });
    setRecipientId("");
    setAmount("");
    fetchPayouts();
    alert("Tạo payout thành công!");
  } catch (err) {
    console.error("Lỗi khi tạo payout:", err);
  }
};


  useEffect(() => {
    fetchPayouts();
  }, []);

  if (loading) return <p>Đang tải danh sách payout...</p>;

  return (
    <div style={{ padding: 20 }}>
      <h2>Quản lý Payout Transactions</h2>

      {/* Form tạo payout mới */}
      <form onSubmit={handleCreatePayout} style={{ marginBottom: 20 }}>
        <h3>Tạo payout mới</h3>
        <div>
          <label>Recipient ID:</label>
          <input
            type="number"
            value={recipientId}
            onChange={(e) => setRecipientId(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Recipient Type:</label>
          <select
            value={recipientType}
            onChange={(e) => setRecipientType(e.target.value)}
          >
            <option value="developer">Developer</option>
            <option value="designer">Designer</option>
          </select>
        </div>
        <div>
          <label>Số tiền:</label>
          <input
            type="number"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            required
          />
        </div>
        <button type="submit">Tạo payout</button>
      </form>

      {/* Danh sách payouts */}
      <table border="1" cellPadding="8" style={{ width: "100%", marginTop: 10 }}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Recipient</th>
            <th>Loại</th>
            <th>Số tiền</th>
            <th>Trạng thái</th>
            <th>Hành động</th>
          </tr>
        </thead>
        <tbody>
          {payouts.map((p) => (
            <tr key={p.id}>
              <td>{p.id}</td>
              <td>{p.recipient_id}</td>
              <td>{p.recipient_type}</td>
              <td>{p.amount}</td>
              <td>{p.status}</td>
              <td>
                {p.status === "pending" && (
                  <>
                    <button onClick={() => updateStatus(p.id, "approved")}>
                      Duyệt
                    </button>
                    <button onClick={() => updateStatus(p.id, "rejected")}>
                      Từ chối
                    </button>
                  </>
                )}
                <button onClick={() => deletePayout(p.id)}>Xóa</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AdminPayouts;
