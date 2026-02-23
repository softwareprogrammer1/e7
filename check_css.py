
import sys

def check_braces(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    stack = []
    for i, char in enumerate(content):
        if char == '{':
            stack.append(i)
        elif char == '}':
            if not stack:
                print(f"Extra closing brace at index {i}")
            else:
                stack.pop()
    
    if stack:
        for pos in stack:
            print(f"Unclosed open brace at index {pos}")
            # Show context
            start = max(0, pos - 50)
            end = min(len(content), pos + 50)
            print(f"Context: ...{content[start:end]}...")
    else:
        print("All braces are balanced.")

if __name__ == "__main__":
    check_braces(sys.argv[1])
