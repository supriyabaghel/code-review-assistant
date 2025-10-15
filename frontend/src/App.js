import React from "react";
import Dashboard from "./Dashboard";

console.log("✅ App.js is loaded");

function App() {
  console.log("App.js rendering Dashboard");
  return (
    <main className="relative flex items-center justify-center min-h-screen vignette bg-gradient-to-br from-[#CBE5FF] to-[#0A64D1]">
      <Dashboard />
    </main>
  );
}

export default App;
