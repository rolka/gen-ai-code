import requests

def fetch_todos():
    url = "https://jsonplaceholder.typicode.com/todos"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad status codes
        
        todos = response.json()
        
        # Print first 10 TODO items
        for todo in todos[:10]:
            print(f"ID: {todo['id']}")
            print(f"Title: {todo['title']}")
            print(f"Completed: {'✅ Yes' if todo['completed'] else '❌ No'}")
            print("-" * 40)
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

# Run the function
fetch_todos()
