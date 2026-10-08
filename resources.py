resources = [
    {
        "id": "R001",
        "name": "Laptop",
        "category": "Electronics",
        "total": 10,
        "available": 10
    },
    {
        "id": "R002",
        "name": "Keyboard",
        "category": "Accessories",
        "total": 5,
        "available": 5
    },
    {
        "id": "R003",
        "name": "Headset",
        "category": "Accessories",
        "total": 3,
        "available": 3
    }
]

fellows = {
    "F001": "Ada",
    "F002": "John",
    "F003": "Grace"
}

borrow_records = []


def add_resource():
    resource_id = input("Enter resource ID: ")
    name = input("Enter resource name: ")
    category = input("Enter resource category: ")
    total = input("Enter total units: ")

    # Check for duplicate ID
    for resource in resources:
        if resource["id"] == resource_id:
            print("Error: Resource ID already exists.")
            return

    # Validate total units
    try:
        total = int(total)
    except ValueError:
        print("Error: Total units must be a whole number.")
        return

    if total <= 0:
        print("Error: Total units must be greater than 0.")
        return

    # Create the new resource
    new_resource = {
        "id": resource_id,
        "name": name,
        "category": category,
        "total": total,
        "available": total
    }

    # Add it to the inventory
    resources.append(new_resource)

    print("Resource added successfully.")


def list_resources():
    if not resources:
        print("No resources available.")
        return

    for resource in resources:
        print(
            f'{resource["id"]} | '
            f'{resource["name"]} | '
            f'{resource["category"]} | '
            f'Total: {resource["total"]} | '
            f'Available: {resource["available"]}'
        )


def borrow_resource():
    fellow_id = input("Enter fellow ID: ")

    # Check that the fellow exists
    if fellow_id not in fellows:
        print("Error: Fellow ID not found.")
        return

    resource_id = input("Enter resource ID: ")

    # Find the resource
    resource = None

    for item in resources:
        if item["id"] == resource_id:
            resource = item
            break

    # Check that the resource exists
    if resource is None:
        print("Error: Resource ID not found.")
        return

    # Get and validate quantity
    quantity = input("Enter quantity: ")

    try:
        quantity = int(quantity)
    except ValueError:
        print("Error: Quantity must be a whole number.")
        return

    if quantity <= 0:
        print("Error: Quantity must be greater than 0.")
        return

    # Check available stock
    if quantity > resource["available"]:
        print(
            f'Error: Only {resource["available"]} units are available.'
        )
        return

    # Update inventory
    resource["available"] -= quantity

    # Record the borrowing
    borrow_record = {
        "fellow_id": fellow_id,
        "resource_id": resource_id,
        "quantity": quantity
    }

    borrow_records.append(borrow_record)

    print(
        f'{fellows[fellow_id]} successfully borrowed '
        f'{quantity} {resource["name"]}(s).'
    )




def return_resource():
    fellow_id = input("Enter fellow ID: ")
    resource_id = input("Enter resource ID: ")
    quantity = input("Enter quantity to return: ")

    # Check that the fellow exists
    if fellow_id not in fellows:
        print("Error: Fellow ID not found.")
        return

    # Validate quantity
    try:
        quantity = int(quantity)
    except ValueError:
        print("Error: Quantity must be a whole number.")
        return

    if quantity <= 0:
        print("Error: Quantity must be greater than 0.")
        return

    # Find the fellow's loan
    loan = None

    for record in borrow_records:
        if (
            record["fellow_id"] == fellow_id
            and record["resource_id"] == resource_id
        ):
            loan = record
            break

    # Check that the fellow has this resource
    if loan is None:
        print("Error: This fellow has no active loan for that resource.")
        return

    # Check that they are not returning more than they borrowed
    if quantity > loan["quantity"]:
        print(
            f'Error: You can only return {loan["quantity"]} unit(s).'
        )
        return

    # Find the resource
    resource = None

    for item in resources:
        if item["id"] == resource_id:
            resource = item
            break

    if resource is None:
        print("Error: Resource ID not found.")
        return

    # Update inventory
    resource["available"] += quantity

    # Update borrowing record
    loan["quantity"] -= quantity

    # Remove the record if the full loan was returned
    if loan["quantity"] == 0:
        borrow_records.remove(loan)

    print(
        f'{fellows[fellow_id]} successfully returned '
        f'{quantity} {resource["name"]}(s).'
    )



def search_resources():
    search_term = input("Enter resource name to search: ")

    found = False

    for resource in resources:
        if search_term.lower() in resource["name"].lower():
            print(
                f'{resource["id"]} | '
                f'{resource["name"]} | '
                f'{resource["category"]} | '
                f'Total: {resource["total"]} | '
                f'Available: {resource["available"]}'
            )
            found = True

    if not found:
        print("No resources found.")



def generate_report():
    total_units = 0
    available_units = 0

    # Calculate total and available units
    for resource in resources:
        total_units += resource["total"]
        available_units += resource["available"]

    borrowed_units = total_units - available_units

    print("\n===== INVENTORY REPORT =====")
    print(f"Total units: {total_units}")
    print(f"Available units: {available_units}")
    print(f"Currently borrowed: {borrowed_units}")

    # Low-stock resources
    print("\nLow-stock resources:")

    low_stock_found = False

    for resource in resources:
        if resource["available"] < 3:
            print(
                f'- {resource["name"]} '
                f'({resource["available"]} available)'
            )
            low_stock_found = True

    if not low_stock_found:
        print("None")

    # Calculate borrowed units by resource
    borrowed_by_resource = {}

    for record in borrow_records:
        resource_id = record["resource_id"]
        quantity = record["quantity"]

        borrowed_by_resource[resource_id] = (
            borrowed_by_resource.get(resource_id, 0) + quantity
        )

    # Find the resource(s) with the most borrowed units
    if borrowed_by_resource:
        most_borrowed = max(borrowed_by_resource.values())

        leaders = []

        for resource_id, quantity in borrowed_by_resource.items():
            if quantity == most_borrowed:
                leaders.append(resource_id)

        print("\nMost borrowed resource(s):")

        for resource_id in leaders:
            for resource in resources:
                if resource["id"] == resource_id:
                    print(
                        f'- {resource["name"]} '
                        f'({most_borrowed} borrowed)'
                    )
    else:
        print("\nMost borrowed resource(s): None")




def show_menu():
    print("\n===== RESOURCE MANAGEMENT SYSTEM =====")
    print("1. Add resource")
    print("2. List resources")
    print("3. Borrow resource")
    print("4. Return resource")
    print("5. Search resources")
    print("6. Filter by category")
    print("7. Generate report")
    print("8. Exit")


def main():
    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_resource()
        elif choice == "2":
            list_resources()
        elif choice == "3":
            borrow_resource()
        elif choice == "4":
            return_resource()
        elif choice == "5":
            search_resources()
        elif choice == "6":
            filter_by_category()
        elif choice == "7":
            generate_report()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 8.")


if __name__ == "__main__":
    main()

