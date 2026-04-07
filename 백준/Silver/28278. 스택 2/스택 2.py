import sys

def solve():
    # 1. 모든 입력을 한 번에 읽어와서 속도 극대화
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # 2. 반복문 최적화 (N을 별도로 관리)
    it = iter(input_data)
    N = int(next(it))
    
    stack = []
    # 3. 출력 데이터를 리스트에 담아 한 번에 출력 (sys.stdout.write)
    results = []
    
    for _ in range(N):
        op = next(it)
        
        if op == "1":
            stack.append(next(it))
        elif op == "2":
            results.append(stack.pop() if stack else "-1")
        elif op == "3":
            results.append(str(len(stack)))
        elif op == "4":
            results.append("0" if stack else "1")
        elif op == "5":
            results.append(stack[-1] if stack else "-1")
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()