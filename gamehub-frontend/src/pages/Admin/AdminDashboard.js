import React from "react";
import { useNavigate } from "react-router-dom";

const AdminDashboard = () => {
  const navigate = useNavigate();

  return (
    <div style={{ padding: 20 }}>
      <h2>Admin Dashboard</h2>
      <p>Chọn chức năng quản lý:</p>

      <div style={{ display: "flex", gap: "20px", marginTop: "20px" }}>
        <button onClick={() => navigate("/admin/users")}>
          Quản lý Người dùng
        </button>
        <button onClick={() => navigate("/admin/payouts")}>
          Quản lý Thanh toán (Payouts)
        </button>
      </div>
    </div>
  );
};

export default AdminDashboard;
