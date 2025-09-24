import React, { useEffect, useState } from "react";
import api from "../../services/api";

const ApiAccess = () => {
  const [apis, setApis] = useState([]);
  const devId = localStorage.getItem("role_id");

  useEffect(() => {
    const fetchApiAccess = async () => {
      try {
        const res = await api.get(`/apiaccess/`);
        setApis(res.data);
      } catch (err) {
        console.error("Lỗi khi lấy API Access", err);
      }
    };
    fetchApiAccess();
  }, [devId]);

  return (
    <div style={{ padding: 20 }}>
      <h2>API Access của Developer</h2>
      {apis.length === 0 ? (
        <p>Tính năng đang cập nhật</p>
      ) : (
        <ul>
          {apis.map((apiItem) => (
            <li key={apiItem.id}>
              <strong>{apiItem.api_type}</strong> - API Key: {apiItem.api_key} - Trạng thái:{" "}
              {apiItem.status}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default ApiAccess;
