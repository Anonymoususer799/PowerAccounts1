import React, { useState, useEffect } from "react";

function Analytics() {
  const [prediction, setPrediction] = useState("");

  useEffect(() => {
    fetch("/api/analytics/predict-expenses?days=30")
      .then((res) => res.json())
      .then((data) => setPrediction(data.prediction));
  }, []);

  return (
    <div>
      <h1>Advanced Analytics</h1>
      <p>{prediction}</p>
    </div>
  );
}

export default Analytics;