import React, { useState } from "react";
import { useSearchParams } from "react-router-dom";
import api from "../../services/api";

const ReviewForm = () => {
  const [searchParams] = useSearchParams();
  const gameId = searchParams.get("gameId");
  const playerId = localStorage.getItem("role_id"); // ✅ id player

  const [comment, setComment] = useState("");
  const [rating, setRating] = useState(5);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post("/game-reviews/", {
        game_id: Number(gameId),
        player_id: Number(playerId),
        comment,
        rating: Number(rating),
        review_date: new Date().toISOString(),
      });
      setComment("");
      setRating(5);
      alert("Đánh giá thành công!");
    } catch (err) {
      console.error("Lỗi khi gửi đánh giá", err);
      alert("Không thể gửi đánh giá.");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>✍️ Viết đánh giá cho game #{gameId}</h2>
      <form onSubmit={handleSubmit} style={{ maxWidth: 400 }}>
        <div>
          <label>Đánh giá (1-5):</label>
          <input
            type="number"
            min="1"
            max="5"
            value={rating}
            onChange={(e) => setRating(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Bình luận:</label>
          <textarea
            value={comment}
            onChange={(e) => setComment(e.target.value)}
            required
          />
        </div>
        <button type="submit">Gửi đánh giá</button>
      </form>
    </div>
  );
};

export default ReviewForm;
