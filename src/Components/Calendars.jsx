import React, { useEffect, useState } from 'react';
import './CalendarView.scss';
import { getCalendarData } from '../Services/BatchDataService';

const weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];

const generateNext7Days = () => {
  const today = new Date();
  return Array.from({ length: 14 }).map((_, i) => {
    const date = new Date(today);
    date.setDate(date.getDate() + i);
    return {
      day: weekdays[date.getDay() - 1] || 'Sun',
      date: date.getDate(),
      fullDate: date.toISOString().split('T')[0],
    };
  });
};

const statusIcons = {
  success: '✅',
  error: '❌',
};

const Calendars = () => {
  const dates = generateNext7Days();
  const [selectedDate, setSelectedDate] = useState(dates[2].fullDate);
  const [calendarData, setCalendarData] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await getCalendarData();
        setCalendarData(data.batches);
        setLoading(false);
      } catch (err) {
        setError('Failed to load calendar.');
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const dataForDate = calendarData[selectedDate] || [];

  return (
    <div className="calendar-container">
      <div className="header">
        <span role="img" aria-label="calendar">📅</span>
        <h2>Calendar</h2>
      </div>

      <div className="date-strip">
        {dates.map((d) => (
          <div
            key={d.fullDate}
            className={`date-item ${selectedDate === d.fullDate ? 'active' : ''}`}
            onClick={() => setSelectedDate(d.fullDate)}
          >
            <div>{d.day}</div>
            <div>{d.date}</div>
          </div>
        ))}
      </div>

      {loading ? (
        <div>Loading...</div>
      ) : error ? (
        <div>{error}</div>
      ) : dataForDate.length === 0 ? (
        <div>No batches for this date.</div>
      ) : (
        dataForDate.map((batch, idx) => (
          <div key={idx} className="batch-card">
            <div className="batch-top">
              <div>
                <strong>Batch</strong> {batch.batch}{' '}
                <span className={`status-icon ${batch.status}`}>
                  {statusIcons[batch.status]}
                </span>
              </div>
              <div>{batch.product}</div>
            </div>
            <div className="batch-bottom">
              <div>Dispo {batch.dispo}</div>
              <div>Join ID {batch.joinId}</div>
            </div>
          </div>
        ))
      )}
    </div>
  );
};

export default Calendars;