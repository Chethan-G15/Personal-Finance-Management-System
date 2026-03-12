from database.db import create_connection

def add_transaction(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    t_type = input("enter type(income/expense):")
    category = input("enter category:")
    amount = float(input("enter amount:"))
    date = input("Enter date[yyyy-mm-dd]")
    cursor.execute("""insert into transaction (user_id,type,category,amount,date) values(?,?,?,?,?)""",(user_id,t_type,category,amount,date))

    conn.commit()
    conn.close()

    print("transaction added successfully")

def view_transaction(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "select t_type,category,amount,date from transaction where user_id=?",(user_id)
    )
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    conn.close()

def update_transaction(user_id):
    conn =create_connection()
    cursor = conn.cursor()

    t_id = int(input("enter transation ID to update:"))
    new_amount = float(input("enter new amount"))

    cursor.execute("""update transaction set amount=? where id=? and user_id=?""",
                   (new_amount,t_id,user_id))
    
    conn.commit()
    if cursor.rowcount>0:
        print("Transaction updated sucessfully")
    else:
        print("Transtion not found")

    conn.close()

def delete_transaction(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    t_id = int(input("enter transaction id to delete"))

    cursor.execute("""delete from transactions where id=? and user_id=?"""
                   ,(t_id,user_id))
    conn.commit()

    if cursor.rowcount>0:
        print("Transaction delete successfully")
    else:
        print("Transaction not found")

    conn.close()