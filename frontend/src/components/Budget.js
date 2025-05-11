import React, { useState, useEffect } from "react";

function Budget() {
  const [budgets, setBudgets] = useState([]);
  const [category, setCategory] = useState("");
  const [limit, setLimit] = useState("");

  useEffect(() => {
    fetch("/api/budget")
      .then((res) => res.json())
      .then((data) => setBudgets(data.budgets));
  }, []);

  const addBudget = (e) => {
    e.preventDefault();
    const newBudget = { category, limit: parseFloat(limit) };
    fetch("/api/budget", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newBudget),
    })
      .then((res) => res.json())
      .then((data) => {
        setBudgets([...budgets, data.budget]);
        setCategory("");
        setLimit("");
      });
  };

  return (
    <div>
      <h1>Budget Management</h1>
      <form onSubmit={addBudget}>
        <input
          type="text"
          placeholder="Category"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
        />
        <input
          type="number"
          placeholder="Limit"
          value={limit}
          onChange={(e) => setLimit(e.target.value)}
        />
        <button type="submit">Add Budget</button>
      </form>
      <ul>
        {budgets.map((b, index) => (
          <li key={index}>
            {b.category}: ${b.limit}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Budget;