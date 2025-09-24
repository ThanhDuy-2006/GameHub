import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
// import ProtectedRoute from "./components/ProtectedRoute";

import HomePage from "./pages/Guest/HomePage";
import Register from "./pages/Guest/Register";
import LoginForm from "./components/LoginForm";

// ✅ Player
import GameList from "./pages/Player/GameList";
import GameDetail from "./pages/Player/GameDetail";
import Leaderboard from "./pages/Player/Leaderboard";
import ReviewForm from "./pages/Player/ReviewForm";
import ReviewList from "./pages/Player/ReviewList";
import PlayerDashboard from "./pages/Player/PlayerDashboard";

// Developer
import DeveloperDashboard from "./pages/Developer/DeveloperDashboard";
import GameUpload from "./pages/Developer/GameUpload";
import AssetList from "./pages/Developer/AssetList";
import ApiAccess from "./pages/Developer/ApiAccess";
import DevAccountInfo from "./pages/Developer/AccountInfo";

// Designer
import DesignerDashboard from "./pages/Designer/DesignerDashboard";
import AssetUpload from "./pages/Designer/AssetUpload";
import AccountInfo from "./pages/Designer/AccountInfo";

// Admin
import AdminDashboard from "./pages/Admin/AdminDashboard";
import AdminUsers from "./pages/Admin/AdminUsers";
import AdminPayouts from "./pages/Admin/AdminPayouts";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        {/* Guest */}
        <Route path="/" element={<HomePage />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<LoginForm />} />

        {/* Player */}
        <Route path="/player/dashboard" element={<PlayerDashboard />} />
        <Route path="/player/games" element={<GameList />} />
        <Route path="/games/:gameId" element={<GameDetail />} />
        <Route path="/leaderboards/game/:gameId" element={<Leaderboard />} />
        <Route path="/player/review" element={<ReviewForm />} />
        <Route path="/player/reviews/:gameId" element={<ReviewList />} />

        {/* Developer */}
        <Route path="/developer" element={<DeveloperDashboard />} />
        <Route path="/developer/game-upload" element={<GameUpload />} />
        <Route path="/developer/assets" element={<AssetList />} />
        <Route path="/developer/api" element={<ApiAccess />} />
        <Route path="/developer/account" element={<DevAccountInfo />} />

        {/* Designer */}
        <Route path="/designer" element={<DesignerDashboard />} />
        <Route path="/designer/asset-upload" element={<AssetUpload />} />
        <Route path="/designer/account" element={<AccountInfo />} />

        {/* Admin */}
        <Route path="/admin/dashboard" element={<AdminDashboard />} />
        <Route path="/admin/users" element={<AdminUsers />} />
        <Route path="/admin/payouts" element={<AdminPayouts />} />
      </Routes>
    </Router>
  );
}

export default App;
