// src/pages/Guest/GuestDashboard.js
import React from "react";
import { Link } from "react-router-dom";

const GuestDashboard = () => {
  return (
    <div style={{ padding: "20px" }}>
      <h2>Welcome Guest!</h2>
      <p>Bạn có thể chơi thử các game miễn phí hoặc đăng ký để trải nghiệm đầy đủ.</p>
      <nav>
        <ul>
          <li><Link to="/guest/home">Xem game miễn phí</Link></li>
          <li><Link to="/guest/register">Đăng ký tài khoản</Link></li>
        </ul>
      </nav>
    </div>
  );
};

export default GuestDashboard;
