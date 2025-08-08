from flask import Flask, jsonify, request
from flasgger import Swagger
from mockdata import batchData, calendarData, tabData

app = Flask(__name__)
swagger = Swagger(app)

@app.after_request
def add_cors_headers(resp):
    origin = request.headers.get("Origin")
    # allow only your dev origin
    if origin in {"http://localhost:3000", "http://127.0.0.1:3000"}:
        resp.headers["Access-Control-Allow-Origin"] = origin
        resp.headers["Vary"] = "Origin"
        resp.headers["Access-Control-Allow-Credentials"] = "true"
        resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        resp.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
    return resp
 
@app.route('/user-profile', methods=['GET'])
def get_user_profile():
    """
    Get logged-in user profile.
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: Bearer token (e.g., "Bearer your_token_here")
    responses:
      200:
        description: User profile details
        examples:
          application/json: {
            "name": "Vani",
            "time": "07:15 AM",
            "date": "30-04-2025",
            "user_id":1
          }
    """
    return jsonify({
        "name": "Vani",
        "time": "07:15 AM",
        "date": "30-04-2025",
        "user_id":1
    })
 
@app.route('/insights', methods=['GET'])
def get_insights():
    """
    Fetch recent disposition insights.
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: Bearer token
    responses:
      200:
        description: List of insights
        examples:
          application/json: {
            "insights": [
              {
                "type": "New",
                "message": "Productivity has increased by 200%",
                "time": "6:30 PM, 24-04-2025"
              }
            ]
          }
    """
    return jsonify({
        "insights": [
            {
                "type": "New",
                "message": "Productivity has increased by 200%",
                "time": "6:30 PM, 24-04-2025"
            }
        ]
    })
 
@app.route('/batches', methods=['GET'])
def get_all_batches():
    """
    Fetch all batches.
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: Bearer token
      - name: status
        in: query
        type: string
        required: false
        description: Status filter (e.g., all, overdue, coming-due)
    responses:
      200:
        description: Batch list
        examples:
          application/json: {
            "batches": [
              {
                "id": "QE-232864",
                "batch": "CDA 0457",
                "sla": "06-04-2025",
                "product": "Breyanzi",
                "status": "overdue"
              }
            ]
          }
    """
    return jsonify({
        "batches": batchData
    })
 
@app.route('/batches/overdue-summary', methods=['GET'])
def get_overdue_summary():
    """
    Summary of overdue batches.
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: Bearer token
    responses:
      200:
        description: Overdue counts
        examples:
          application/json: {
            "total": 121,
            "missed": 87,
            "completed": 34
          }
    """
    return jsonify({
        "total": 121,
        "missed": 87,
        "completed": 34
    })
 
@app.route('/batches/coming-due-summary', methods=['GET'])
def get_coming_due_summary():
    """
    Summary of batches that are coming due.
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: Bearer token
    responses:
      200:
        description: Coming due counts
        examples:
          application/json: {
            "total": 45,
            "ready_for_approval": 14,
            "pending": 31
          }
    """
    return jsonify({
        "total": 45,
        "ready_for_approval": 14,
        "pending": 31
    })
 
@app.route('/qe-batches', methods=['GET'])
def get_qe_batches():
    """
    Get QE batch disposition details.
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: Bearer token
      - name: status
        in: query
        type: string
        required: false
        description: Filter by status (overdue, coming-due, new)
    responses:
      200:
        description: QE batch info
        examples:
          application/json: {
            "batches": [
              {
                "id": "QE-137419",
                "batch": "ACL0456",
                "dispo_date": "06-06-2025",
                "due_in": "3 days"
              }
            ]
          }
    """
    return jsonify({
        "batches": tabData
    })
 
@app.route('/qc-batches', methods=['GET'])
def get_qc_batches():
    """
    Get QC Testing batch disposition details.
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: Bearer token
      - name: status
        in: query
        type: string
        required: false
        description: Filter by status (overdue, coming-due, new)
    responses:
      200:
        description: QC batch info
        examples:
          application/json: {
            "batches": [
              {
                "id": "QE-137419",
                "batch": "ACL0456",
                "dispo_date": "06-06-2025",
                "due_in": "3 days"
              }
            ]
          }
    """
    return jsonify({
        "batches": tabData
    })
 
@app.route('/calendar-batches', methods=['GET'])
def get_calendar_batches():
    """
    Fetch batches for calendar view.
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: Bearer token
      - name: fromDate
        in: query
        type: string
        required: true
        description: Start date (YYYY-MM-DD)
      - name: toDate
        in: query
        type: string
        required: true
        description: End date (YYYY-MM-DD)
    responses:
      200:
        description: Calendar-scheduled batches
        examples:
          application/json: {
            "batches": [
              {
                "batch": "ACL0456",
                "dispo_date": "2025-06-06",
                "join_id": "1WWO-194WS"
              }
            ]
          }
    """
    return jsonify({
        "batches": calendarData
    })
 
@app.route('/batch-overview-stats', methods=['GET'])
def get_batch_overview():
    """
    Get batch overview statistics (for chart).
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: Bearer token
      - name: range
        in: query
        type: string
        required: false
        description: Range of days (e.g., last7days)
    responses:
      200:
        description: Batch stats by day
        examples:
          application/json: {
            "data": [
              {
                "date": "2025-03-25",
                "completed": 17,
                "missed": 4,
                "in_progress": 10
              }
            ]
          }
    """
    return jsonify({
        "data": [
            {
                "date": "2025-03-25",
                "completed": 17,
                "missed": 4,
                "in_progress": 10
            }
        ]
    })
 
@app.route('/ai/query', methods=['POST'])
def ai_query():
    """
    AI assistant query for batch-related information.
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: Bearer token
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            query:
              type: string
              example: "What is the status of batch ACL0456?"
    responses:
      200:
        description: AI-generated response
        examples:
          application/json: {
            "answer": "Batch ACL0456 is due in 3 days and is assigned to QC Testing."
          }
    """
    return jsonify({
        "answer": "Batch ACL0456 is due in 3 days and is assigned to QC Testing."
    })
 
 
@app.route('/batches_qc_qe', methods=['GET'])
def get_batches():
    """
    Get batch disposition details for QE or QC.
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: Bearer token
      - name: type
        in: query
        type: string
        required: true
        description: Type of batch, either "qe" or "qc"
      - name: status
        in: query
        type: string
        required: false
        description: Filter by status (overdue, coming-due, new)
    responses:
      200:
        description: Batch disposition info
        examples:
          application/json: {
            "batches": [
              {
                "id": "QE-137419",
                "batch": "ACL0456",
                "dispo_date": "06-06-2025",
                "due_in": "3 days",
                "state": "qe"
              },
              {
                "id": "QC-157839",
                "batch": "BND-3210",
                "dispo_date": "10-06-2025",
                "due_in": "5 days",
                "state": "qc"
              }
            ]
          }
    """
    # Hardcoded response based on batch type (qe or qc)
    batches = [
        {
            "id": "QE-137419",
            "batch": "ACL0456",
            "dispo_date": "06-06-2025",
            "due_in": "3 days",
            "state": "qe"
        },
        {
            "id": "QC-157839",
            "batch": "BND-3210",
            "dispo_date": "10-06-2025",
            "due_in": "5 days",
            "state": "qc"
        }
    ]
 
    return jsonify({"batches": batches})
 
 
if __name__ == '__main__':
    app.run(debug=True)