import React from 'react';
import StatusCard from './StatusCard';

const Dues = () => {
  return (
    <div style={{ display: 'flex', gap: '20px' }}>
      <StatusCard
        title="Over due"
        totalBatches={121}
        gradient="linear-gradient(180deg, #fbd3e9 0%, #bb377d 100%)"
        stats={[
          { label: 'Missed', value: 87, percentage: 81 },
          { label: 'Completed', value: 34, percentage: 29 },
        ]}
      />

      <StatusCard
        title="Coming Due"
        totalBatches={45}
        gradient="linear-gradient(180deg, #43cea2 0%, #185a9d 100%)"
        stats={[
          { label: 'Ready for approval', value: 14, percentage: 32 },
          { label: 'Pending', value: 31, percentage: 68 },
        ]}
      />
    </div>
  );
};

export default Dues;