// src/components/Navbar.js
import React from "react";
import { Link, useNavigate } from "react-router-dom";

const Navbar = () => {
  const navigate = useNavigate();
  const token = localStorage.getItem("token");
  const username = localStorage.getItem("username");
  const role = localStorage.getItem("role");

  const handleLogout = () => {
    localStorage.clear();
    navigate("/");
  };

  return (
    <nav className="navbar">
      <Link to="/">GameHub</Link>
      <div>
        {!token ? (
          <>
            <Link to="/login">Đăng nhập</Link>
            <Link to="/register">Đăng ký</Link>
          </>
        ) : (
          <>
            <span>
              Xin chào, {username} ({role})
            </span>
            <button onClick={handleLogout}>Đăng xuất</button>
          </>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
