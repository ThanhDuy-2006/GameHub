// src/pages/Designer/DesignerDashboard.js
import React from "react";
import { Link } from "react-router-dom";

const DesignerDashboard = () => {
  return (
    <div style={{ padding: 20 }}>
      <h2>Designer Dashboard</h2>
      <ul>
        <li><Link to="/designer/asset-upload">Upload Asset</Link></li>
        <li><Link to="/designer/account">Thông tin Tài khoản</Link></li>
      </ul>
    </div>
  );
};

export default DesignerDashboard;


