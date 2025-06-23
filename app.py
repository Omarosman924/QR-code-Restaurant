from flask import Flask, render_template, request , jsonify , redirect, url_for
from sqlalchemy.orm import sessionmaker
from sqldp import engine, MenuItem , Order , OrderItem

app = Flask(__name__)

Session = sessionmaker(bind=engine)
session = Session()

@app.route("/<int:table_id>")
def menu(table_id):
    menu_items = session.query(MenuItem).all()
    return render_template("menu.html", menu_items=menu_items, table_id=table_id)

@app.route("/add-to-order/<int:table_id>", methods=["POST"])
def api_add_to_order(table_id):
    data = request.form.to_dict()
    order = []
    for i in range(1, int(len(data)/2) + 1):
        quantity = int(data[f"quantities[{i}]"])
        price = float(data[f"prices[{i}]"]) * quantity
        if quantity <= 0 :
            continue 
        
        order.append({"id": i, "price": price, "quantity": quantity})

        # 🟩 Step 1: Create a new Order
    new_order = Order(
        table_id=table_id,
        total_price=price,
        status="Pending"
    )
    session.add(new_order)
    session.commit()

    # 🟩 Step 2: Add items to OrderItem table
    for item in order:
        order_item = OrderItem(
            order_id=new_order.id,
            item_id=item["id"],
            quantity=item["quantity"]
        )
        session.add(order_item)

    session.commit()

    return redirect(url_for("menu", table_id=table_id))

@app.route("/orders")
def view_orders():
    orders = session.query(Order).order_by(Order.id.desc()).all()
    return render_template("orders.html", orders=orders)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
