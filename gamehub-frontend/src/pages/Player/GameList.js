import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../../services/api";

const GameList = () => {
  const [games, setGames] = useState([]);

  useEffect(() => {
    const fetchGames = async () => {
      try {
        const res = await api.get("/games/");
        setGames(res.data);
      } catch (err) {
        console.error("Lỗi khi lấy danh sách game", err);
      }
    };
    fetchGames();
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h2>🎮 Danh sách Game</h2>
      <ul>
        {games.map((game) => (
          <li key={game.id}>
            <Link to={`/games/${game.id}`}>
              {game.name} {game.price === 0 && "(Miễn phí)"}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default GameList;
