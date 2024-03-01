from model.models import Customer, Customers


def create_customers():
    janet = Customer(
        name="Janet Thomas",
        age=64,
        id="abc",
        accountId="1234",
        email="janetthomas@gmail.com",
        recent_change="Recently turned 64",
        current_products=[]
    )

    john = Customer(
        name="John Collins",
        age=42,
        id="abcd",
        accountId="4321",
        email="johncollins@xyzcompany.com",
        recent_change="Child recently turned 25",
        current_products=[]
    )

    oliver = Customer(
        name="Oliver Paul",
        age=42,
        id="abcd",
        accountId="4321",
        email="oliverpaul@gmail.com",
        recent_change="Purchased new vehicle",
        current_products=[]
    )

    mary = Customer(
        name="Mary Green",
        age=42,
        id="abcd",
        accountId="4321",
        email="marygreen@abcinsurance.com",
        recent_change="Recently moved to new home",
        current_products=[]
    )

    sam = Customer(
        name="Sam Anthony",
        age=42,
        id="abcd",
        accountId="4321",
        email="samanthony@xyzcompany.com",
        recent_change="Dental coverage upgraded",
        current_products=[]
    )

    customer_list = list()
    customer_list.append(john)
    customer_list.append(janet)
    customer_list.append(oliver)
    customer_list.append(mary)
    customer_list.append(sam)

    customer_list = Customers(
        totalSize=5,
        records=customer_list
    )

    return customer_list
