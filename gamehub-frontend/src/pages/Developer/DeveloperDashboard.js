// src/pages/Developer/DeveloperDashboard.js
import React from "react";
import { Link } from "react-router-dom";

const DeveloperDashboard = () => {
  return (
    <div style={{ padding: "20px" }}>
      <h2>Developer Dashboard</h2>
      <nav>
        <ul>
          <li><Link to="/developer/game-upload">Đăng game</Link></li>
          <li><Link to="/developer/assets">Danh sách Asset</Link></li>
          <li><Link to="/developer/api">Truy cập API</Link></li>
          <li><Link to="/developer/account">Thông tin Tài khoản</Link></li>
        </ul>
      </nav>
    </div>
  );
};

export default DeveloperDashboard;
