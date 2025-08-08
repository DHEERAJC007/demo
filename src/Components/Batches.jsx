import React, { useEffect, useState } from 'react';
import './Batches.scss';
// import batchData from '../Data/BatchesData';
import getBatchData from '../Services/BatchDataService';

const statusIcon = {
  success: '✅',
  error: '❌',
  warning: '⚠️',
};

const Batches = () => {

  const data12 = getBatchData();
  console.log('Batch Data:', data12);
  
  const [batchData, setBatchData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await getBatchData();
        setBatchData(data.batches);
        setLoading(false);
      } catch (err) {
        setError('Failed to load users.');
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="batch-list-container">
      <div className="header">
        <span role="img" aria-label="document">📄</span>
        <h2>Batches ({batchData.length})</h2>
      </div>

      {batchData.map((batch, index) => (
        <div className="batch-row" key={index}>
          <div className="batch-info">
            <div className="id-status">
              <span className="id">{batch.id}</span>
              <span className={`status-icon ${batch.status}`}>
                {statusIcon[batch.status]}
              </span>
            </div>
            <div className="batch-label">Batch {batch.batch}</div>
          </div>

          <div className="sla-info">
            <div className="sla-label">SLA</div>
            <div className={`sla-badge ${batch.slaStatus}`}>
              {batch.sla}
            </div>
          </div>

          <div className="product">{batch.product}</div>
        </div>
      ))}
    </div>
  );
};

export default Batches;
