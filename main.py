# QNX Easy-Check - Helps beginners check if project is ready for QNX 8.0
import os

def check_project(folder):
    print("=== QNX Easy-Check ===")
    print(f"Checking folder: {folder}\n")
    
    score = 0
    total = 4
    
    # 1. Check README
    if os.path.exists(os.path.join(folder, "README.md")):
        print("[PASS] README.md found - Has build instructions")
        score += 1
    else:
        print("[FIX] README.md missing - Add build and run instructions")
    
    # 2. Check LICENSE
    if os.path.exists(os.path.join(folder, "LICENSE")):
        print("[PASS] LICENSE found")
        score += 1
    else:
        print("[FIX] LICENSE missing - Add a license file")
    
    # 3. Check for code files
    files = os.listdir(folder)
    code_files = [f for f in files if f.endswith(('.c', '.cpp', '.py'))]
    if code_files:
        print(f"[PASS] Code files found: {code_files}")
        score += 1
    else:
        print("[FIX] No code files found - Add .c, .cpp or .py files")
    
    # 4. Check for QNX mention
    if os.path.exists(os.path.join(folder, "README.md")):
        with open(os.path.join(folder, "README.md")) as f:
            text = f.read().lower()
            if "qnx" in text and "8.0" in text:
                print("[PASS] README mentions QNX 8.0")
                score += 1
            else:
                print("[FIX] README must mention QNX 8.0 and how to build")
    
    print(f"\nResult: {score}/{total}")
    if score == total:
        print("READY FOR QNX 8.0!")
    else:
        print("Please fix the items above.")

if __name__ == "__main__":
    folder = input("Enter project folder path (or . for current): ")
    if folder == "":
        folder = "."
    check_project(folder)
