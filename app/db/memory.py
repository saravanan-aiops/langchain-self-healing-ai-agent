import sqlite3

conn = sqlite3.connect(
    "incidents.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    issue TEXT,
    root_cause TEXT,
    remediation TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()


def save_incident(issue, root_cause, remediation):

    cursor.execute("""
    INSERT INTO incidents (
        issue,
        root_cause,
        remediation
    )
    VALUES (?, ?, ?)
    """, (
        issue,
        root_cause,
        remediation
    ))

    conn.commit()


def get_previous_incidents():

    cursor.execute("""
    SELECT * FROM incidents
    ORDER BY created_at DESC
    """)

    return cursor.fetchall()