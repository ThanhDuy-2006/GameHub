import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../../services/api";

const Leaderboard = () => {
  const { gameId } = useParams();
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const res = await api.get(`/leaderboards/game/${gameId}`);
        setLeaderboard(res.data);
      } catch (err) {
        console.error("Lỗi khi lấy bảng xếp hạng:", err);
      }
    };
    fetchLeaderboard();
  }, [gameId]);

  return (
    <div style={{ padding: 20 }}>
      <h2>🏆 Bảng xếp hạng - Game #{gameId}</h2>
      {leaderboard.length > 0 ? (
        <ol>
          {leaderboard.map((entry, idx) => (
            <li key={idx}>
              Người chơi #{entry.player_id} - Điểm: {entry.score}
            </li>
          ))}
        </ol>
      ) : (
        <p>Chưa có ai trong bảng xếp hạng.</p>
      )}
    </div>
  );
};

export default Leaderboard;
