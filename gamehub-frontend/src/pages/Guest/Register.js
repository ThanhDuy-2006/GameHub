import React, { useState } from "react";
import api from "../../services/api";

const Register = () => {
  const [form, setForm] = useState({
    username: "",
    password: "",
    role: "player", // mặc định
  });
  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage("");

    try {
      // tự động thêm status = active
      const payload = {
        ...form,
        status: "active",
      };

      const res = await api.post("/users/", payload);
      setMessage("Đăng ký thành công! ID: " + res.data.id);
    } catch (err) {
      if (err.response && err.response.data.error) {
        setMessage("Lỗi: " + err.response.data.error);
      } else {
        setMessage("Lỗi khi đăng ký.");
      }
    }
  };

  return (
    <div className="register-container" style={{ maxWidth: 400, margin: "auto", padding: 20 }}>
      <h2>Đăng ký tài khoản</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Tên đăng nhập</label>
          <input
            type="text"
            name="username"
            value={form.username}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Mật khẩu</label>
          <input
            type="password"
            name="password"
            value={form.password}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Vai trò</label>
          <select name="role" value={form.role} onChange={handleChange}>
            <option value="player">Player</option>
            <option value="developer">Developer</option>
            <option value="designer">Designer</option>
            <option value="admin">Admin</option>
          </select>
        </div>

        <button type="submit">Đăng ký</button>
      </form>

      {message && <p>{message}</p>}
    </div>
  );
};

export default Register;
