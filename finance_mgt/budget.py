from database.db import create_connection

def set_budget(user_id, category, amount, month, year):
    conn = create_connection()
    cursor = conn.cursor()

    # Check if budget already exists
    cursor.execute("""
        SELECT id FROM budgets
        WHERE user_id=? AND category=? AND month=? AND year=?
    """, (user_id, category, month, year))

    result = cursor.fetchone()

    if result:
        cursor.execute("""
            UPDATE budgets
            SET amount=?
            WHERE user_id=? AND category=? AND month=? AND year=?
        """, (amount, user_id, category, month, year))
    else:
        cursor.execute("""
            INSERT INTO budgets(user_id, category, amount, month, year)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, category, amount, month, year))

    conn.commit()
    conn.close()


def check_budget(user_id, category, month, year):
    conn = create_connection()
    cursor = conn.cursor()

    # Get budget limit
    cursor.execute("""
        SELECT amount FROM budgets
        WHERE user_id=? AND category=? AND month=? AND year=?
    """, (user_id, category, month, year))

    budget = cursor.fetchone()

    if not budget:
        conn.close()
        return None, None, None

    budget_limit = budget[0]

    # Get total expense in that category
    cursor.execute("""
        SELECT IFNULL(SUM(amount),0) FROM transactions
        WHERE user_id=? AND type='expense'
        AND category=?
        AND strftime('%m', date)=?
        AND strftime('%Y', date)=?
    """, (user_id, category, month, year))

    total_spent = cursor.fetchone()[0]
    conn.close()

    remaining = budget_limit - total_spent

    return budget_limit, total_spent, remaining