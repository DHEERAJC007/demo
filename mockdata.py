batchData = [
  {
    "id": 'QE-232864',
    "batch": 'CDA 0457',
    "sla": '06-04-2025',
    "status": 'success',
    "slaStatus": 'danger',
    "product": 'Breyuanzi',
  },
  {
    "id": 'QE-232864',
    "batch": 'CDA 0457',
    "sla": '06-07-2025',
    "status": 'error',
    "slaStatus": 'warning',
    "product": 'Breyuanzi',
  },
  {
    "id": 'QE-232864',
    "batch": 'CDA 0457',
    "sla": '06-04-2025',
    "status": 'warning',
    "slaStatus": 'warning',
    "product": 'Breyuanzi',
  }
]

calendarData = {
  '2025-08-09': [
    {
      "batch": 'ACL 0456',
      "dispo": '06-06-2025',
      "joinId": '1WW0-194W5',
      "product": 'Breyuanzi',
      "status": 'success',
    },
    {
      "batch": 'ACL 0456',
      "dispo": '06-06-2025',
      "joinId": '1WW0-194W5',
      "product": 'Breyuanzi',
      "status": 'success',
    },
    {
      "batch": 'ACL 0457',
      "dispo": '06-08-2025',
      "joinId": '1WW0-194W6',
      "product": 'Breyuanzi',
      "status": 'warning',
    },
    {
      "batch": 'ACL 0458',
      "dispo": '06-09-2025',
      "joinId": '1WW0-194W7',
      "product": 'Breyuanzi',
      "status": 'info',
    }
  ],
  '2025-08-08': [
    {
      "batch": 'ACL 0456',
      "dispo": '06-06-2025',
      "joinId": '1WW0-194W5',
      "product": 'Breyuanzi',
      "status": 'error',
    },
    {
      "batch": 'ACL 0457',
      "dispo": '06-08-2025',
      "joinId": '1WW0-194W6',
      "product": 'Breyuanzi',
      "status": 'warning',
    },
    {
      "batch": 'ACL 0458',
      "dispo": '06-09-2025',
      "joinId": '1WW0-194W7',
      "product": 'Breyuanzi',
      "status": 'info',
    },
    {
      "batch": 'ACL 0459',
      "dispo": '06-10-2025',
      "joinId": '1WW0-194W8',
      "product": 'Breyuanzi',
      "status": 'success',
    }
  ],
  '2025-08-10': [
    {
      "batch": 'ACL 0460',
      "dispo": '06-11-2025',
      "joinId": '1WW0-194W9',
      "product": 'Breyuanzi',
      "status": 'success',
    },
    {
      "batch": 'ACL 0461',
      "dispo": '06-12-2025',
      "joinId": '1WW0-194W10',
      "product": 'Breyuanzi',
      "status": 'error',
    },
    {
      "batch": 'ACL 0462',
      "dispo": '06-13-2025',
      "joinId": '1WW0-194W11',
      "product": 'Breyuanzi',
      "status": 'warning',
    },
    {
      "batch": 'ACL 0463',
      "dispo": '06-14-2025',
      "joinId": '1WW0-194W12',
      "product": 'Breyuanzi',
      "status": 'info',
    }
  ]
}

tabData = {
  "overdue": [
  { "id": 'QE-137419', "type": 'QE', "dispo": '06-06-2025', "days": 3, "status": 'success' },
  { "id": 'ACL0456', "type": 'Batch', "dispo": '06-06-2025', "days": 3, "status": 'success' },
  { "id": 'ACY0474', "type": 'Batch', "dispo": '06-06-2025', "days": 2, "status": 'warning' },
  { "id": 'ACL 0456', "type": 'Batch', "dispo": '06-06-2025', "days": 1, "status": 'error' },
  { "id": 'ACL 0457', "type": 'Batch', "dispo": '06-08-2025', "days": 5, "status": 'success' }
  ],
  "comingdue": [
    { "id": 'CM-874512', "type": 'QE', "dispo": '08-08-2025', "days": 5, "status": 'success' },
    { "id": 'BCH874', "type": 'Batch', "dispo": '08-08-2025', "days": 7, "status": 'success' },
    { "id": 'BCH875', "type": 'Batch', "dispo": '08-08-2025', "days": 4, "status": 'warning' },
    { "id": 'BCH876', "type": 'Batch', "dispo": '08-08-2025', "days": 3, "status": 'error' },
    { "id": 'BCH877', "type": 'Batch', "dispo": '08-08-2025', "days": 2, "status": 'info' }
  ],
  "new": [
    { "id": 'NEW0456', "type": 'QE', "dispo": '08-10-2025', "days": 2, "status": 'info' },
    { "id": 'NEW0474', "type": 'Batch', "dispo": '08-10-2025', "days": 1, "status": 'info' },
    { "id": 'NEW1234', "type": 'Batch', "dispo": '08-10-2025', "days": 1, "status": 'info' },
    { "id": 'NEW5678', "type": 'Batch', "dispo": '08-10-2025', "days": 2, "status": 'info' },
    { "id": 'NEW9101', "type": 'Batch', "dispo": '08-10-2025', "days": 2, "status": 'info' }
  ]
}