import React from "react";
import { Link } from "react-router-dom";

const PlayerDashboard = () => {
  return (
    <div style={{ padding: 20 }}>
      <h2>👤 Player Dashboard</h2>
      <ul>
        <li><Link to="/player/games">🎮 Xem danh sách game</Link></li>
        <li><Link to="/player/review">✍️ Viết đánh giá</Link></li>
      </ul>
    </div>
  );
};

export default PlayerDashboard;
