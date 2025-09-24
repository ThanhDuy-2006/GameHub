import React, { useEffect, useState } from "react";
import api from "../../services/api";

const AssetUpload = () => {
  const [assets, setAssets] = useState([]);
  const [form, setForm] = useState({
    name: "",
    price: 0,
    type: "image", // default type
  });

  const designerId = localStorage.getItem("role_id"); // ✅ lấy từ login

  // Fetch assets của designer
  useEffect(() => {
    const fetchAssets = async () => {
      try {
        const res = await api.get("/assets/");
        setAssets(res.data.filter((a) => a.designer_id == designerId)); // chỉ lấy asset của mình
      } catch (err) {
        console.error("Lỗi khi lấy asset:", err);
      }
    };
    fetchAssets();
  }, [designerId]);

  // Xử lý thay đổi form
  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // Upload asset
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await api.post("/assets/", {
        ...form,
        designer_id: parseInt(designerId, 10),
      });
      setAssets([...assets, res.data]);
      setForm({ name: "", price: 0, type: "image" });
      alert("Tải asset thành công!");
    } catch (err) {
      console.error("Lỗi khi upload asset:", err);
    }
  };

  // Xóa asset
  const handleDelete = async (id) => {
    if (!window.confirm("Bạn có chắc muốn xóa asset này?")) return;
    try {
      await api.delete(`/assets/${id}`);
      setAssets(assets.filter((a) => a.id !== id));
    } catch (err) {
      console.error("Lỗi khi xóa asset:", err);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Quản lý Assets</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Tên asset</label>
          <input
            type="text"
            name="name"
            value={form.name}
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
            min="0"
          />
        </div>
        <div>
          <label>Loại</label>
          <input
            type="text"
            name="type"
            value={form.type}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Upload Asset</button>
      </form>

      <h3>Danh sách Assets của bạn</h3>
      <ul>
        {assets.map((a) => (
          <li key={a.id}>
            {a.name} - {a.price === 0 ? "Miễn phí" : `${a.price} coins`} ({a.type})
            <button onClick={() => handleDelete(a.id)}>Xóa</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AssetUpload;
