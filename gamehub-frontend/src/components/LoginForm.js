import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../services/authService";
import api from "../services/api";

const LoginForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const data = await login(username, password);

      // Lưu token, role, user_id
      localStorage.setItem("token", data.access_token);
      localStorage.setItem("role", data.role);
      localStorage.setItem("user_id", data.id);

      let roleId = null;

      // ✅ Lấy role_id từ API cụ thể
      if (data.role === "developer") {
        const res = await api.get(`/developers/get-by-user-id/${data.id}`);
        roleId = res.data.id;
      } else if (data.role === "player") {
        const res = await api.get(`/players/get-by-user-id/${data.id}`);
        roleId = res.data.id;
      } else if (data.role === "designer") {
        const res = await api.get(`/designers/get-by-user-id/${data.id}`);
        roleId = res.data.id;
      } else if (data.role === "admin") {
        const res = await api.get(`/admins/get-by-user-id/${data.id}`);
        roleId = res.data.id;
      }

      if (roleId) {
        localStorage.setItem("role_id", roleId);
      }

      // ✅ Điều hướng theo role
      if (data.role === "player") {
        navigate("/player/games");
      } else if (data.role === "developer") {
        navigate("/developer");
      } else if (data.role === "designer") {
        navigate("/designer");
      } else if (data.role === "admin") {
        navigate("/admin/dashboard");
      } else {
        navigate("/");
      }
    } catch (err) {
      console.error("Login error:", err);
      setError("Sai username hoặc password hoặc lỗi kết nối server");
    }
  };

  return (
    <div className="login-container">
      <h2>Đăng nhập</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Tên đăng nhập</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>

        <div>
          <label>Mật khẩu</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>

        {error && <p style={{ color: "red" }}>{error}</p>}

        <button type="submit">Đăng nhập</button>
      </form>
    </div>
  );
};

export default LoginForm;
