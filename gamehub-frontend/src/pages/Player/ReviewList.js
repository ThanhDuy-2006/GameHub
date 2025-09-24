import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../../services/api";

const ReviewList = () => {
  const { gameId } = useParams();
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    const fetchReviews = async () => {
      try {
        const res = await api.get(`/game-reviews?game_id=${gameId}`);
        setReviews(res.data);
      } catch (err) {
        console.error("Lỗi khi lấy danh sách đánh giá:", err);
      }
    };
    fetchReviews();
  }, [gameId]);

  return (
    <div style={{ padding: 20 }}>
      <h2>⭐ Đánh giá cho game #{gameId}</h2>
      {reviews.length > 0 ? (
        <ul>
          {reviews.map((r) => (
            <li key={r.id}>
              <strong>Người chơi #{r.player_id}</strong>: {r.comment} ⭐{r.rating}
            </li>
          ))}
        </ul>
      ) : (
        <p>Chưa có đánh giá nào.</p>
      )}
    </div>
  );
};

export default ReviewList;
