import React, { useEffect, useState } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch('https://curly-system-w97w5pg6h5wpr-8000.app.github.dev/api/leaderboard')
      .then(response => response.json())
      .then(data => setLeaderboard(data));
  }, []);

  return (
    <div>
      <h1>Leaderboard</h1>
      <ul>
        {leaderboard.map(entry => (
          <li key={entry.id}>{entry.name}: {entry.score}</li>
        ))}
      </ul>
    </div>
  );
}

export default Leaderboard;
