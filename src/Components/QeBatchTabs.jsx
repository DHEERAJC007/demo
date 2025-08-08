import React, { useState } from 'react';
import './QeBatchTabs.scss';
import { tabData } from '../Data/QeData';

const QeBatchTabs = () => {
  const [activeTab, setActiveTab] = useState('overdue');

  const statusIcon = {
  success: '✅',
  error: '❌',
  warning: '⚠️',
};

  return (
    <div className="qe-card">
      <div className="qe-header">
        <div className="qe-title-row">
          <span className="qe-icon">📄</span>
          <span className="qe-title">QE</span>
          <div className="qe-icons-right">
            <span className="icon-placeholder">⤢</span>
            <span className="icon-placeholder">⋮</span>
          </div>
        </div>

        <div className="qe-tabs">
          {['overdue', 'comingdue', 'new'].map((tab) => (
            <button
              key={tab}
              className={`tab-btn ${activeTab === tab ? 'active' : ''}`}
              onClick={() => setActiveTab(tab)}
            >
              {tab === 'overdue' ? 'Over due' : tab === 'comingdue' ? 'Coming due' : 'New'}
            </button>
          ))}
        </div>
      </div>

      <div className="qe-content">
        {tabData[activeTab].map((item, index) => (
          <div key={index} className="qe-item">
            <div className="left">
              <div className="top-line">
                <span className="type">{item.type}</span> <span className="id">{item.id}</span>
                <span className="check">{statusIcon[item.status] || ''}</span>
              </div>

              <div className="dispo">Dispo {item.dispo}</div>
            </div>
            <div className="right">
              <span className="brand">Breyunzi</span>
              {item.days !== null && (
                <span className="due-badge">{item.days} {item.days === 1 ? 'day' : 'days'}</span>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default QeBatchTabs;
