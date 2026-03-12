from database.db import create_connection

def get_monthly_report(user_id,month,year):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""select ifnull(sum(amount),0) from transaction
                   where user_id=? and type='income'
                   and strftime('%m',date)=?
                   and strftime('%m',date)=?
                   and strftime('%y',date)=?""",
                   (user_id,month,year))
    total_income = cursor.fetchone()[0]

    cursor.execute("""select ifnull(sum(amount),0) from transactions
                   where user_id=? and type='expense'
                   and strftime('%m',date)=?
                   and strftime('%y',date)=?
                    """,(user_id,month,year))
    total_expense=cursor.fetchone()[0]

    conn.close()

    savings=total_income-total_expense

    return total_income,total_expense,savings

def get_yearly_report(user_id,year):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""select ifnull(sum(amount),0) from transaction
                   where user_id and type='expense'
                   and strftime('%y',date)=?"""
                   ,(user_id,year))
    total_income = cursor.fetchone()[0]

    cursor.execute("""select ifnull(sum(amount),0) from transactions
                   where user_id=? and type='expense'
                   and strftime('%y',date)=?
                   """,(user_id,year))
    total_expense = cursor.fetchone()[0]

    conn.close()

    savings = total_income-total_expense

    return total_income,total_expense,savings
    