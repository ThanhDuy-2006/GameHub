import React, { useEffect, useState } from "react";
import api from "../../services/api";

const AssetList = () => {
  const [assets, setAssets] = useState([]);

  useEffect(() => {
    const fetchAssets = async () => {
      try {
        const res = await api.get("/assets/");
        setAssets(res.data);
      } catch (err) {
        console.error("Lỗi khi lấy asset:", err);
      }
    };
    fetchAssets();
  }, []);

  const handleBuy = async (assetId, price) => {
    try {
      await api.post("/asset_purchases/", {
        dev_id: localStorage.getItem("role_id"),
        asset_id: assetId,
        amount_paid: price
      });
      alert("Mua thành công!");
    } catch (err) {
      console.error("Lỗi khi mua asset:", err);
      alert("Không mua được asset.");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Danh sách Asset</h2>
      <ul>
        {assets.map((asset) => (
          <li key={asset.id}>
            {asset.name} - {asset.type} - {asset.price}$
            {asset.price > 0 && (
              <button onClick={() => handleBuy(asset.id, asset.price)}>
                Mua
              </button>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AssetList;
