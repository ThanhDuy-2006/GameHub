import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import api from "../../services/api";

const GameDetail = () => {
  const { gameId } = useParams();
  const [game, setGame] = useState(null);

  useEffect(() => {
    const fetchGame = async () => {
      try {
        const res = await api.get(`/games/${gameId}`);
        setGame(res.data);
      } catch (err) {
        console.error("Lỗi khi lấy thông tin game:", err);
      }
    };
    fetchGame();
  }, [gameId]);

  if (!game) return <p>Đang tải...</p>;

  return (
    <div style={{ padding: 20 }}>
      <h2>{game.name}</h2>
      <p><strong>Mô tả:</strong> {game.description}</p>
      <p><strong>Giá:</strong> {game.price === 0 ? "Miễn phí" : `${game.price} $`}</p>
      <p><strong>Nguồn:</strong> <a href={game.sources} target="_blank" rel="noreferrer">{game.sources}</a></p>

      <div style={{ marginTop: 20 }}>
        <Link to={`/leaderboards/game/${gameId}`} style={{ marginRight: 10 }}>
          📊 Xem BXH
        </Link>
        <Link to={`/player/review?gameId=${gameId}`} style={{ marginRight: 10 }}>
          ✍️ Viết đánh giá
        </Link>
        <Link to={`/player/reviews/${gameId}`}>
          ⭐ Xem đánh giá
        </Link>
      </div>
    </div>
  );
};

export default GameDetail;
