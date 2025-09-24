import React, { useEffect, useState } from "react";
import api from "../../services/api";

const GameUpload = () => {
  const [games, setGames] = useState([]);
  const [form, setForm] = useState({
    name: "",
    description: "",
    price: 0,
    sources: "",
  });

  const devId = localStorage.getItem("role_id"); // ✅ lấy dev_id đã lưu khi login

  // Lấy danh sách game của dev
  const fetchGames = async () => {
    try {
      const res = await api.get(`/games/`);
      const myGames = res.data.filter((g) => g.dev_id === Number(devId));
      setGames(myGames);
    } catch (err) {
      console.error("Lỗi khi lấy danh sách game:", err);
    }
  };

  useEffect(() => {
    fetchGames();
  }, []);

  // Xử lý thay đổi input
  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // Upload game mới
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post("/games/", {
        ...form,
        dev_id: Number(devId),
      });
      alert("Upload game thành công!");
      setForm({ name: "", description: "", price: 0, sources: "" });
      fetchGames(); // refresh list
    } catch (err) {
      console.error("Lỗi khi upload game:", err);
      alert("Không thể upload game.");
    }
  };

  // Xóa game
  const handleDelete = async (gameId) => {
    if (!window.confirm("Bạn có chắc chắn muốn xóa game này?")) return;
    try {
      await api.delete(`/games/${gameId}`);
      alert("Đã xóa game thành công!");
      fetchGames();
    } catch (err) {
      console.error("Lỗi khi xóa game:", err);
      alert("Không thể xóa game.");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>🎮 Upload Game</h2>
      <form onSubmit={handleSubmit} style={{ maxWidth: 500 }}>
        <div>
          <label>Tên game</label>
          <input
            type="text"
            name="name"
            value={form.name}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Mô tả</label>
          <textarea
            name="description"
            value={form.description}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Giá</label>
          <input
            type="number"
            name="price"
            value={form.price}
            onChange={handleChange}
          />
        </div>
        <div>
          <label>Nguồn game (URL)</label>
          <input
            type="text"
            name="sources"
            value={form.sources}
            onChange={handleChange}
          />
        </div>
        <button type="submit">Upload</button>
      </form>

      <h3 style={{ marginTop: 30 }}>📋 Danh sách game của tôi</h3>
      {games.length > 0 ? (
        <ul>
          {games.map((g) => (
            <li key={g.id}>
              <strong>{g.name}</strong> - {g.price === 0 ? "Miễn phí" : `${g.price} $`}
              <button
                style={{ marginLeft: 10, color: "red" }}
                onClick={() => handleDelete(g.id)}
              >
                ❌ Xóa
              </button>
            </li>
          ))}
        </ul>
      ) : (
        <p>Chưa có game nào.</p>
      )}
    </div>
  );
};

export default GameUpload;
