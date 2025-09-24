// src/pages/Guest/HomePage.js
import React, { useEffect, useState } from "react";
import api from "../../services/api";

const HomePage = () => {
  const [games, setGames] = useState([]);

  useEffect(() => {
    const fetchGames = async () => {
      try {
        const res = await api.get("/games"); // lấy tất cả game
        // lọc chỉ game miễn phí
        const freeGames = res.data.filter((game) => game.price === 0);
        setGames(freeGames);
      } catch (err) {
        console.error("Lỗi khi load game:", err);
      }
    };
    fetchGames();
  }, []);

  return (
    <div>
      <h1>Game miễn phí</h1>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: "16px" }}>
        {games.length > 0 ? (
          games.map((game) => (
            <div key={game.id} style={{ border: "1px solid #ccc", padding: "10px" }}>
              <img
                src={game.thumbnail || "https://via.placeholder.com/200x120?text=No+Image"}
                alt={game.name}
                style={{ width: "100%" }}
              />
              <h3>{game.name}</h3>
              <p>{game.description}</p>
              <button>Chơi thử</button>
            </div>
          ))
        ) : (
          <p>Không có game miễn phí nào.</p>
        )}
      </div>
    </div>
  );
};

export default HomePage;
