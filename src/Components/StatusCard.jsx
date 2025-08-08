import React from 'react';
import './StatusCard.scss';

const StatusCard = ({ title, totalBatches, stats, gradient }) => {
  return (
    <div className="status-card" style={{ background: gradient }}>
      <h3>{title}</h3>
      <p className="label">Batches</p>
      <p className="total">{totalBatches}</p>

      <hr />

      <div className="stats">
        {stats.map((stat, index) => (
          <div key={index} className="stat-row">
            <span className="stat-label">{stat.label}</span>
            <span className="stat-value">{stat.value}</span>
            <span className="badge">{stat.percentage}%</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default StatusCard;